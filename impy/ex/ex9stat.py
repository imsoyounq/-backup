# -*- encoding:utf-8 -*-

a = []
while True:
    b = int(input("숫자 "))
    if b == 0:
        print "종료합니다."
        break
    else:
        a.append(b)
        print "mean:",sum(a)/len(a),", max:",max(a),", min:",min(a),
        print ", stdev:"
        continue

# mean: 10, 이 아니라 mean: 10 , 처럼 ,앞에 공백 추가
# 캡처 formatter 안됨
