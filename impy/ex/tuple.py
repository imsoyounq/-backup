import random
a = range(10)
random.shuffle(a)
print a
for i in range(len(a)): # why range(len(a)), instead of range(a)?
    for j in range(len(a)):
        if a[i] < a[j]:
          a[i], a[j] = a[j], a[i] # ???

print "sorted: ", a

