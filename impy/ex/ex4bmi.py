# -*- coding:utf-8 -*-
while True:
    try:
        a = float(input("키를 입력하세요: "))*0.01
        b = float(input("몸무게를 입력하세요: "))
        BMI = float(b/(a*a))
        print "BMI는 %.2f 입니다." % BMI
        break
    except:
        print "숫자만 입력하세요."

