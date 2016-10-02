n = input()
pf = {}
d = 2
while d*d <= n:
    c = 0
    while (n % d) == 0:
        c += 1
        n /= d
    if c > 0:
        pf[d] = c
    d += 1
if n > 1:
    pf[n] = 1

for k, v in pf.iteritems():
    print k, v

print pf


        
