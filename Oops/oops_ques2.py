class Account():
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc
    def credit(self,amount):
        self.bal+=amount
        print("credited amount=",amount)
    def debit(self,amount):
        self.bal-=amount
        print("debited amount=",amount)
    def print_bal(self):
        print(self.bal)
s1=Account(1000,123)
s1.credit(200)
s1.debit(100)
s1.print_bal()
    