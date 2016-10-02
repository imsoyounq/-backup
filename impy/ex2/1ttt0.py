from random import randint
"""
def board():
    print '''1 2 3
    4 5 6
    7 8 9
    '''
"""
'''
ttt = [{1:1, 2:2, 3:3}, {4:4, 5:5, 6:6}, {7:7, 8:8, 9:9}]
[range(1,4), range(4,7), range(7,10)]
'''
'''
for i in ttt:
    for key in i:
        print i[key],
# prints 1 2 3 4 5 6 8 9 7 (wrong order)

for key in ttt[0]:
    print ttt[0][key],
for key in ttt[1]:
    print ttt[1][key],
for key in ttt[2]:
    print ttt[2][key],
'''

ttt = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
'''
a = []
for i in range(9):
    a.append(ttt[i])
''' 
board = [
        ttt[1], ttt[2], ttt[3], 
        ttt[4], ttt[5], ttt[6], 
        ttt[7], ttt[8], ttt[9]
        ]

def win():
    if ttt[1] == ttt[2] == ttt[3] or\
            ttt[4] == ttt[5] == ttt[6] or\
            ttt[7] == ttt[8] == ttt[9] or\
            ttt[1] == ttt[4] == ttt[7] or\
            ttt[2] == ttt[5] == ttt[8] or\
            ttt[3] == ttt[6] == ttt[9] or\
            ttt[1] == ttt[5] == ttt[9] or\
            ttt[3] == ttt[5] == ttt[7]:
                return True
    else: pass

def print_board(board): 
    print board[0], board[1], board[2]
    print board[3], board[4], board[5]
    print board[6], board[7], board[8]

def turn_p():
    p = int(input("\nX: "))
    ttt[p] = "X"
    board[p-1] = ttt[p]
''' 
    print_board(board) ### prints twice at random??? 
''' 
'''
    if win() == True: 
        print "YOU WIN!"
        break ### break outside loop???
''' 
def turn_c():
    while True: 
        c = randint(1,9)
        if ttt[c] != "X" and ttt[c] != "O":
            print "\nO: %d" % c
            ttt[c] = "O"
            board[c-1] = ttt[c]
            break
'''
    if win() == True: 
        print "YOU LOSE!"
        break
'''

print_board(board)

while True:
    turn_p()
    print_board(board)
    if win() == True: 
        print "YOU WIN!"
        break
    turn_c()
    print_board(board)
    if win() == True:
        print "YOU LOSE!"
        break
