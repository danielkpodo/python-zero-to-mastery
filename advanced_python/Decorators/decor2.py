def user_decorator(func):
    def wrapper_func(name):
        print("*" * 10)
        func(name)
        print("*" * 10)
    return wrapper_func


@user_decorator
def greet_user(name):
    print("Hello %s" % (name))


greet_user("narh")

# Explanation -> the function greet_user get passed into the user_decorator func
# Under the hood this func is saying, a = my_decorator(hello)


# Dealing with multiple arguments!
# This syntax is why decorators are sooo powerful, refer to this
# This is known as decorator patterns
def members_decorator(func):
    def new_members(*args, **kwargs):
        func(*args, **kwargs)
    return new_members


@members_decorator
def greet_member(username, age):
    print(f"Welcome {username}, {age}")


greet_member("narh", 30)
