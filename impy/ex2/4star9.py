n = int(input("number: "))
a = "*"
#for i in range(n):
#def a1():
'''result = ""
for i in range(n+1):
    result += a*n +"\n" + a+" "*(i-1)**2+a+"\n" + a*n
    a = result
print result
'''
'''
#print a*n+"\n" + a+len(a)+a+"\n" + a*n
print a*n
print a+" "*len(a)+a
'''

b = a*n +"\n" + a+" "*n**0+a+"\n" + a*n
c = b*n +"\n" + b+" "*n**1+b+"\n" + b*n
d = c*n +"\n" + c+" "*n**2+c+"\n" + c*n
print d


