def total(*numbers):

    sum_value = 0

    for num in numbers:
        sum_value = sum_value + num

    return sum_value

print(total(1, 2, 3, 4, 5))