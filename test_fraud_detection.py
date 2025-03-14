import pandas as pd
from src.fraud_detector import FraudDetection

def test_fraud_detection():
    data = pd.DataFrame({
        'amount': [500, 2000, 15000],
        'transaction_type': [1, 2, 2],
        'account_age': [12, 1, 0]
    })

    detector = FraudDetection()
    detector.train_model(data)
    
    result = detector.detect_fraud(data)
    assert 'is_fraud' in result.columns
