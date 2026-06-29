#8. Password Validation
# Allow the user only three attempts to enter the correct password. If all attempts fail, display "Account Locked".

password = "python123"

for i in range(3):

    user = input("Enter password: ")

    if user == password:
        print("Login Successful")
        break

else:
    print("Account Locked")