with open('TOQ1.txt', 'r') as Q:
    print Q.readline()
    print Q.readline()
    print Q.readline()
    print Q.readline()

with open('TOQ1.txt', 'w') as Q:
    Q.write(bears.upper())
    Q.write(beets.lower())
