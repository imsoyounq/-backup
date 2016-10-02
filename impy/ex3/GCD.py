a = input("#1: ")
b = input("#2: ")
for i in range(a, 0, -1):
    if a%i == 0 and b%i == 0:
        print "GCD = %d" % i
        break
