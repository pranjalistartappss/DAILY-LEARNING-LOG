def employee(**details):

    print("Name:", details["name"])
    print("Age:", details["age"])
    print("City:", details["city"])

employee(
    name="Rahul",
    age=25,
    city="Delhi"
)