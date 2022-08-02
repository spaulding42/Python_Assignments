class User:
    all_users = []
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
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

user1 = User("Devin", "Spaulding", "dspaulding@codingdojo.com", 37)
user2 = User("Steve", "Jobs", "sjobs@icloud.com", 66)
user3 = User("Mark", "Zuck", "mzuck@facebook.com", 45)

user1.display_info().enroll().spend_points(50).display_info()

user2.enroll().spend_points(80).display_info()

# for users in User.all_users:
#     users.display_info()


# user3.spend_points(40)

