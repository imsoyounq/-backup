# -*- coding:utf-8 -*-

text = raw_input('입력: ')
count = dict()
words = text.split()
for word in words:
    count[word] = count.get(word,0) + 1

answer = ''
maximum = 0
for w, c in count.items():
    if c > maximum:
        answer = w
        maximum = c

print answer, maximum


charcters = list(text)
