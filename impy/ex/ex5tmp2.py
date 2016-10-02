# -*-encoding:utf-8 -*-

def cf(a):
    return a*1.8+32
def fc(a):
    return (a-32)/1.8

print """
변환하고 싶은 단위를 선택하세요.
1. C -> F
2. F -> C"""
m=int(input())

if m==1:
    c=int(input("\nC -> F 를 선택했습니다. 섭씨 온도를 입력하세요.\n"))
    print c,"C 를 화씨로 변환하면", cf(c),"F 입니다." 

else:
    f=int(input("\nF -> C 를 선택했습니다. 화씨 온도를 입력하세요.\n"))
    print "%dF 를 섭씨로 변환하면 %.2fC 입니다." % (f, fc(f))


# print c,"C를~" 출력시 [c를]이 아니라 [c 를]인 이유? (,이 공백?)
# 함수 리턴값에 소수점 지정 어떻게?
