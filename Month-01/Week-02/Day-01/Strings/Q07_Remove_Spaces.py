text = input("Enter string: ")
result = ""

for i in text:
    if i == " ":
        result += i

print(result)