def make_prediction(model, input_data):
    """
    Make a prediction using the trained model.
    
    :param model: The trained model.
    :param input_data: Preprocessed data for prediction.
    :return: Model's prediction.
    """
    prediction = model.predict(input_data)
    return prediction
