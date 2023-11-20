class Acount:
    def __init__(self, real_acount):
        self.balance = 100
        self.acount = real_acount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance = self.balance - amount
            return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

Jan = Acount("Jan")
Jan.acount
Jan_count =  Jan.deposit(100)

