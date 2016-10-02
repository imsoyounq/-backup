# -*- coding:utf-8 -*-
print "변환하고 싶은 단위를 선택하세요."
a = int(input("\n1. °C >> °F\n2. °F >> °C\n\n"))

if a==1:
    print "\n°C >> °F 를 선택하셨습니다.",
    c1 = float(input("섭씨 온도를 입력하세요.\n\n"))
    f1 = float(c1*1.8 + 32)
    print "%.0f°C 를 화씨로 변환하면, %.2f°F 입니다." % (c1,f1)

else:
    print "\n°F >> °C 를 선택하셨습니다.",
    f2 = float(input("화씨 온도를 입력하세요.\n\n"))
    c2 = float((f2-32) / 1.8) 
    print "%.0f°F 를 섭씨로 변환하면, %.2f°C 입니다." % (f2,c2)






