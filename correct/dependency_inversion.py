class PaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount):
        self.payment_gateway.charge(amount)


class PaymentGateway:
    def charge(self, amount):
        pass


class StripePaymentGateway(PaymentGateway):
    def charge(self, amount):
        # Charge the payment using Stripe API
        pass


class PayPalPaymentGateway(PaymentGateway):
    def charge(self, amount):
        # Charge the payment using PayPal API
        pass