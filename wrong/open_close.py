# Let's say we have a `PaymentProcessor` class that handles payments for a website.
# It has a method called `process_payment()` that processes the payment.
# Now, we want to add a new payment method called `Bitcoin`.
# To do this, we need to modify the `PaymentProcessor` class to add a new case for `Bitcoin`.


class PaymentProcessor:
    def __init__(self, payment_method, amount):
        self.payment_method = payment_method
        self.amount = amount

    def process_payment(self):
        if self.payment_method == "Credit Card":
            # Process Credit Card payment
            pass
        elif self.payment_method == "PayPal":
            # Process PayPal payment
            pass
        # New case for Bitcoin
        elif self.payment_method == "Bitcoin":
            # Process Bitcoin payment
            pass