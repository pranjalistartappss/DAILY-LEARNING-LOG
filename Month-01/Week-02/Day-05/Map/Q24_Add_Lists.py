first_list = [1, 2, 3]

second_list = [4, 5, 6]

sum_list =  list(map( lambda first, second: first + second,first_list,second_list ))

print(sum_list)


nums = [1, 2, 3]

result = map(lambda x: x*x, nums)

print(type(result))