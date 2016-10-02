a = map(int, raw_input('first point: ').split())
b = map(int, raw_input('second point: ').split())
c = map(int, raw_input('third point: ').split())

def cross(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

v1 = (a[0] - b[0], a[1] - b[1])
v2 = (a[0] - c[0], a[1] - c[1])

# if v1 x v2 == 0, then v1, v2, v3 are on the same line
if cross(v1, v2):
    print 'triangle'
else:
    print 'line'
