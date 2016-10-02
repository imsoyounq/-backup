'''
prime = [n for n in range(1,1001)]
for i in prime:
    for j in range(1, 35):
        if i > j and i in prime:
            if i%j == 0:
                prime.remove(i)
                break
print prime
'''
prime = [n for n in range(1,1001)]
j = 2
for i in range(1, 1001):
    for j in range(2, 1001):
        if i > j:
            if i%j == 0:
                prime.remove(i)
                j += 1
                break
        else:
            j += 1
            continue

print prime
