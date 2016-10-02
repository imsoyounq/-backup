n = input()
p = [int(item) for item in raw_input().split()]

p.sort()
s = []
a = 0
for i in range(n):
    a += p[i]
    s.append(a)

print sum(s)

