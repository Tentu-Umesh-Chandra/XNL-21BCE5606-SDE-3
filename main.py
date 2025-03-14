from fastapi import FastAPI
from app.routes import router  # Correct import path
from src.transaction_processor import TransactionProcessor
from src.fraud_detector import FraudDetector
from src.load_balancer import LoadBalancer  # Add this import

app = FastAPI()
app.include_router(router)
# Correct Initialization with Required Arguments
fraud_detector = FraudDetector()
load_balancer = LoadBalancer()
processor = TransactionProcessor(fraud_detector, load_balancer)  # ✅ Correct

@app.get("/")
def read_root():
    return {"message": "Welcome to XNL Fintech Project!"}

@app.get("/health")
def health_check():
    return {"status": "Server running successfully!"}