f = open("new.txt", 'w')
for i in range(1, 11):
    data = "Line number %d.\n" % i
    f.write(data)
f.close()

# readline
with open("new.txt", 'r') as f:
    line = f.readline()
    print line

# readline_all
with open("new.txt", 'r') as f:
    while True:
        line = f.readline()
        if not line: break
        print line

# readlines
#f = open("new.txt", 'r')
#lines = f.readlines()
#for line in lines:
#    print line
#f.close()

# read()
with open("new.txt", 'r') as f:
    data = f.read()
    print data

# adddata
with open("new.txt", 'a') as f:
    for i in range(11,20):
        data = "Line number %d.\n" % i
        f.write(data)
