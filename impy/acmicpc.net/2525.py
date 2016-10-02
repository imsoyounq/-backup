a = raw_input()
h1,m1 = map(int, a.split())
b = input()

a = h1*60 + m1
r = (a+b)%(60*24)

h = r/60
m = r%60
print h,m

