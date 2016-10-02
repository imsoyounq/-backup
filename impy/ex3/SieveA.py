primes = [1]*1001

primes[0] = 0
primes[1] = 0

for i in range(2, 1001):
    if primes[i]:
        for j in range(i*i, 1001, i):
            primes[j] = 0

for p, v in enumerate(primes):
    if v:
        print p,
