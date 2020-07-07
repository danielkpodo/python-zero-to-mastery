
class UserRegistration:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def register_user(self, password):
        print(
            f"Hello! {self.name}, your email is {self.email} with passode {password} is now active")


user = UserRegistration("Dzigbordi", "dzidzi@gmail.com")
user.register_user("arbynarh")
