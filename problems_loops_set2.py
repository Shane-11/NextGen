print("Create a password")
password = input()

while len(password) < 8 or password == password.lower():
    print("Try Again")
    password = input()

print("Success")
