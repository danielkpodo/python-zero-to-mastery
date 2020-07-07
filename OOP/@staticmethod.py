# we will use the @staticmethod when we do not care about the class attributes
# It works like the @classmethod except it does not have access to cls

class DescribeUser:
    # this is a method on the actual class, which does not care about the class attr
    @staticmethod
    def identify_user(username, age):
        return f"Your username is {username} and you are {age}yrs old"


print(DescribeUser.identify_user("narh", 267))
