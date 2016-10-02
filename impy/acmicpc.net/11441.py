n = input()
a = [int(item) for item in raw_input().split()]
m = input()

s = [0]*100001
s[0] = a[0]

for i in range(1, n):
    s[i] = s[i-1] + a[i]

#print a[:10]
#print s[:10]

for _ in range(m):
    i, j =(int(item) for item in raw_input().split())
    print (s[j-1] - s[i-2])

