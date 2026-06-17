
marks = {"Math":50, "Ss":70, "English":50}

total = sum(marks.values())
average = sum(marks.value()) / len(marks)

print(total)
print(average)

if average >= 40:
    print("Pass")
else:
    print("Fail")