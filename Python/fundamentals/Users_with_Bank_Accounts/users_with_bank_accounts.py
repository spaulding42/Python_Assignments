# ---------------------------------BankAccount Class Declaration -------------------------------------
from re import A


class BankAccount:
    all_Accounts = []
    def __init__(self, int_rate, account_name = "Checking", balance = 0):
        self.account_name = account_name
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_Accounts.append(self)
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of: ${amount} into {self.account_name} was successful.")
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw of: ${amount} from {self.account_name} was successful.")
        else:
            print(f"Insufficient funds. You attempted to withdraw ${amount} but only had ${self.balance} in your account. $5 overdraft fee has been applied and you still didn't get your money. Umadbro?")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"{self.account_name} account balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            print(f"{self.int_rate*100}% Interest applied. New balance: ${self.balance}")
        return self

#----------------------------------------User Class Declaration --------------------------------------------
class User:
    all_users = []
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = [BankAccount(0.02, "Checking"), BankAccount(0.02, "Savings")]
        User.all_users.append(self)

    def display_info(self):
        print("--------------------------------")
        print("First Name: " + self.first_name)
        print("Last Name: " + self.last_name)
        print("Email Address: " + self.email)
        print("Age: " + str(self.age))
        print("Is rewards member: " + str(self.is_rewards_member))
        print("Gold card points earned: " + str(self.gold_card_points))
        print("--------------------------------")
        return self

    def enroll(self):
        print(f"enrolling {self.first_name} {self.last_name}...")
        if self.is_rewards_member == True:
            print("Already a member.")
        else:
            print("Congradulations on becomming a member!")
            self.is_rewards_member = True
            self.gold_card_points += 200
        return self

    def spend_points(self, amount):
        print(f"Spending {amount} points...")
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            print("Points spent successfully!")
        else:
            print(f"Insufficient points! You have {self.gold_card_points} points in your account.")
        return self
    
    def make_deposit(self, amount = 100):
        print(f"{self.first_name}'s deposit")
        self.account[0].deposit(amount)
        return self

    def make_withdrawl(self, amount = 100):
        print(f"{self.first_name}'s withdraw")
        self.account[0].withdraw(amount)
        return self

    def display_user_balance(self):
        for bank_accounts in self.account:
            bank_accounts.display_account_info()
        return self
    def transfer_money(self,amount,from_account,other_user):
        for account_selection in self.account:
            if account_selection.account_name == from_account:
                if account_selection.balance >= amount:
                    self.make_withdrawl(amount)
                    other_user.make_deposit(amount)
                else:
                    print(f"You lack the funds to transfer {other_user.first_name} ${amount} from your {account_selection.account_name} account")

        
            


Devin = User("Devin", "Spaulding", "dspaulding@email.com", 37)
Steve = User("Stephen", "Strange", "drstrange@marvel.com", 50)

Devin.make_deposit(1010)

Devin.make_withdrawl(99)

Devin.account[1].deposit(300)

Devin.display_user_balance()

print("loaning steve money")
Devin.transfer_money(100,"Checking", Steve)


