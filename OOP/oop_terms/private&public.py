# In python there is not true private variable like in order langs that you will use the private keyword
# Nonetheless in class when we see  a variable with underscore_anything it means it is a private variabke
# So the underscore in python is a convention that means please do not touch this
# giving privacy is to help us to prevent overwriting our code
# the double __ is also a convention that means you shouldnt ever touch this or modify this
# We would never run our own dunder or magic methods

class RegisterUser:

    def __init__(self, username, age):
        self.name = name
        # underscore before age means it is a private
        # # the underscore means this age var should not be modified
        self._age = age


# Puclic by default all things in a class are public
