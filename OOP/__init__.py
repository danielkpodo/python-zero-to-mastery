#  we can safeguard our code in the constructor-> __init__ func to make sure things are working properly
# e.g setting age retriction more than 18
# setting default parameters


class GrantLicense:
    def __init__(self, username, age):
        if age >= 18:
            self.username = username
            self.age = age

    def register_user(self):
        try:
            print(
                f"Dear {self.username} your age {self.age} passed for the license")
        except AttributeError:
            print("Your age does not meet the minimum requirement for self driving")


user = GrantLicense("narh", 20)
user.register_user()
