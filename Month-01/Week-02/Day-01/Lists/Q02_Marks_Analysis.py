#  Take 5 marks from the user and store them in a list. Calculate:
# Total
# Average
# Highest Marks
# Lowest Marks

marks = []

total = 0

for i in range(5):
    mark = int(input("Enter mark: "))
    marks.append(mark)

    total += mark

    if i == 0:
        highest = mark
        lowest = mark
    else:
        if mark > highest:
            highest = mark

        if mark < lowest:
            lowest = mark

average = total / 5

print(total)
print(average)
print(highest)
print(lowest)