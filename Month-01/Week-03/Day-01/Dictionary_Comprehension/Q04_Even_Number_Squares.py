#Q04. Create a dictionary of even numbers from 1 to 20 and their squares.

even_square = {num: num**2 for num in range(1, 21) if num % 2 == 0}

print(even_square)