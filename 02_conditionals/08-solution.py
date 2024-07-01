password = input("Enter your password: ")

if len(password) < 6:
    print("Password is weak")
elif len(password) < 10:
    print("Password is medium")
else:
    print("Password is strong")

