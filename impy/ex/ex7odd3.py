# -*- coding:utf-8 -*-

q = raw_input('숫자 범위를 두 개의 숫자로 입력하세요: ')
p = q.split()
a = int(p[0])
b = int(p[1])

if a%2 == 1:
    result=0
    for i in range(a,b+1,2):
        result += i**2
    print result,"입니다."

else:
    result=0
    for i in range(a+1,b+1,2):
        result += i**2
    print result,"입니다."

