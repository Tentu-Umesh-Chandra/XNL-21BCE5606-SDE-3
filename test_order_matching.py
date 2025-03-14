from src.order_matching import OrderBook, Order

def test_order_matching():
    order_book = OrderBook()
    order_book.add_order(Order(1, 100, 5, 0), 'buy')
    order_book.add_order(Order(2, 100, 5, 1), 'sell')

    result = order_book.match_orders()

    assert result == ["Matched 5 units at price 100"]
