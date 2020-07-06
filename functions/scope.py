# Scope simply means what variables do I have access to
# when you defined a variable inside the global scope you can use it inside of an if block, function


# there are two types of scope
# function scope and global scope
# variables defined within a func cannot be accessed by other things especially in the global scope


# Python scope rules:
# 1. check local scope
# 2. check parent scope
# 3. check global scope
# 4. check built-in function
# parameters are considered local variables


# How to use global variables
# global is a way for us to access global variables, however it is not a good way of doing thing
total = 0

# Doing the counter with the global keyword
# def count():
#     global total
#     total += 1
#     return total


# count()
# count()
# print(count())


# A better way to do this is what we call depency injection

# passing the total as a parameter
def counter(total):
    total += 10
    return total


print(counter(total))


# Why care abt scope
# scope helps us so that our programs that clog up a lot of memory
# it helps us to utilize ur compter resources well
