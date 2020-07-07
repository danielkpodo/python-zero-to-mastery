
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe_player(self):
        print(f"Your username is {self.name} and you are {self.age}yrs old")


player1 = PlayerCharacter("narh", 23)
player1.describe_player()
