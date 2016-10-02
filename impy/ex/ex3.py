a = int(raw_input("a: "))
b = int(raw_input("b: "))
if a > b:
    a,b = b,a
result = 0
for i in range(a,b+1):
    result += i
print result
print type(result)

with open('answer.txt', 'w') as f:
    f.write(str(result))

