n = input("1st number : ")
m = input("2nd number : ")
if n < m:
    n, m = m, n

nPm = n
mF = m
for i in range(1, m):
    nPm *= (n-i)
    mF *= (m-i)

nCm = nPm / mF 
print nCm
