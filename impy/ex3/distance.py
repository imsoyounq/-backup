import math

a = raw_input("x1,y1 : ")
a = a.split(',')
x1 = float(a[0])
y1 = float(a[1])

b = raw_input("x2,y2 : ")
b = b.split(',')
x2 = float(b[0])
y2 = float(b[1])

a = y1 - y2
b = x1 - x2
c2 = a**2 + b**2

c = math.sqrt(c2)
print c
