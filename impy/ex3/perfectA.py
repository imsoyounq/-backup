n = input('n: ')

s = 0

for i in xrange(1, n):
    if n % i == 0:
        s += i

if s == n:
    print '%d is a perfect number' % n
else:
    print '%d is not a perfect number' % n
