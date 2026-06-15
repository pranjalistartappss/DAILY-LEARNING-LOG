username = "admin"
password = "1234"

attempts = 0

while attempts < 3:

    user = input("Enter Username: ")
    pwd = input("Enter Password: ")

    if user == username and pwd == password:
        print("Login Successful")
        break

    else:
        print("Invalid Username or Password")

    attempts += 1

if attempts == 3:
    print("Account Locked")