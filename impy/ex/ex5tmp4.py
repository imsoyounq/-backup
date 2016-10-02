# -*- coding:utf-8 -*-

try:
    #option = int(input("변환하고 싶은 단위.\n 1. C > F   2. F > C\n"))
    #if option == 1:
    t = raw_input("온도를 입력하세요.\n")
    if ('c' in t.lower()):
        t = float(t[:-1])
        print '섭씨 %.2f > 화씨 %.2f' % (t, t*1.8+32)
    elif ('f' in t) or ('F' in t):
        t = float(t[:-1])
        print '화씨 %.2f > 섭씨 %.2f' % (t, ((t-32)/1.8))
except:
    pass
