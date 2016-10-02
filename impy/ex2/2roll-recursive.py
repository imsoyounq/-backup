# -*- coding:utf-8 -*-
#n = input()
n = 5

a = []
for i in range(n):
    a.append([0]*n)

def wrap(s, st):
    """ s: sth wrap, st: starting number """
    global a, n
    if 2 * s >= n:
        return
    for j in range(s, n-s):
        a[s][j] = st
        st += 1
    for j in range(1+s, n-s):
        a[j][n-1-s] = st
        st += 1
    for j in range(n-s-2, s-1, -1):
        a[n-1-s][j] = st
        st += 1
    for j in range(n-s-2, s, -1):
        a[j][s] = st
        st += 1
    wrap(s+1, st)

wrap(0, 1)

for row in a:
    for item in row:
        print '%2d' % item,
    print ''
