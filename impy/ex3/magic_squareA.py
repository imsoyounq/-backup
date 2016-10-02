n = 5

sq = []
for _ in range(n):
    sq.append([0]*n)

row = 0
col = n/2
num = 1
#sq[row][col] = num

for _ in range(n**2):
    if sq[row][col] > 0:
        row += 2
        col -= 1
        row %= n
        col %= n

    sq[row][col] = num
    num += 1
    row -= 1
    col += 1
    row %= n
    col %= n

for row in sq:
    for item in row:
        print '%2d ' % item,
    print ''
