t = input()
a = 5*60
b = 60
c = 10

if t%10 != 0: 
    print -1
else:
    a2 = t/a
    b2 = t%a/b
    c2 = t%b/c 
    print a2,b2,c2
    
