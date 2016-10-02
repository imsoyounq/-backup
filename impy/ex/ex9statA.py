# -*- coding:utf-8 -*-

#numpy

numbers = []
s = 0
std = 0
while True:
    a = float(input('number: '))
    if abs(a) < 0.000001: break #abs absolute value 절대값
    # if a == 0:break 라고 해도 된다
    numbers.append(a)
    mean = float(sum(numbers))/len(numbers)

    stdev = sum([(float(n)-mean)**2 for n in numbers])/float(len(numbers))
    # stdev = []
    # for n in numbers:
    #   stdev.append((float(n)-mean)**2)
    
    statistic = 'mean: %.2f, max: %.2f, min: %.2f, stdev: %.2f'

    print statistic % (mean, max(numbers), min(numbers), stdev)

#이렇게 하면 조금 비효율적. 합을 s += a, mean = s/len(a), 표준편차도 가능
#M 이때까지 나온 수 중 가장 큰 수, m은 작은 수
'''
M = 0 
m = 0 ---0대신 None이라고 쓰면 음수도 된대~
if a > M:
    M = a 
    이렇게 최대값 출력하면 numbers 리스트 모든 수를 다 검토하지 않아도 된다
'''

