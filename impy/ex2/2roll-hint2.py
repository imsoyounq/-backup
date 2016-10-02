# -*- coding:utf-8 -*-
#n = input()
#입력 대신
n = 7
#초기화
a = []
for i in range(n):
   a.append([0]*n)

# ㄱ+ㄴ 한바퀴 만들기
c = 1
for i in range(n):
    for j in range(i, n-i):
        a[i][j] = c
        c += 1
    for j in range(1+i, n-i):
        a[j][n-1-i] = c
        c += 1
    for j in range(1+i, n-i):
        a[n-1-i][n-1-j] = c
        c += 1
    for j in range(1+i, n-1-i):
        a[n-1-j][i] = c
        c+=1

# ㄱ+ㄴ 한바퀴 출력
for row in a:
    for item in row:
        print '%2d' % item,
    print ''


