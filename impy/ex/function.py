# -*- coding: utf-8 -*-

def add(a, b):
    return a + b

def mul(a, b):
    return a * b
while True:
    a = int(raw_input("a: "))
    b = int(raw_input("b: "))

    print add(a, b)
    print mul(a, b)

    if a*b == 0:
        break

print '종료되었습니다.'

