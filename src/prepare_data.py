import pandas as pd
import numpy as np

def prepare_data():
    # Number of rows
    n_rows = 100
    n_cols = 5

    # Generate random float data for features
    feature_data = np.random.rand(n_rows, n_cols)

    # Generate random binary data for the target
    target_data = np.random.randint(2, size=n_rows)

    # Create a DataFrame for features
    df_features = pd.DataFrame(feature_data, columns=[f'feature_{i}' for i in range(1, n_cols + 1)])

    # Add the target column to the DataFrame
    df_features['target'] = target_data

    # Save the DataFrame to a CSV file
    df_features.to_csv('data/features.csv', index=False)

if __name__ == "__main__":
    prepare_data()
