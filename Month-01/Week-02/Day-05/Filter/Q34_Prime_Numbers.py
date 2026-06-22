def prime(num):

    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

prime_nums = list(filter(prime, range(1, 51)))

print(prime_nums)