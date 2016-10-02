a = input("#1: ")
b = input("#2: ")
if a > b:
    (a, b) = (b, a)
for i in range(a, a*b+1):
    if i%a == 0 and i%b == 0:
        print "LCM = %d" % i
        break
