# -*- coding:utf-8 -*-
#n = input()
#입력 대신
n = 4
#초기화
a = []
for i in range(n):
   a.append([0]*n)

# ㄱ자 만들기
c = 1
for i in range(n):
   for j in range(n-i):
       a[i][j] = c
       c += 1
   for j in range(1+i, n):
       a[j][n-1-i] = c
       c += 1
# ㄱ자 출력
for row in a:
   for item in row:
       print '%2d' % item,
   print ''

# ㄴ자 만들기
b = []
for i in range(n):
   b.append([0]*n)

c=1
for k in range(n):
    for l in range(n-k):
        b[l][k] = c
        c += 1
    for l in range(1+k, n):
        b[n-1-k][l] = c
        c +=1
# ㄴ자 출력
for row in b:
   for item in row:
       print '%2d' % item,
   print ''


