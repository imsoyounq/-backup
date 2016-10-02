n = input()

a = [0]*31
a[2] = 3
a[4] = 11
for i in range(6,n+1,2):
    a[i] = 4*a[i-2] - a[i-4]
print a[n]

