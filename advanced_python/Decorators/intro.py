# Decorators have the @sign
# In python func are what we called first class citizens, i.e they can be pass around like variables

# In short -> Decorators supercharge our functions, and add extra functionality


def say_Hello(func):
    return func()


def greet():
    print("Hello")


say_Hello(greet)
