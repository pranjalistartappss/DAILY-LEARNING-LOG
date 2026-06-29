# Student Marks Validation
# Accept marks from the user.

# Conditions:
# Marks cannot be negative.
# Marks cannot exceed 100.

# Raise an exception with an appropriate message if validation fails.
class MarksError(Exception):
    pass


try:
    marks = int(input("Enter marks: "))

    if marks < 0:
        raise MarksError("Marks cannot be negative.")

    if marks > 100:
        raise MarksError("Marks cannot exceed 100.")

    print("Marks Accepted.")

except MarksError as e:
    print(e)