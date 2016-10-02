# -*- coding:utf-8 -*-
def greeting(to,n):
    for i in range(n):
        print 'Hello, ',' '.join(to)

a = raw_input("Hello, what's your name?").split()

if len(a) > 1:
    greeting(a[:-1], int(a[-1]))

