from flask import Flask, request, jsonify
import os
from utils.data_loading import load_data
from utils.data_processing import preprocess_data
from models.train import train_models_by_industry
from models.predict import make_prediction

app = Flask(__name__)

# Load and/or train models during server initialization
# This will return a dictionary of models trained for each industry
data, target = load_data()  # Assuming load_data() returns X and y
processed_data, processed_target = preprocess_data(data, target)
models, _ = train_models_by_industry(processed_data, processed_target)

@app.route('/')
def index():
    return "Welcome to the Machine Learning API!"

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to make predictions.
    Assumes incoming request has a JSON object with a key 'data' and a key 'industry' specifying the model to use.
    """
    data = request.json.get('data')
    industry = request.json.get('industry')

    # Data validation and preprocessing can be done here
    processed_data, _ = preprocess_data(data)

    if industry not in models:
        return jsonify({"error": f"No model trained for industry: {industry}"}), 400

    prediction = make_prediction(models[industry]['model'], processed_data)

    return jsonify({"prediction": prediction.tolist()})  # Convert numpy array to list for JSON serialization

if __name__ == '__main__':
    # Retrieve PORT and DEBUG setting from environment if defined, otherwise default to safe values
    PORT = int(os.getenv('PORT', '5000'))
    DEBUG = os.getenv('DEBUG', False) == 'True'

    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)

