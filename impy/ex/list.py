a = [ ]
with open('TOQ1.txt', 'r') as f:
    for line in f.readlines():
        a.append(line)

print a[-3]
