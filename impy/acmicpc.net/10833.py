n = input()
result = 0
for i in range(n):
    a = raw_input()
    a,b = map(int, a.split())
    r = b%a
    result += r
print result
