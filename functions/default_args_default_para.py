

def resolve_user(user, location):
    print(f"My name is {user} and I come from {location}")


# positional arguments
resolve_user("Daniel", "Kasseh")

# default parameters


def check_user(user="lewis", location="Brazil"):
    print(f"My name is {user} and I come from {location}")


check_user("Daniel", "Kasseh")


def identify_user(user="lewis", location="Brazil"):
    print(f"My name is {user} and I come from {location}")


# keyword arguments
identify_user(location="Tamatoku", user="Brad Schiff")
