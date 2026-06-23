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


# from functools import reduce

# students = [
#     (101, "Pranjali", 85),
#     (102, "Rahul", 92),
#     (103, "Ankit", 78)
# ]

# total_marks = reduce(
#     lambda total, student: total + student[2],
#     students,
#     0
# )

# print("Total Marks:", total_marks)



squares = {x: x*x for x in range(1, 6)}
print(squares)


# l = [1,2,3,4,5]
# freq = {}
# for i in l:
#     if i in freq:
#         freq[i] += 1

#     else:
#         freq[i] = 1

# print(freq)


# fruits = ["mango", "banana", "apple"]

# d = {}

# for fruit in fruits:
#     count = 0

#     for ch in fruit:
#         count += 1

#     d[fruit] = count

# print(d)


# fruits = ["mango":44, "banana":55, "apple":45]

# d = {fruit: len(fruit) for fruit in fruits}

# print(d)
dict3 = {"paridhi": 65000,"avantika": 55000,"gurman": 50000,"pranjali": 70000}

new_salary = {
    name: salary + salary * 10 // 100 if salary > 55000 else salary
    for name, salary in dict3.items()
}

print(new_salary)


dict3 = { "paridhi": 65000, "avantika": 55000, "gurman": 50000, "pranjali": 70000}

result = {
    name: {
        "salary": salary + salary * 10 // 100 if salary > 55000 else salary,
        "bonus": salary * 10 // 100 if salary > 55000 else 0
    }
    for name, salary in dict3.items()
}

print(result)