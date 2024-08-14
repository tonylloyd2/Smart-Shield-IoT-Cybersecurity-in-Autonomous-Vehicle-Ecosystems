import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the large dataset
data = pd.read_csv('../data/raw_data/cybersecurity_data_large.csv')

# Separate features and labels
X = data.drop('label', axis=1)
y = data['label']

# Identify categorical columns
categorical_cols = X.select_dtypes(include=['object']).columns
numeric_cols = X.select_dtypes(include=['number']).columns

# Create a preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ])

# Create a pipeline that combines preprocessing and model training
pipeline = Pipeline(steps=[('preprocessor', preprocessor)])

# Apply preprocessing to the features
X_processed = pipeline.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

# Save the processed data
pd.DataFrame(X_train).to_csv('../data/processed_data/X_train.csv', index=False)
pd.DataFrame(X_test).to_csv('../data/processed_data/X_test.csv', index=False)
pd.DataFrame(y_train).to_csv('../data/processed_data/y_train.csv', index=False)
pd.DataFrame(y_test).to_csv('../data/processed_data/y_test.csv', index=False)

print("Data preprocessing complete. Processed files saved in 'data/processed_data/'.")
