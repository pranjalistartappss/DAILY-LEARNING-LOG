set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

unique = set1 ^ set2
# ^ = Symmetric Difference
# Returns elements present in either set but not both.(unique element)

print("Unique Elements:", unique)