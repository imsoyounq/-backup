a = input()
def leapyear():
    if a%400 == 0:
        return 1
    if a%100 == 0:
        return 0
    if a%4 == 0:
        return 1
    else: return 0

print leapyear()

