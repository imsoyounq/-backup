def leapyear():
    if a%400 == 0:
        return True
    if a%100 == 0:
        return False
    if a%4 == 0:
        return True
    else: return False

while True:
    a = input("leap year?: ")
    if a == 0000:
        break
    print leapyear()

