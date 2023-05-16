from abc import ABC, abstractmethod

# To follow the Open-Closed Principle,
# we can create an abstract `PaymentMethod` class and then create concrete classes for each
# payment method that extends the `PaymentMethod` class.
# This way, we can add new payment methods to our program without modifying the `PaymentProcessor` class.


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class CreditCard(PaymentMethod):
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        # Process Credit Card payment
        pass


class PayPal(PaymentMethod):
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        # Process PayPal payment
        pass


class Bitcoin(PaymentMethod):
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        # Process Bitcoin payment
        pass


class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self):
        self.payment_method.process_payment()