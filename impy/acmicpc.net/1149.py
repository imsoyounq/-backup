g = input()
a = []
cost = []
for _ in range(n):
    s = [int(item) for item in raw_input().split()]
    a.append(s)
    cost.append([0]*3)

cost[0][0] = a[0][0]
cost[0][1] = a[0][1]
cost[0][2] = a[0][2]

for idx, _ in enumerate(a):
    if idx > 0:
        cost[idx][0] = min(cost[idx-1][1], cost[idx-1][2]) + a[idx][0]
        cost[idx][1] = min(cost[idx-1][0], cost[idx-1][2]) + a[idx][1]
        cost[idx][2] = min(cost[idx-1][0], cost[idx-1][1]) + a[idx][2]

print min(cost[n-1])

