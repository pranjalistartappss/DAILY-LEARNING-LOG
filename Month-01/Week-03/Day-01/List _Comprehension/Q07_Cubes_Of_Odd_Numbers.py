#Q07. Create a list of cubes of odd numbers from 1 to 30.

cubes = [num**3 for num in range(1, 31) if num % 2 != 0]

print(cubes)

