class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            self._orders = []
        else:
            raise ValueError("Name must be a string of at least 3 characters.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _):
        raise AttributeError("Coffee name is immutable and cannot be changed.")

    @property
    def orders(self):
        return self._orders

    def add_order(self, order):
        self._orders.append(order)

    @property
    def customers(self):
        return list({order.customer for order in self._orders})

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        prices = [order.price for order in self._orders]
        return sum(prices) / len(prices) if prices else 0
