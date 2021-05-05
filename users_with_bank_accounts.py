class BankAccount:
    def __init__(self,balance=0,interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if self.balance < 0:
            print("Insufficient funds: Charging a 5$ fee")
            self.balance -= 5
            return self
        else:    
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0: 
            interest = self.balance * self.interest_rate
            self.balance += interest
            return self
        else:
            self.balance = self.balance
            return self

class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(balance=0,interest_rate=0.01)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    
    def make_transfer(self, from_user, amount):
        from_user.make_withdrawal(amount)
        self.make_deposit(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

kris = User("Kris Bratvold", "kris@gmail.com")
bob = User("Bob Guy", "bob@gmail.com")
bill = User("Bill Dude", "bill@gmail.com")


kris.make_deposit(200).display_user_balance()