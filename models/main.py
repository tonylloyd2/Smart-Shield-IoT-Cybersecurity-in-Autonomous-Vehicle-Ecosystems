import pandas as pd
import joblib

# Load the trained model
model = joblib.load('best_cybersecurity_model.pkl')

# Load the training data to get the feature names
X_train = pd.read_csv('../data/processed_data/X_train.csv')

# Print the columns of X_train to understand the feature names
print("Columns in X_train:", X_train.columns)

# Generate sample data with correct feature names
sample_data = pd.DataFrame({
    '0': [0.374540118847363, 0.950714306409916, 0.731993941811405, 0.598658484197037, 0.156018640442437, 0.155994520336203, 0.0580836121681995, 0.866176145774935, 0.601115011743209, 0.708072577796046, 0.0205844942958024, 0.969909852161994, 0.832442640800422, 0.212339110678276],
    '1': [0.59515562394826, 0.364717142859127, 0.00537562009219494, 0.56108772599392, 0.896570411148597, 0.531716901963098, 0.780487681882826, 0.161954309061228, 0.137297667853683, 0.89394354233452, 0.782998185753691, 0.347410331684328, 0.800172351573337, 0.0753255470627904],
    '2': [0.101811663740822, 0.29828347490409, 0.636571670522715, 0.435670921528103, 0.220577718365374, 0.990797419151043, 0.654223820664918, 0.820192514898904, 0.904737208970246, 0.137785159241218, 0.155397715965196, 0.307139806708775, 0.921908931063864, 0.707242159598262],
    '3': [0.1] * 14,  # Placeholder values
    '4': [0.1] * 14,  # Placeholder values
    '5': [0.1] * 14   # Placeholder values
})

# Ensure the sample data has the same columns as the training data
sample_data = sample_data[X_train.columns]

# Make predictions
predictions = model.predict(sample_data)

# Print the predictions
print("Predictions:", predictions)