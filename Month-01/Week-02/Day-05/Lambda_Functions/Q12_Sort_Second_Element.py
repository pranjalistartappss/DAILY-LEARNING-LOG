#Method - 01
data = [(1,4),(2,1),(3,2),(4,5)]

result = sorted(data, key=lambda x: x[1])

print(result)

#Method-02
data = [(1,4), (2,1), (3,2), (4,5)]

for i in range(len(data)):
    for j in range(len(data)-1):

        if data[j][1] > data[j+1][1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp

print(data)