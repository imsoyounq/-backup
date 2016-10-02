def isPalindrome(a):
    l = len(a)
    for i in range(l/2):
        if a[i] != a[l-1-i]:
            return False
    return True

s = raw_input('input: ')

print isPalindrome(s)


