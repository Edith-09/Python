class Payment:
    def pay(self):
        return "Processing payment"



class Mpesa(Payment):
    def pay(self):
        return "Paying using M-Pesa"


class Visa(Payment):
    
        pass


class PayPal(Payment):
    def pay(self):
        return "Paying using PayPal"


# Polymorphism in action
payment_methods = [Mpesa(), Visa(), PayPal()]

for method in payment_methods:
    print(method.pay())
