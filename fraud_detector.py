import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class FraudDetector:
    def __init__(self):
        self.model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
        self.scaler = StandardScaler()

    def train_model(self, data):
        features = ['transaction_amount', 'transaction_frequency', 'account_age_days']
        X = data[features]
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled)

    def detect_fraud(self, transaction):
        features = ['transaction_amount', 'transaction_frequency', 'account_age_days']
        transaction_data = pd.DataFrame([transaction])
        X_scaled = self.scaler.transform(transaction_data[features])
        prediction = self.model.predict(X_scaled)
        return prediction[0] == -1  # -1 indicates anomaly

    def calculate_risk_score(self, transaction):
        risk_score = 0
        if transaction['transaction_amount'] > 10000:
            risk_score += 5
        if transaction['transaction_frequency'] > 50:
            risk_score += 3
        if transaction['account_age_days'] < 30:
            risk_score += 2
        return min(risk_score, 10)