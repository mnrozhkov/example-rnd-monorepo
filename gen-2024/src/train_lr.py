import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression 
import time

from pathlib import Path
from dvclive import Live


def train_model_LR():

    print("Training Logistic Regression model - START")
    time.sleep(20)

    # Load the prepared data
    data = pd.read_csv('data/features.csv')

    # Extract features and target variable
    X = data.drop('target', axis=1)
    y = data['target']

    # Train the model
    model = LogisticRegression()
    model.fit(X, y)

    # Save the trained model
    joblib.dump(model, 'models/model_LR.pkl')

    with Live() as live:
        live.log_artifact(
            path='models/model_LR.pkl',
            type="model",
            name="model_LR",
            labels=["lr", "example-rnd-monorepo", "gen-2024"],
        )

    print("Training Logistic Regression model - COMPLETE")

if __name__ == "__main__":
    train_model_LR()
