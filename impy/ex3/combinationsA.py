n = input('n: ')
m = input('m: ')

ans = 1

for i,p in enumerate(range(n, n-m, -1)):
    ans *= p
    ans /= i+1

print ans
