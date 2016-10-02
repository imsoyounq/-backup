n = input()
a = raw_input()
a = list(map(int, a.split()))
d = [1]*len(a)
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            d[i] = max(d[j]+1, d[i]) 
            
print max(d)
