# Custom Exception - Invalid Age
# Create a custom exception named InvalidAgeError.
# Raise it if the user's age is less than 18.
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("You are eligible.")

except InvalidAgeError as e:
    print(e)