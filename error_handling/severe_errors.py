# Sometimes errors can be so disastrous we do wanna catch them but also stop our program
# from running

# we raise the error and give it a custom error -> It is rare you will do this, it useful for

try:
    result = 1 / 2
    raise ValueError('Cannot divide by zero')
    # you can also raise Exceptions
   #  raise Exception("Hmmmn, not possible")

finally:
    print("ok")
