class BankAccount:
    all_Accounts = []
    def __init__(self, int_rate, balance = 0):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_Accounts.append(self)
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of: ${amount} was successful.")
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawing: ${amount}")
        else:
            print(f"Insufficient funds. You attempted to withdraw ${amount} but only had ${self.balance} in your account. $5 overdraft fee has been applied and you still didn't get your money. Umadbro?")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            print(f"{self.int_rate*100}% Interest applied. New balance: ${self.balance}")
        return self

account1 = BankAccount(.04)
account2 = BankAccount(.05)

account1.deposit(500).deposit(200).deposit(1000).withdraw(200).display_account_info().yield_interest()
account2.deposit(150).deposit(100).withdraw(100).withdraw(50).withdraw(75).withdraw(50).yield_interest().display_account_info()

for accounts in BankAccount.all_Accounts:
    accounts.display_account_info()
