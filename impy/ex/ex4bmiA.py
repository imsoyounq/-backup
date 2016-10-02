# -*- encoding:utf-8 -*-

while True:
    try:
        height = float(input("키를 입력하세요:"))/100
        weight = float(input("몸무게를 입력하세요:"))
        print 'BMI: %.2f' % (weight/(height*height))
    except NameError:
        pass
