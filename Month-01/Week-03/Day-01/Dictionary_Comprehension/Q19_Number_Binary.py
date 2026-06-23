#Q19. Create a dictionary where keys are numbers from 1 to 10 and values are their binary representations.

binary = {num: bin(num) for num in range(1, 11)}

print(binary)