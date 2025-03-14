from fastapi import APIRouter
from src.transaction_processor import TransactionProcessor
from src.fraud_detector import FraudDetector
from src.load_balancer import LoadBalancer

# Initialize components
fraud_detector = FraudDetector()  
load_balancer = LoadBalancer()    
transaction_processor = TransactionProcessor(fraud_detector, load_balancer)  

# Create router instance
router = APIRouter()

# Sample Endpoint (Add actual endpoints here)
@router.get("/health")
async def health_check():
    return {"status": "OK", "message": "Service is running successfully"}

@router.post("/process-transaction/")
async def process_transaction(transaction: dict):
    result = transaction_processor.process_transaction(transaction)
    return {"result": result}
