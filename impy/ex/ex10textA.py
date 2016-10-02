# -*- coding:utf-8 -*-

d = {}  # d = dict() 도 가능
with open('lorem1', 'r') as filename:
    lines = filename.readlines()
    #print text
    #print type(text) 보면, type이 list란다
    for line in lines:
        for word in line.split():
            word = word.strip()
            if d.get(word) == None:
                d[word] = 1
            else:
                d[word] += 1
    M = 0
    mw = ''
    for word, occurences in d.items():
        #print word, occurences
        if occurences > M:
            M = occurences
            mw = word 
    print mw, M


    #print max(d)
    #print d[max(d)]



    for char in text:
        if 'A' <= char and char <= 'Z'

