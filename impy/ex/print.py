# -*- coding: utf-8 -*-
# comment (주석)
'''
여러줄
주석은
이렇게
'''

print   "Hello, World!"   # my first program!

# print "Hello python!"

"""
'과 "은 구분 없이 쓰입니다.
"""

print   '따옴표 안에 따옴표(\')를 넣으려면'
print   '''이렇게 세 개의 따옴표를 쓴 뒤 '를 넣거나,
escape character를 사용하면 됩니다.
또는 "와 '를 번갈아서 활용해도 됩니다.
        '''

print "여\n러\n줄\n출\t력\n"

print '출력 후 줄을 바꾸지 않으려면 끝에 ,를 덧붙인다.',
print '이어서 나온다.'

name = raw_input("input your name: ") # this is a variale
print "Hi!", name, "nice to meet you!"
print "Hello, %s" % name
