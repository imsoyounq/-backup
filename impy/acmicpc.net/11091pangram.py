import string
az = string.ascii_lowercase
n = input()
for i in range(n):
    a = raw_input().lower()
    missing = filter(lambda x: x not in a, az)            
    if missing:
        print "missing %s" % missing
    else:
        print "pangram"
        

