n = int(input("number: "))
for i in range(1, n):
    print " " * (n-i) + "*" * (2*i-1)
for i in range(n):
    print " " * i + "*" * (2*(n-i)-1)

