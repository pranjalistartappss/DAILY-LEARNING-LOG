contacts = {}

contacts["Pranjali"] = "9876543210"
contacts["Rahul"] = "9123456789"

name = input("Enter name to search: ")

if name in contacts:
    print("Phone Number:", contacts[name])
else:
    print("Contact not found")