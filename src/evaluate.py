import joblib
import pandas as pd
import json
from sklearn.metrics import accuracy_score # Example metric

def evaluate_models():
    # Load models
    model = joblib.load('models/model.pkl')
    
    # Load evaluation data
    eval_data = pd.read_csv('data/features.csv')
    X_eval = eval_data.drop('target', axis=1)
    y_eval = eval_data['target']

    # Evaluate models
    predictions = model.predict(X_eval)
    
    accuracy = accuracy_score(y_eval, predictions)

    # Save metrics
    metrics = {
        'model_accuracy': accuracy,
    }
    with open('reports/metrics_report.json', 'w') as f:
        json.dump(metrics, f)

if __name__ == "__main__":
    evaluate_models()
