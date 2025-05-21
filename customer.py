from order import Order

class Customer:
    def __init__(self, name):
        self.name = name  # Triggers the name setter
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    @property
    def orders(self):
        return self._orders

    @property
    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)  # You should define `add_order` in Coffee class
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders:
            return None
        spending = {}
        for order in coffee.orders:
            spending[order.customer] = spending.get(order.customer, 0) + order.price
        return max(spending, key=spending.get)
