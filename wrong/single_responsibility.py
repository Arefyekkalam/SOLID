

# Let's say we have a class called `Order` which is responsible for handling both the order details and the order processing.
# This means that if we need to change the order processing logic,
# we will have to change the `Order` class, which violates the Single Responsibility Principle.

class Order:
    def __init__(self, order_details):
        self.order_details = order_details

    def process_order(self):
        # Processing logic here
        pass

    def save_order(self):
        # File I/O logic here
        pass