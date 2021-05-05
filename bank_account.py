class BankAccount:
    all_accounts = []
    def __init__(self,balance=0,interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.all_accounts.append(self)

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

account1 = BankAccount(500)
account2 = BankAccount(500)

account1.deposit(150).deposit(200).deposit(50).withdraw(100).yield_interest().display_account_info()
account2.deposit(50).deposit(50).withdraw(100).withdraw(200).withdraw(300).withdraw(100).withdraw(50).yield_interest().display_account_info()

