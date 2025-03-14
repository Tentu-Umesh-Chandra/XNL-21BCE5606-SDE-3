import threading
from queue import Queue
import random

class LoadBalancer:
    def __init__(self, num_workers=3):
        """
        Initialize the LoadBalancer with multiple worker queues.
        Each worker queue will handle transactions independently.
        """
        self.num_workers = num_workers
        self.queues = [Queue() for _ in range(num_workers)]
        self.locks = [threading.Lock() for _ in range(num_workers)]

    def distribute_order(self, order_data):
        """
        Distributes orders across available worker queues using a round-robin strategy.
        """
        worker_index = hash(order_data['order_id']) % self.num_workers
        with self.locks[worker_index]:  # Ensure thread safety
            self.queues[worker_index].put(order_data)
            print(f"Order {order_data['order_id']} assigned to Worker {worker_index}")

    def process_orders(self):
        """
        Processes orders in each worker queue concurrently.
        """
        threads = []
        for i in range(self.num_workers):
            thread = threading.Thread(target=self._process_queue, args=(i,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def _process_queue(self, worker_index):
        """
        Private method to process transactions in each queue.
        """
        while not self.queues[worker_index].empty():
            order = self.queues[worker_index].get()
            print(f"Processing order {order['order_id']} in Worker {worker_index}")
            # Simulate processing delay
            self._simulate_processing_time()

    def _simulate_processing_time(self):
        """
        Simulates transaction processing time with a random delay.
        """
        import time
        time.sleep(random.uniform(0.5, 2.0))  # Random delay between 0.5 - 2 seconds

