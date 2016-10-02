import bisect

n = input()
a = [int(item) for item in raw_input().split()]
a.sort()
m = input()
b = [int(item) for item in raw_input().split()]
for item in b:
    idx = bisect.bisect(a, item)
    if a[idx-1] == item:
        print 1
    else:
        print 0

