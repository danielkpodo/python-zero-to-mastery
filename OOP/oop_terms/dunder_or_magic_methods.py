# the dunder methods are special methods
# Most of the built in functions in python are implemented using the dunder methods
# They allow us to use python specific func on objects

# It also allows us to do some basic customizaton of our built in functions

# Usually we don't want to overwrite them but we just wanna know we have the power to do so

class Car:
    def __init__(self, type, color):
        self.color = color
        self.type = type

    # changing str function using using dunder

    def __str__(self):
        return f'car color is {self.color}'


# str is modified when we use this obj
car_obj = Car("Honda", "red")
print(car_obj.__str__())
print(str(car_obj))
