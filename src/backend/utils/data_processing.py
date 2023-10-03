import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(X, y):
    """
    Normalize and preprocess the data.
    :param X: Features DataFrame.
    :param y: Target DataFrame or Series.
    :return: Preprocessed X, y.
    """
    # Normalize the data without 'industry' column
    X_numeric = X.drop(columns=['industry'])
    scaler = MinMaxScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X_numeric), columns=X_numeric.columns)

    # Add the 'industry' column back to the scaled data
    X_scaled['industry'] = X['industry'].values

    return X_scaled, y
