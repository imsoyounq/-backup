n,m = (int(item) for item in raw_input().split())
t = [int(item) for item in raw_input().split()]
low, high = 1, 2000000000

while low <= high:
    mid = (low + high) / 2
    wood = 0
    for item in t:
        if item > mid:
            wood += (item - mid)
    if wood >= m:
        low = mid + 1
    else:
        high = mid - 1

print high 

# wood = sum([tree-mid for tree in tress if tree > mid])

