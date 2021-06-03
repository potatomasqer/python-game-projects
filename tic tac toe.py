from random import seed
from random import randint

board = [['0','0','0'],['0','0','0'],['0','0','0']]
seed(1)

def printb():
    print("---------------")
    print(board[0])
    print(board[1])
    print(board[2])
    print("---------------")

def check(n, T):
    n = int(n)
    if (n <= 3):
        if (board[0][n-1] == '0'):
            board[0][n-1] = T
            return True
            print("true")
        else:
            return False
    elif (n <= 6):
        if (board[1][n-4] == '0'):
            board[1][n-4] = T
            return True
        else:
            return False
    else:
        if (board[2][n-7] == '0'):
            board[2][n-7] = T
            return True
        else:
            return False

def donecheck():
    tot0 = 0
    row = 0
    for _ in board:
        col = 0
        for _ in board[row]:
            if (board[row][col] == '0'):
                tot0 += 1
            col +=1
        row += 1
    if (tot0 == 0):
        return True
    else:
        return False

def wincheck():
    #check rows
    row = 0
    for _ in board:
        if (board[row] == ['X','X','X']):
            return 1
        if (board[row] == ['O','O','O']):
            return 2
        row += 1
    #check col
    col = 0
    for _ in board: 
        if (board[0][col] == 'X' and board[1][col] == 'X' and board[2][col] == 'X'):
            return 1
        if (board[0][col] == 'O' and board[1][col] == 'O' and board[2][col] == 'O'):
            return 2
        col += 1
    #check x
    if (board[0][0] == 'X' and board[1][1] == 'X'and board[2][2] == 'X'):
        return 1
    if  (board[0][2] == 'X' and board[1][1] == 'X'and board[2][0] == 'X'):
        return 1
    if (board[0][0] == 'O' and board[1][1] == 'O'and board[2][2] == 'O'):
        return 2
    if  (board[0][2] == 'O' and board[1][1] == 'O'and board[2][0] == 'O'):
        return 2
    else:
        return 0


side = input('first or second, x for first o for second \n')
done = 0
printb()
turn = 0
i = 0
while (done == 0):
    turnComplete = 0
    while (turn%2 == 0):
        if (side == 'x' or side == 'X'):
            pn = input('your move \n')
            if (check(pn,'X') == True):
                turn += 1
        if (side == 'o' or  side == 'O'):
            n = randint(0, 8)
            if (check(n,"X") == True):
                turn += 1
            else:
                n = (n+1)%9+1
    printb()

    win = wincheck()
    if (win == 1):
        done = True
        print('X wins')
    if (win == 2):
        done = True
        print('O wins')


    while (turn%2 == 1 and done != True):
        if (side == 'o' or side == 'O'):
            pn = input('your move \n')
            if (check(pn,"O") == True):
                turn += 1

        if (side == 'x' or side == 'X'):
            n = randint(0, 8)
            if (check(n,"O") == True):
                turn += 1
            else:
                n = (n+1)%9+1
                if (donecheck()):
                    turn += 1

    printb()

    win = wincheck()
    if (win == 1):
        done = True
        print('X wins')
    if (win == 2):
        done = True
        print('O wins')

    if (turn >= 9 and done != True):
        done = True
        print("Tie")