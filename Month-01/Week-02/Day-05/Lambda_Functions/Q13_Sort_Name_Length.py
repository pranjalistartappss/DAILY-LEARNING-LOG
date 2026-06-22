#Method - 01
names = ["John","Alexander","Bob","David"]

result = sorted(names, key=lambda name: len(name))

print(result)

#Method-02
names = ["John", "Alexander", "Bob", "David"]

for i in range(len(names)):
    for j in range(len(names)-1):

        if len(names[j]) > len(names[j+1]):

            temp = names[j]
            names[j] = names[j+1]
            names[j+1] = temp

print(names)