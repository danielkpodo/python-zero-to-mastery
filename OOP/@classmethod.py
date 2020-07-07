# @classmethod is a method on the actual class
# The @classmethod is commonly referred to as a decorator
# It allows us to call the method without using any
# @class method usually takes cls as a first argument, and this refers to the parent class

class RegisterUser:
    def __init__(self, user, age):
        self.age = age
        self.user = user

    @classmethod
    def add_numbers(cls, num1, num2):
        return num1 + num2


# we can call the add_numbers with the class instantiator
user_reg = RegisterUser("narh", 26)
print(user_reg.add_numbers(20, 10))

# Essentially using the @classmethod enables us to call the func without using the instantiator
print(RegisterUser.add_numbers(100, 200))
