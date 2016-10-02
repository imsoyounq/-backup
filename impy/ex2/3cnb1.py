from random import sample

while True:
    xxx = sample(range(10), 3)
    if xxx[0] != 0:
        x = xxx[0]*100 + xxx[1]*10 + xxx[2]
        break

def guess():
    guess = raw_input("guess: ")
    ggg = []
    for i in range(3):
        ggg.append(int(guess[i]))
    return ggg

def check_strike():    
    strike = 0
    if ggg[0] == xxx[0]: 
        strike += 1
    if ggg[1] == xxx[1]:
        strike += 1
    if ggg[2] == xxx[2]:
        strike += 1
    return strike

def check_ball():
    strike = check_strike()
    ball = 0
    for i in range(3):
        if ggg[i] in xxx:
            ball += 1
            continue
    return ball-strike

def check_out():
    strike = check_strike()
    ball = check_ball()
    return 3 - strike - ball

while True:
    ggg =guess()
    strike = check_strike()
    ball = check_ball()
    out = check_out()
    if strike == 3:
        print "3 strike!"
        break
    elif strike != 3 and strike > 0: 
        print strike, "strike,",
    if ball > 0:
        print ball, "ball,",
    if out > 0:
        print out, "out",
    print '\n'
   
