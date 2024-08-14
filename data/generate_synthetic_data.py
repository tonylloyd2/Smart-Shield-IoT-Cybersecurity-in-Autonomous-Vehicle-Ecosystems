import numpy as np
import pandas as pd

# Set the number of rows for the dataset
num_rows = 1000000  # Adjust this value as needed (e.g., 10000, 50000, 100000)

# Define possible attack types
attack_types = ['normal', 'dos_attack', 'mitm_attack']

# Generate synthetic data
np.random.seed(42)
sensor_data1 = np.random.rand(num_rows)
sensor_data2 = np.random.rand(num_rows)
sensor_data3 = np.random.rand(num_rows)
attack_type = np.random.choice(attack_types, num_rows)

# Assign labels: 0 for normal, 1 for attacks
labels = np.where(attack_type == 'normal', 0, 1)

# Create a DataFrame
data = pd.DataFrame({
    'attack_type': attack_type,
    'sensor_data1': sensor_data1,
    'sensor_data2': sensor_data2,
    'sensor_data3': sensor_data3,
    'label': labels
})

# Save the dataset to a CSV file
data.to_csv('raw_data/cybersecurity_data_large.csv', index=False)

print(f"Synthetic dataset with {num_rows} rows generated and saved to 'raw_data/cybersecurity_data_large.csv'")
