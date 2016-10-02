a = int(input("a: "))
b = int(input("b: "))
result = 0
if a > b:
    a,b = b,a
for i in range(a,b+1):
    result += i
print result
with open('ex3answer.txt', 'w') as f:
    f.write(str(result))
