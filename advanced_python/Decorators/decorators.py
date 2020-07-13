# Decorator is a func that wraps another func

# This is a basic example on how to use decorators
# The decorator essentially only wraps our function so we don't have to do func_name = mydecorator(hello)

def my_decorator(func):
    def wrap_func():
        print("**********")
        func()
        print("***********")
    return wrap_func

# this function underhood -> is saying my_decorator(hello)


@my_decorator
def hello():
    print("Helooooooooooooo")


hello()


def user_decorator(func):
    def func_wrapper():
        func()
    return func_wrapper
