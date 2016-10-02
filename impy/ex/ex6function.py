# -*- coding:utf-8 -*-

to = raw_input("이름: ")
n = int(input("숫자(자연수): "))

def greeting(to, n):
    for i in range(n):
        print "Hello, %s" % to

print greeting(to, n)
