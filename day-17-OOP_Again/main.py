class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0                       #for insta app, all followers would start at 0 (you can provide a default value instead of typing 0 with each initiation)
        self.following = 0

    def boost_followers(self):
        self.followers = 5000

    def follow(self, user):
        user.followers += 1
        self.following += 1




#user_1 = User()
#user_1.id = "001"
#user_1.username = "Szymon"
#print(user_1.username)

user_1 = User("001", "Bean")
user_2 = User("002", "Yam")
print(user_1.username)

print(user_1.followers)
user_1.boost_followers()

print(user_1.followers)

user_1.follow(user_2)
print(user_2.followers)
