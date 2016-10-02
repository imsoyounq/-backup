n = input()
numbers = raw_input()
numbers = list(map(int, numbers.split()))
v = input()
#print numbers.count(v)
count = 0
for i in range(n):
    if numbers[i] == v:
        count += 1
print count
