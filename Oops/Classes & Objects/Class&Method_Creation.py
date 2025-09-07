'''Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance.'''

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    #Debit Method
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs.{amount} is debited.")
        print(f"Your Total Balance is Rs.{self.balance}")
        
    #Credit Method
    def credit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} is credited.")
        print(f"Your Total Balance is Rs.{self.balance}")
        
        
        
acc1 = Account(5000, 1234)
acc1.debit(1000)
print()
acc1.credit(10000)
print()
acc1.debit(4569)