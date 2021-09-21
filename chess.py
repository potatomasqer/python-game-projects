#the goal is to create chess or something like chess.
#to  do list
#make a board done
#put pieces on board done
#make pieces move the way the have to done
#have the player control one side.(white or black)
#something in the way checker done
#how the ai works
    #check the current board 
    #make a move
#add check

from random import seed
from random import randint

board = [['wR','wN','wB','wQ','wK','wB','wN','wR'],
        ['wP','wP','wP','wP','wP','wP','wP','wP'],
        ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
        ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
        ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
        ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
        ['bP','bP','bP','bP','bP','bP','wP','wP'],
        ['bR','bH','bB','bQ','bK','bB','wH','wR']]

def printb():
    print("------------------------------------------------")
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])
    print(board[5])
    print(board[6])
    print(board[7])
    print("------------------------------------------------")

def sideCheck(unit,side):
    T = unit
    if side == 0: #white 
        if (T == 'bP' or T == 'bR' or T == 'bH' or T == 'bK' or T == 'bQ' or T == 'bB'):
            return True
    elif  side == 1: #black
        if (T == 'wP' or T == 'wR' or T == 'wH' or T == 'wK' or T == 'wQ' or T == 'wB'):
            return True
    if T == '0 ':
        return True
    else:
        return False
    
    

def knightCheck(loc,side):
    tpos = [] #total positions
    #up
    if sideCheck(board[loc[0]-1][loc[1]+2]): 
        tpos += [[loc[0]-1,loc[1]+2]]

    if sideCheck(board[loc[0]-1][loc[1]+2]):
        tpos += [[loc[0]-1,loc[1]-2]]

    if sideCheck(board[loc[0]-1][loc[1]+2]):
        tpos += [[loc[0]+1,loc[1]+2]]
    
    if sideCheck(board[loc[0]-1][loc[1]+2]):
        tpos += [[loc[0]+1,loc[1]-2]]

    #down

    if sideCheck(board[loc[0]-1][loc[1]+2]):
        tpos += [[loc[0]-2,loc[1]+1]]
    
    if sideCheck(board[loc[0]-1][loc[1]+2]):
        tpos += [[loc[0]-2,loc[1]-1]]
    
    if sideCheck(board[loc[0]-1][loc[1]+2]):
        tpos += [[loc[0]+2,loc[1]+1]]
    
    if sideCheck(board[loc[0]-1][loc[1]+2]):
        tpos += [[loc[0]+2,loc[1]-1]]

    return tpos


def rookCheck(loc,side):
    #up
    done = 0
    temp = [loc[0],loc[1]]
    tpos = []
    if loc[0] - 1 != -1:
        temp[0] -= 1
        done = 0
        while done == 0:
            if temp[0] != -1:
                if board[temp[0]][temp[1]] == '0 ':
                    tpos += [temp]
                else:
                    done = 1
                if sideCheck(board[temp[0]][temp[1]],side):
                    tpos += [temp]
                    done = 1
            else:
                done = 1
            temp[0] -= 1
    #down
    temp = [loc[0],loc[1]]
    if loc[0] + 1 != 8:
        temp[0] += 1
        done = 0
        while done == 0:
            if temp[0] != 8:
                if board[temp[0]][temp[1]] == '0 ':
                    tpos += [temp]
                else:
                    done = 1
                if sideCheck(board[temp[0]][temp[1]],side):
                    tpos += [temp]
                    done = 1
            else:
                done = 1
            temp[0] += 1
    #left
    temp = [loc[0],loc[1]]
    if loc[1] - 1 != -1:
        temp[1] -= 1
        done = 0
        while done == 0:
            if temp[1] != -1:
                if board[temp[0]][temp[1]] == '0 ':
                    tpos += [temp]
                else:
                    done = 1
                if sideCheck(board[temp[0]][temp[1]],side):
                    tpos += [temp]
                    done = 1
                    
            else:
                done = 1
            temp[1] -= 1
    #right
    temp = [loc[0],loc[1]]
    if loc[1] + 1 != 8:
        temp[1] += 1
        done = 0
        while done == 0:
            if temp[1] != 8:
                if board[temp[0]][temp[1]] == '0 ':
                    tpos += [temp]
                else:
                    done = 1
                if sideCheck(board[temp[0]][temp[1]],side):
                    tpos += [temp]
                    done = 1
            else:
                done = 1
            temp[1] += 1
    return tpos

def  bishopCheck(loc,side):
    done = 0
    temp = [loc[0],loc[1]]
    tpos = []
    #up right
    if loc[0] - 1 != -1 and loc[1] + 1 != 8:
        temp[0] -= 1
        temp[1] += 1
        done = 0
        while done == 0:
            if loc[0] - 1 != -1 and loc[1] + 1 != 8:
                if board[temp[0]][temp[1]] == '0 ':
                    tpos += [temp]
                else:
                    done = 1
                if sideCheck(board[temp[0]][temp[1]],side):
                    tpos += [temp]
                    done = 1
            else:
                done = 1
            temp[0] -= 1
            temp[1] += 1
    temp = [loc[0],loc[1]]

    if loc[0] - 1 != -1 and loc[1] - 1 != -1:
        temp[0] -= 1
        temp[1] -= 1
        done = 0
        while done == 0:
            if loc[0] - 1 != -1 and loc[1] - 1 != -1:
                if board[temp[0]][temp[1]] == '0 ':
                    tpos += [temp]
                else:
                    done = 1
                if sideCheck(board[temp[0]][temp[1]],side):
                    tpos += [temp]
                    done = 1
            else:
                done = 1
            temp[0] -= 1
            temp[1] -= 1
    temp = [loc[0],loc[1]]

    if loc[0] + 1 != 8 and loc[1] + 1 != 8:
        temp[0] += 1
        temp[1] += 1
        done = 0
        while done == 0:
            if loc[0] + 1 != 8 and loc[1] + 1 != 8:
                if board[temp[0]][temp[1]] == '0 ':
                    tpos += [temp]
                else:
                    done = 1
                if sideCheck(board[temp[0]][temp[1]],side):
                    tpos += [temp]
                    done = 1
            else:
                done = 1
            temp[0] += 1
            temp[1] += 1
    temp = [loc[0],loc[1]]

    if loc[0] + 1 != 8 and loc[1] - 1 != -1:
        temp[0] += 1
        temp[1] -= 1
        done = 0
        while done == 0:
            if loc[0] + 1 != 8 and loc[1] - 1 != -1:
                if board[temp[0]][temp[1]] == '0 ':
                    tpos += [temp]
                else:
                    done = 1
                if sideCheck(board[temp[0]][temp[1]],side):
                    tpos += [temp]
                    done = 1
            else:
                done = 1
            temp[0] += 1
            temp[1] -= 1
    temp = [loc[0],loc[1]]
    return tpos

def queenCheck(loc):
    tpos = rookCheck(loc)
    tpos += [bishopCheck(loc)]
    return tpos
    
def pawnCheck(loc,side):
    tpos = []
    if side == 0: #white
        if loc[0] == 1:
            if board[3][loc[1]] == '0 ': #if pawn first row allow it to go 2 down
                tpos += [[3,loc[1]]]
        if loc[0] + 1 != -1:
            if board[loc[0]+1][loc[1]] == '0 ': # can pawn go 1 down
                tpos += [[loc[0]+1,loc[1]]]
        if loc[0] + 1 != -1 and loc[1] - 1 != -1:
            if sideCheck(board[loc[0]+1][loc[1]-1],side):
                tpos += [[loc[0]+1,loc[1]-1]]
        if loc[0] + 1 != -1 and loc[1] + 1 != 8:
            if sideCheck(board[loc[0]-1][loc[1]+1],side):
                tpos += [[loc[0]+1,loc[1]+1]]
    if side == 1:
        if loc[0] == 6: 
            if board[4][loc[1]] == '0 ': #if pawn first row allow it to go 2 up
                tpos += [[3,loc[1]]]
        if loc[0] + 1 != -1:
            if board[loc[0]+1][loc[1]] == '0 ': # can pawn go 1 up
                tpos += [[loc[0]+1,loc[1]]]
        if loc[0] + 1 != -1 and loc[1] - 1 != -1:
            if sideCheck(board[loc[0]+1][loc[1]-1],side):
                tpos += [[loc[0]+1,loc[1]-1]]
        if loc[0] + 1 != -1 and loc[1] + 1 != 8:
            if sideCheck(board[loc[0]-1][loc[1]+1],side):
                tpos += [[loc[0]+1,loc[1]+1]]
    return tpos


def fullcheck(side):
    #look at all pieces form 1 side
    Flatboard = []
    for i in board:
        for a in i:
            Flatboard += a
    Allpos = []
    a = -1
    for i in Flatboard: #geting cords of any piece using 1 number
        a += 1
        b = [int(a/8),a%8]

    
    


        



#Game start
print('Welcome to chess, this game will be a bit diffrent than most other games you have played')
print('to make a move you must input you starting cords starting at 0,0 from the top left and down to 7,7 at the bottom left')
print('to finish a move you have to also input the final cords for that piece, if it dosnt work you have to do it again')
print('to end the game you have to capture the opposing king, so regular chess after the checkmate')
print('have fun')
print('as most of my games choices between two words are answered with numbers so let us continue')
run = 0
while run == 0: # start the game
    numb = input('will this be a 1 or 2 player game: ')
    numb = int(numb)