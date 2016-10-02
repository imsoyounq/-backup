# -*- coding: utf-8 -*-
def draw():
    global board
    print '  | 1 2 3'
    print '-'*10
    for idx, row in enumerate(board):
        print '%c |' % (chr(idx+65)),
        for item in row:
            if item == 1:
                print 'O',
            elif item == 10:
                print 'X',
            else:
                print ' ',
        print ''


def initialize():
    global board
    board = []
    for _ in range(3):
        board.append([0] * 3)


def quit():
    while True:
        q = raw_input('quit? (y/n) ')
        if q[0] == 'y':
            return True
        else:
            return False


def getInput():
    global board
    while True:
        p = raw_input('place your stone[ABCabc] [123]: ').strip().split()
        r = ord(p[0].upper()) - ord('A')
        c = ord(p[1]) - ord('1')
        if 0 <= r < 3 and 0 <= c < 3 and board[r][c] == 0:
            break
        else:
            print 'Wrong position'
    return (r, c)


def over():
    global board

    # horizontal
    for row in board:
        s = sum(row)
        if s == 3 or s == 30:
            return s

    # vertical
    for col in zip(*board):  # zip(*board): transpose
        s = sum(col)
        if s == 3 or s == 30:
            return s

    # diagonal
    s = 0
    t = 0
    for i in range(3):
        s += board[i][i]
        t += board[i][3-1-i]
    if s == 3 or s == 30:
        return s
    if t == 3 or t == 30:
        return t

    # full
    for row in board:
        for item in row:
            if item == 0:
                return 0
    return 1

def game():
    global board
    turn = 1
    while True:
        draw()
        r, c = getInput()
        board[r][c] = turn
        
        if turn == 1:
            turn = 10
        else:
            turn = 1
        
        o = over()
        if o == 3:
            print '--------------'
            print ' player O win!'
            print '--------------'
        elif o == 30:
            print '--------------'
            print ' player X win!'
            print '--------------'
        elif o == 1:
            print '--------------'
            print '     draw~    '
            print '--------------'

        if o > 0:
            break

    draw()


if __name__ == '__main__':
    while True:
        initialize()
        game()
        if quit():
            print 'quit~'
            break
        else:
            print '---------------\nplay new game!\n---------------'
