import heapq
import threading
from sortedcontainers import SortedDict

class Order:
    def __init__(self, order_id, price, quantity, timestamp):
        self.order_id = order_id
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp

    def __lt__(self, other):
        # Price-Time Priority (Higher price first for buy, lower price first for sell)
        return self.price > other.price if self.price == other.price else self.timestamp < other.timestamp

class OrderBook:
    def __init__(self):
        self.buy_orders = []  # Max-heap for buy orders
        self.sell_orders = []  # Min-heap for sell orders
        self.lock = threading.Lock()  # Ensures thread safety

    def add_order(self, order, order_type):
        with self.lock:
            if order_type == "buy":
                heapq.heappush(self.buy_orders, (-order.price, order))  # Max-heap behavior for buy orders
            else:
                heapq.heappush(self.sell_orders, (order.price, order))  # Min-heap behavior for sell orders

    def match_orders(self):
        matches = []
        with self.lock:
            while self.buy_orders and self.sell_orders:
                top_buy = self.buy_orders[0][1]  # Highest buy price
                top_sell = self.sell_orders[0][1]  # Lowest sell price

                if top_buy.price >= top_sell.price:  # Match condition
                    matched_qty = min(top_buy.quantity, top_sell.quantity)
                    matches.append((top_buy.order_id, top_sell.order_id, matched_qty))

                    # Update quantities or remove matched orders
                    if top_buy.quantity > matched_qty:
                        top_buy.quantity -= matched_qty
                    else:
                        heapq.heappop(self.buy_orders)

                    if top_sell.quantity > matched_qty:
                        top_sell.quantity -= matched_qty
                    else:
                        heapq.heappop(self.sell_orders)
                else:
                    break  # No more matching possible
        return matches

class LoadBalancer:
    def __init__(self, num_order_books=3):
        self.order_books = [OrderBook() for _ in range(num_order_books)]
        self.next_book = 0

    def distribute_order(self, order, order_type):
        selected_order_book = self.order_books[self.next_book]
        selected_order_book.add_order(order, order_type)
        self.next_book = (self.next_book + 1) % len(self.order_books)

    def match_all_orders(self):
        matches = []
        for book in self.order_books:
            matches.extend(book.match_orders())
        return matches
