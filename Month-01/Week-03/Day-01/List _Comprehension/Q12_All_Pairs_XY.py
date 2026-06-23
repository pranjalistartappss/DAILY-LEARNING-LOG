#Q12. Create a list of all pairs (x, y) where x and y range from 1 to 5 and x != y.

pairs = [(x,y) for x in range(1,6) for y in range(1,6) if x!=y]

print(pairs)
