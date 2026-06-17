marks = {"Math":50, "Ss":70, "English":50}

top_subject = None
highest_marks = -1

for i in marks:
    if marks[i] > highest_marks:
        highest_marks = marks[i]
        top_subject = i

print("Topper Subject:", top_subject)
print("Marks:", highest_marks)