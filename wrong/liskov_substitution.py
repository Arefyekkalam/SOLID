# Let's say we have a `PaymentProcessor` class that handles payments for a website.
# It has a method called `process_payment()` that processes the payment.
# We also have a `CreditCard` class that extends the `PaymentProcessor` class and overrides the `process_payment()` method.
# However, the `CreditCard` class violates the Liskov Substitution Principle, as it modifies the preconditions of the `process_payment()` method.


class PaymentProcessor:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        # Process payment
        pass


class CreditCard(PaymentProcessor):
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