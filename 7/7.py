from math import sqrt


primes = [2, 3,]
n = 3
while len(primes) <= 10001:
    k = sqrt(n)
    for p in primes:
        if p > k:
            primes.append(n)
            break
        elif n % p == 0: 
            break
    n += 2

print primes[-1]
