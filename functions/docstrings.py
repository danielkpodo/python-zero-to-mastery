# docsting allows us to write infos abt our functions

def greet_user():
    ''' This function greets randomly '''
    print("Greet user")


greet_user()


# To check what a func does use
# . help

print(help(greet_user))


# we can also use __doc__
print(greet_user.__doc__)
