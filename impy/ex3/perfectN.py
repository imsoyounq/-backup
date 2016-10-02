n = input('Perfect Number? : ')
a = []
for i in range(1,n+1):
    if n%i == 0:
        a.append(i)
print a

b = 0
for i in range(len(a)-1):
    b += a[i]
print b

if n == b: print "PN!"
else: print "NOT a PN!"
