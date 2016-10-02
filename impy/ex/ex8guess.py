# -*- encoding:utf-8 -*-

import random
x = random.randint(1,100)

print "1에서 100까지 숫자를 맞춰보세요."
b = 0
while True:
    a = int(input())
    b += 1
    if a > x:
        print "%d보다 작습니다." % a
        continue
    elif a < x:
        print "%d보다 큽니다." % a
        continue
    else:
        print "%d번만에 맞혔습니다!" % b
        break

