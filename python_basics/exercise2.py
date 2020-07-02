username = input("What is your username: ")
password = input("Enter password: ")
password_length = len(password)
password_hash = "*" * password_length

print(
    f"Welcome {username} your password {password_hash} is {password_length} letters long")
