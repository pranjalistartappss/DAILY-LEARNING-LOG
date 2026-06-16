# Create a program that stores:
# subjects = ("Maths", "English", "Science", "Hindi", "SS")
# marks = [90, 85, 78, 88, 92]
# Print:
# Maths   : 90
# English : 85
# Science : 78
# Hindi   : 88
# SS      : 92
# Total Marks : ?
# Average     : ?
# Highest     : ?
# Lowest      : ?
# Also print:
# Result : PASS
# if average is 35 or more, otherwise:
# Result : FAIL

subjects = ("Maths", "English", "Science", "Hindi", "SS")
marks = [90, 85, 78, 88, 92]

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print(total)
print(average)
print(highest)
print(lowest)

if average >= 35:
    print("Result : PASS")
else:
    print("Result : FAIL")