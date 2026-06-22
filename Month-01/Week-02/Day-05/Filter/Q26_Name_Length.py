names = ["Ram","Shyam","John","Bob","Alexander"]

long_names = list(filter(lambda name: len(name) > 4, names))

print(long_names)