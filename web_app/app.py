# web_app/app.py
import sys
import os
import json
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify
import joblib
from datetime import datetime
import threading
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from block.blockchain_utils import initialize_blockchain, add_log_to_blockchain

app = Flask(__name__)

# Load the trained model
model = joblib.load('../models/best_cybersecurity_model.pkl')

# Initialize the blockchain
blockchain, blockchain_log_path = initialize_blockchain()

# Read the CSV file
csv_file_path = '../data/raw_data/cybersecurity_data_large.csv'
df = pd.read_csv(csv_file_path)

# Function to generate sample data
def generate_sample_data():
    sample_data = pd.DataFrame({
        '0': np.random.rand(14),
        '1': np.random.rand(14),
        '2': np.random.rand(14),
        '3': np.random.rand(14),
        '4': np.random.rand(14),
        '5': np.random.rand(14)
    })
    return sample_data

@app.route('/')
def index():
    with open(blockchain_log_path, 'r') as f:
        blockchain_data = json.load(f)
    dataset = df.to_dict(orient='records')
    return render_template('index.html', blockchain_data=blockchain_data, dataset=dataset)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    log_data = f"Prediction made: {prediction[0]}"
    add_log_to_blockchain(blockchain, [log_data], blockchain_log_path)
    
    # Convert int64 to native Python int
    prediction_value = int(prediction[0])
    
    return jsonify({'prediction': prediction_value})

@app.route('/generate_data')
def generate_data():
    sample_data = generate_sample_data()
    sample_data = sample_data[['0', '1', '2', '3', '4', '5']]
    predictions = model.predict(sample_data)
    data = sample_data.to_dict(orient='records')
    return jsonify(data=data, predictions=[int(pred) for pred in predictions])

@app.route('/predictions_for_time', methods=['GET'])
def predictions_for_time():
    time_str = request.args.get('time')
    try:
        time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return jsonify({'error': 'Invalid time format. Use YYYY-MM-DD HH:MM:SS'}), 400

    # Filter the dataset for the given time (assuming the dataset has a 'timestamp' column)
    filtered_df = df[df['timestamp'] == time_str]
    if filtered_df.empty:
        return jsonify({'error': 'No data found for the specified time'}), 404

    predictions = model.predict(filtered_df.drop(columns=['timestamp']))
    data = filtered_df.to_dict(orient='records')
    return jsonify(data=data, predictions=[int(pred) for pred in predictions])

@app.route('/get_latest_data')
def get_latest_data():
    with open(blockchain_log_path, 'r') as f:
        blockchain_data = json.load(f)
    
    # Generate sample data and make predictions
    sample_data = generate_sample_data()
    predictions = model.predict(sample_data)
    
    return jsonify({
        'blockchain_data': blockchain_data,
        'predictions': [int(pred) for pred in predictions]
    })

def background_task():
    while True:
        # Generate sample data and make predictions
        sample_data = generate_sample_data()
        predictions = model.predict(sample_data)
        
        # Log predictions to the blockchain
        log_data = f"Automated prediction made: {predictions.tolist()}"
        add_log_to_blockchain(blockchain, [log_data], blockchain_log_path)
        
        # Sleep for a specified interval (e.g., 60 seconds)
        time.sleep(60)

# Start the background task
thread = threading.Thread(target=background_task)
thread.daemon = True
thread.start()

if __name__ == '__main__':
    app.run(debug=True)