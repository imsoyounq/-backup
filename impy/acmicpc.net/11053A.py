n = input()

a = [int(item) for item in raw_input().split()]
d = [1] * len(a)

for i, _ in enumerate(a):
    for j in range(i):
        if a[j] < a[i]:
            d[i] = max(d[i], d[j]+1)

print max(d)

