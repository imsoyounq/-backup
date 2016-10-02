n = input("Divisors of: ")
divisors = []
for i in range(1, n+1):
    if n%i == 0:
        divisors.append(i)

for items in divisors:
    print "%d" % items,


