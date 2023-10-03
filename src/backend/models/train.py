import tensorflow as tf
from tensorflow import keras
import os
import sys
import ray
import numpy as np
from sklearn.model_selection import train_test_split


class MetricsHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs=None):
        self.history = {'loss': [], 'val_loss': []}

    def on_epoch_end(self, epoch, logs=None):
        self.history['loss'].append(logs['loss'])
        self.history['val_loss'].append(logs['val_loss'])

# Define the neural network model
def create_nn_model(input_shape):
    model = keras.Sequential([
        keras.layers.Dense(128, activation='relu', input_shape=(input_shape,)),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(1)  # Regression problem, so no activation in the output layer
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Define the training function with Ray's remote decorator
@ray.remote
def train_nn_model(industry, X_train, y_train, input_shape):
    nn_model = create_nn_model(input_shape)
    
    metrics_callback = MetricsHistory()
    nn_model.fit(X_train, y_train, epochs=80, batch_size=32, validation_split=0.1, verbose=2, callbacks=[metrics_callback])

def train_models_by_industry(X_scaled, y):
    """
    Train separate models for each industry in the data.
    :param X_scaled: Preprocessed features DataFrame.
    :param y: Target DataFrame or Series.
    :return: Trained models and summaries.
    """
    models = {}
    futures = []
    
    for industry, group in X_scaled.groupby('industry'):
        y_group = y[group.index]
        X_group = group.drop(columns=['industry'])

        X_train, X_test, y_train, y_test = train_test_split(X_group, y_group, test_size=0.2, random_state=42)
        future = train_nn_model.remote(industry, X_train, y_train, X_train.shape[1])
        futures.append((industry, future, X_test, y_test))
        
    summaries = []
    for industry, future, X_test, y_test in futures:
        nn_model, summary = ray.get(future)
        models[industry] = {'model': nn_model, 'X_test': X_test, 'y_test': y_test}
        summaries.append(summary)

    return models, summaries

