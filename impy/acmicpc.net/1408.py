a = raw_input()
h1,m1,s1 = map(int, a.split(':'))
b = raw_input()
h2,m2,s2 = map(int, b.split(':'))
a = h1*60*60 + m1*60 + s1
b = h2*60*60 + m2*60 + s2
r = (b-a+86400) % 86400
h3 = r/(60*60) 
m3 = r/60%60
s3 = r%60
print "%02d:%02d:%02d" % (h3, m3, s3)

