# Create a tuple of subject names and a list of marks. Print:

# Maths : 90
# English : 85
# Science : 80

# using a loop.

# Method 1
subjects = ("Maths", "English", "Science")
marks = [90, 85, 80]

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])


print()

# Method 2
students_subject = ("Maths", "English", "Science")
students_marks = [90, 85, 80]

for students_subject, students_marks in zip(students_subject, students_marks):
    print(students_subject, ":", students_marks)