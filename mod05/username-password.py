attempts = 1
username = input("username: ")
password = input("password: ")

while (username != "python" or password != "rules") and attempts < 5:
    username = input("username: ")
    password = input("password: ")
    attempts = attempts + 1
if username == "python" and password =="rules":
        print("Welcome")
else:
    print("Access Denied")