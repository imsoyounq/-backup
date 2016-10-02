n = 5
a = []
c = 1
for i in range(n):
    a.append([0]*n)
'''
for i in range(n):
    for j in range(i, n-i):
        a[i][j] = c
        c += 1
'''

for i in range(n):
    a[0][i] = c
    c += 1

for i in range(1, n):
    a[i][n-1]=c
    c += 1

for i in range(1, n):
    a[n-1][n-1-i] = c
    c += 1

for i in range(2, n):
    a[n-i][0] = c
    c += 1

for i in range(2, n):
    a[1][i-1] = c
    c += 1

for i in range(3, n):
    a[i-1][n-2] = c
    c += 1

for i in range(3, n):
    a[n-2][n-i] = c
    c += 1

for i in range(4, n):
    a[n+1-i][n-4] = c
    c += 1

for i in range(4, n):
    a[2][i-2] = c
    c += 1


for i in range(n):
    for j in range(n):
        print '%2d' % a[i][j],
    print ''

