a = raw_input("x1,y1 : ")
a = a.split(',')
x1 = float(a[0])
y1 = float(a[1])

b = raw_input("x2,y2 : ")
b = b.split(',')
x2 = float(b[0])
y2 = float(b[1])

c = raw_input("x3,y3 : ")
c = c.split(',')
x3 = float(c[0])
y3 = float(c[1])

l1 = (y2-y1) / (x2-x1)
l2 = (y3-y2) / (x3-x2)

if l1 == l2:
    print "Straight in line."
else:
    print "Not in line."

