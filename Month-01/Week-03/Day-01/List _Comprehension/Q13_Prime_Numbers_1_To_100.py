#Q13. Create a list of prime numbers between 1 and 100 using list comprehension.

primes = [num for num in range(2,100) if all(num%i!= 0 for i in range(2,num))]

print(primes)
