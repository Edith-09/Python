class MpesaAccount:
    # constructor
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance # Encapsulation

    # methods
    # deposit money
    def deposit(self, amount):
        if amount <= 0:
            return "Amount should be more than 0"
        self.__balance += amount
        return f"Confirmed, You deposited {amount}. Your New balance is {self.__balance}"
    
    # withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            return "You have insufficient amount"
        self.__balance -= amount
        return f"Confirmed, you have withdrawn {amount}. your new balance is {self.__balance}"
        
    # check balance
    def get_balance(self):
        return self.__balance
    
    # polymophic 
    def calculate_interest(self):
        return 0
    
# savings account - child classes
class Mshwari(MpesaAccount):
    def calculate_interest(self):
        return self.get_balance() * 0.05 # calculates 5%
    
class Kcb(MpesaAccount):
    def calculate_interest(self):
        return self.get_balance() * 0.03 # calculates 3%
    
# create objects / bank accounts
acc1 = MpesaAccount("746539950", "John Doe", 3000)
acc2 = Mshwari("746539950", "John Doe", 2000)

# deposit
print(acc2.deposit(500))

# withdraw
print(acc2.withdraw(200))

# balance
print(acc2.get_balance())

# calculate interest
print(acc2.calculate_interest())