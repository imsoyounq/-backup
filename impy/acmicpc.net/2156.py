n = input()
wine = []
total = []
for i in range(n):
    a = input()
    wine.append(a)
    total.append([0]*3)

#total[0][0] = 0 doesn't drink ith wine
total[0][1] = wine[0] #drinks ith wine but not the (i-1)th one
#total[0][2] = 0 drinks ith and (i-1)th wine but not the (i-2)th one 

for idx, _ in enumerate(wine):
    if idx > 0:
        total[idx][0] = max(total[idx-1])
        total[idx][1] = total[idx-1][0] + wine[idx]
        total[idx][2] = total[idx-1][1] + wine[idx]

print max(total[n-1])


'''
a = []
for _ in range(n):
    amount = input()
    a.append(amount)
a = [a]*len(a)
w[i] = max(w[i-1], w[i-2]) + w[i][n-1]
'''
