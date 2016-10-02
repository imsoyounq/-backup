# -*- coding:utf-8 -*-

a = int(input("시작 숫자: "))
b = int(input("끝 숫자: "))

if a%2 == 1:
    s=list()
    for i in range(a,b+1,2):
        s.append(i**2)
    print sum(s)

else:
    print sum([i**2 for i in range(a+1,b+1,2)])


