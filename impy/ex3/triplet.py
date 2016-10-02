'''
n = raw_input("a,b,c : ")
n = n.split(',')
a = float(n[0])
b = float(n[1])
c = float(n[2])
'''

triplet = []
for a in range(1, 101):
    for b in range(a, 101):
        for c in range(b, 101):
            if a**2 + b**2 == c**2:
                triplet.append((a,b,c))

triplet = set(triplet)
print len(triplet)
