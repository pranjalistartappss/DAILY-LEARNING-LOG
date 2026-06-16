# Take 5 student names in a list and search for a specific student name.
# If found print:
# Student Found
# otherwise:
# Student Not Found

students = ["Ram", "Mohan", "Riya", "Aman", "Priya"]

for i in range(len(students)):
    search = input("Enter student name: ")
    
    if search in students:
        print("Student Found")
    else:
        print("Student Not Found")
