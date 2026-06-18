inventory = {"Laptop": 10,"Mouse": 25,"Keyboard": 15}

product = input("Enter product name: ")

if product in inventory:
    print(inventory[product])
else:
    print("Product not found")