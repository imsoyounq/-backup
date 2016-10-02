def gcd(a, b):
    if b:
        return gcd(b, a%b)
    return a

a = input('a: ')
b = input('b: ')

print gcd(a, b)
