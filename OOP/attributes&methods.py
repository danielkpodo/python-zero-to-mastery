# Attributes are pieces of data that are dynamic
# When we instantiate an object they are going to pass in as arguments
# class obj attr is not dynamic it described into the class alone


class PlayerCharacter:
    # class obj attribute is something that does't change across instances
    membership = True

    def __init__(self, username, age, lives):
        self.username = username
        self.age = age
        self.lives = lives

    def play_game(self):
        return "Your user id is {} and you are {}yrs and has {} lives".format(self.username, self.age, self.lives)


player1 = PlayerCharacter("narh", 26, 10)

print(player1.play_game())

# we can access class obj attribute directly and even our decalred variables
print(player1.username)
print(player1.membership)
