# -*- coding: utf-8 -*-
import math

c1 = raw_input("make circle1 with x1,y1,r1 : ")
c1 = c1.split(',')
x1 = float(c1[0])
y1 = float(c1[1])
r1 = float(c1[2])

c2 = raw_input("make circle2 with x2,y2,r2 : ")
c2 = c2.split(',')
x2 = float(c2[0])
y2 = float(c2[1])
r2 = float(c2[2])

a = y1 - y2
b = x1 - x2
c2 = a**2 + b**2
c = math.sqrt(c2)

if r1 < r2: r1,r2 = r2,r1
if abs(r1-r2) == c: print "내접"
if abs(r1+r2) == c: print "외접"
if abs(r1+r2) > c and c > r1-r2: print "서로 다른 두 점에서 만남"
if abs(r1-r2) > c and c < r1 : print "포함"
if abs(r1+r2) < c: print "분리"
