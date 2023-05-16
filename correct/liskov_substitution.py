from abc import ABC, abstractmethod
# To follow the Liskov Substitution Principle, we can create a `PaymentMethod` abstract class that defines the `process_payment()` method,
# and then create concrete classes for each payment method that extends the `PaymentMethod` class.
# This way, any instance of a concrete payment method class can be used interchangeably with the `PaymentMethod` class.


class PaymentMethod(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        pass


class CreditCard(PaymentMethod):
    def __init__(self, amount, card_number, card_expiry):
        super().__init__(amount)
        self.card_number = card_number
        self.card_expiry = card_expiry

    def process_payment(self):
        if self.card_expiry < datetime.datetime.now():
            # Card has expired, do not process payment
            pass
        else:
            # Process payment
            pass


class PayPal(PaymentMethod):
    def __init__(self, amount, email, password):
        super().__init__(amount)
        self.email = email
        self.password = password

    def process_payment(self):
        # Process payment using PayPal
        pass


class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self):
        self.payment_method.process_payment()