#Q18. Create a set of prime numbers from 1 to 100.

primes = {num for num in range(2, 101) if all(num % i != 0 for i in range(2, num))}

print(primes)