import threading  # Correctly imported threading
class TransactionProcessor:
    def __init__(self, fraud_detector, load_balancer):
        self.fraud_detector = fraud_detector
        self.load_balancer = load_balancer
        self.buy_orders = []
        self.sell_orders = []
        self.lock = threading.Lock()  # No error now
