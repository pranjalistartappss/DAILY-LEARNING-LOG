#Q08. Create a dictionary containing only odd numbers from 1 to 20 and their cubes.

odd_cube = {num: num**3 for num in range(1, 21) if num % 2 != 0}

print(odd_cube)