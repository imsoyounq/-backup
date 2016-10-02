import random
a=range(10)
random.shuffle(a)
print a
print random.choice(range(1,20,2))
print random.randrange(1,20,2)
print random.randint(-5,5)
print random.random()
print random.normalvariate(0,1)
