a = ''
def p(i, j):
    global a
    if i >= j:
        return True
    return (a[i] ==a[j]) and p(i+1, j-1)

a = raw_input("input: ")

print p(0, len(a)-1)

