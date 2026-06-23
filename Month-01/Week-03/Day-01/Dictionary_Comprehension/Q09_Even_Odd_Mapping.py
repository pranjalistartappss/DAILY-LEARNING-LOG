#Q09. Create a dictionary mapping numbers from 1 to 10 to "Even" or "Odd".

result = {num: "Even" if num % 2 == 0 else "Odd" for num in range(1, 11)}

print(result)