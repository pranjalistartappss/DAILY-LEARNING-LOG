# def check(s):
#     count = 0

#     for ch in s:
#         if 'A' <= ch <= 'Z':
#             count += 1

#     if count == len(s):
#         return True
#     return False

# print(check("HELLO")) 


# def make_capital(s):
#     return s.upper()

# result = make_capital("python")
# print(result)


from functools import reduce

students = [
    (101, "Pranjali", 85),
    (102, "Rahul", 92),
    (103, "Ankit", 78)
]

total_marks = reduce(
    lambda total, student: total + student[2],
    students,
    0
)

print("Total Marks:", total_marks)
