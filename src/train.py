import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression 
import time

def train_model_LR():

    print("Training Logistic Regression model - START")
    # time.sleep(20)

    # Load the prepared data
    data = pd.read_csv('data/features.csv')

    # Extract features and target variable
    X = data.drop('target', axis=1)
    y = data['target']

    # Train the model
    model = LogisticRegression()
    model.fit(X, y)

    # Save the trained model
    joblib.dump(model, 'models/model.pkl')

    print("Training Logistic Regression model - COMPLETE")

if __name__ == "__main__":
    train_model_LR()
