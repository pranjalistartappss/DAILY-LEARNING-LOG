students = {"Aman": "A",
    "Riya": "B","Rahul": "A","Priya": "C","Neha": "B"}

grades = {}

for student, grade in students.items():

    if grade not in grades:
        grades[grade] = []

    grades[grade].append(student)

print(grades)