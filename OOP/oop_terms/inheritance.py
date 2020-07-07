# Inheritance allows new objects to take on the properties of existing objects
# After they inherit they can also extend with their own functionalities
# Those that inherit are called child classes or derived classes
# python gives us a useful tool to check if something is an instance of a class
# it follwows the convention isistance(instance, classname)

# Note anytime we create a class it also accepts a base class called the object that gives us python built-in methods


class GamePlayer:
    # you can omit __init__ if you do not have any dynamic attribute

    def greet_player(self):
        print("Welcome to aludrox game international")

# what is in bracket depicts inheritance


class PlayPoker(GamePlayer):
    # Once GamePlayer is passed as parameter it has access to all of the GamePlayer properties

    # We can also defined attr specific to the PlayPoker
    def __init__(self, username, lives):
        self.username = username
        self.lives = lives

    def play_poker(self):
        print(f"Dear {self.username} your lives left is: {self.lives}")


# instantiate PlayPoker
poker_boss = PlayPoker("Daniel Narh", 100)
# inheritance in action here
poker_boss.greet_player()

poker_boss.play_poker()
