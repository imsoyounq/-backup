# -*- coding:utf-8 -*-
def cf(a):
    return a*1.8+32
def fc(a):
    return (a-32)/1.8

a = raw_input("온도를 입력하세요\n")
a.upper() # 작동 안하는 듯?
if a.find('C') > 0:
    print a.replace("C","0")
    print float("a")
    #print "변환결과:",a,"->", cf(a),"F"




