# To follow the Single Responsibility Principle,
# we can separate the responsibilities of processing and file I/O into two separate classes - `OrderProcessor` and `OrderRepository` respectively.

class OrderProcessor:
    def __init__(self, order):
        self.order = order

    def process_order(self):
        # Processing logic here
        pass


class OrderRepository:
    def __init__(self, order):
        self.order = order

    def save_order(self):
        # File I/O logic here
        pass

# Now, if we need to change the processing logic, we only need to change the `OrderProcessor` class,
# and if we need to change the file I/O logic, we only need to change the `OrderRepository` class.