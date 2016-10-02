import bisect

n = input()
a = [int(item) for item in raw_input().split()]
m = input()
b = [int(item) for item in raw_input().split()]

a.sort()

for item in b:
    c = bisect.bisect(a, item)
    print c

