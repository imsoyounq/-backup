import math

# get input points separated by a white space
a = map(int, raw_input('first point: ').split())
b = map(int, raw_input('second point: ').split())

print math.hypot(a[0]-b[0], a[1]-b[1])
# math.hypot(x,y)
# Return the Euclidean norm, sqrt(x*x + y*y).
# This is the length of the vector from the origin to point (x,y).

