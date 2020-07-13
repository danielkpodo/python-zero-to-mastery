# Everything covered in oop

class RegisterUser:
    # actual class attribute
    user_ref_id = 100

    # class constructor | deifnes class attributes
    def __init__(self, username, email, passcode):
        self.username = username
        self.email = email
        self.passcode = passcode

    # basic class method
    def register_new_user(self):
        return f"Hello {self.username}, your email is {self.email}"

    # decorator function that allows us to use the describe_full_user func wifawt instantiation
    # takes cls as an option for the self parameter
    @classmethod
    def describe_full_user(cls, dob, reg_date):
        return f"Hello your reg_date is {reg_date} and dob is {dob} with passcode"

    # A class method that does not depend on the class attrubutes
    # Can also be used without instatiation
    @staticmethod
    def maximum_salary_finder(*args):
        return max(args)


# instantiate basic obj
user_ = RegisterUser("kpodo", "napthanewman@gmail.com", "argentina33")

# using instattion
print(user_.register_new_user())

# @static method used without instantiation, class used directly to access method
print(RegisterUser.maximum_salary_finder(10, 390, 18, 100))


# @classmethod used similar to static method
print(RegisterUser.describe_full_user("April 6, 2020", "April 4, 2020"))
