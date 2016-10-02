a = raw_input("Enter: ")
l = len(a)
b = ''
for i in range(l):
    b += a[l-1-i]

print b

if a == b: 
    print "Palindrome it is!"
else:
    print "Not a palindrome!"
