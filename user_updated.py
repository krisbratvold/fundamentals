class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email, account_balance=0):
        self.name = name
        self.email = email
        self.account_balance = account_balance
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def make_transfer(self, from_user, amount):
        from_user.make_withdrawal(amount)
        self.make_deposit(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

kris = User("Kris Bratvold", "kris@gmail.com",0)
bob = User("Bob Guy", "bob@gmail.com", 0)
bill = User("Bill Dude", "bill@gmail.com", 0)

kris.make_deposit(700).make_deposit(300).make_deposit(100).make_withdrawal(300).display_user_balance()
bob.make_deposit(250).make_deposit(100).make_withdrawal(50).make_withdrawal(30).display_user_balance()
bill.make_deposit(800).make_withdrawal(200).make_withdrawal(50).make_withdrawal(80).display_user_balance()
kris.make_transfer(bill, 200).display_user_balance()
bill.display_user_balance()