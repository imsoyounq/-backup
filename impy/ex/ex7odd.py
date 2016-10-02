# -*- coding:utf-8 -*-

a = int(input("시작 숫자: "))
b = int(input("끝 숫자: "))

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

