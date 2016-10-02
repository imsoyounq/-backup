n = 5
a = []
c = 1
for i in range(n):
    a.append([0]*n)

for i in range(n):
    for j in range(i+1):
        a[j][i-j] = c
        c += 1

for i in range(n-1):
    for j in range(i+1, n):
        a[j][n+i-j] = c
        c += 1

for i in range(n):
    for j in range(n):
        print '%2d' % a[i][j],
    print ''

