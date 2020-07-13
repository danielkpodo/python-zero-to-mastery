# A higher Order function or HOC can be of to defintion types
# 1. A function that receives another func as a parameter
# 2. Or a function that returns another func

# 1.Illustration for point 1
def greet_audience(func):
    func()

# 2. Illustration for point 2


def user_registeration():
    def say_helo():
        return 6
    return say_helo
