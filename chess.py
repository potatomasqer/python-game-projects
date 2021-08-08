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

board = [['bR','bH','bB','bQ','bK','bB','bH','bR'],['bP','bP','bP','bP','bP','bP','bP','bP'],['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],['0 ' ,'0 ','0 ','0 ','0 ','0 ','0 ','0 '],['wP','wP','wP','wP','wP','wP','wP','wP'],['wR','wH','wB','wQ','wK','wB','wH','wR']]

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
        else:
            return False
    elif  side == 1: #black
        if (T == 'wP' or T == 'wR' or T == 'wH' or T == 'wK' or T == 'wQ' or T == 'wB'):
            return True
        else:
            return False
    


def fullcheck(side):
    #look at all pieces form 1 side
    boardtmp = []
    for i in board:
        boardtmp += i

    uLoc = []
    pos = []
    if side == 0:
        #find all the pieces
        for y in range(8):
            for x in range(8):
                T = board[y][x]
                if T == 'wK' or T == 'wQ' or T == 'wB' or T == 'wP' or T == 'wR' or T == 'wH':
                    uLoc = uLoc + [[y,x]]

        for i in uLoc:
            T = board[i[0]][i[1]]
            if T == 'wk':
                tpos = []
                if i[0] + 1 != 8:
                    if board[i[0]+1][i[1]] == '0 ' or sideCheck(board[i[0]+1][i[1]],side):
                        tpos += [[i[0]+1,i[1]]]
                if i[0] - 1 != -1:
                    if board[i[0]-1][i[1]] == '0 ' or sideCheck(board[i[0]-1][i[1]],side):
                        tpos += [[i[0]-1,i[1]]]
                if i[1] + 1 != 8:
                    if board[i[0]][i[1]+1] == '0 ' or sideCheck(board[i[0]][i[1]+1],side):
                        tpos += [[i[0],i[1]]+1]
                if i[1] - 1 != 8:
                    if board[i[0]-1][i[1]] == '0 ' or sideCheck(board[i[0]-1][i[1]],side):
                        tpos += [[i[0],i[1]]-1]
                
                if i[0] - 1 != -1 and i[1] + 1 != 8:
                    if board[i[0]-1][i[1]+1] == '0 ' or sideCheck(board[i[0]-1][i[1]+1],side):
                        tpos += [[i[0]-1,i[1]+1]]
                if i[0] - 1 != -1 and i[1] - 1 != -1:
                    if board[i[0]-1][i[1]-1] == '0 ' or sideCheck(board[i[0]-1][i[1]-1],side):
                        tpos += [[i[0]-1,i[1]-1]]
                if i[0] + 1 != 8 and i[1] + 1 != 8:
                    if board[i[0]+1][i[1]+1] == '0 ' or sideCheck(board[i[0]+1][i[1]+1],side):
                        tpos += [[i[0]+1,i[1]+1]]
                if i[0] + 1 != 8 and i[1] - 1 != -1:
                    if board[i[0]+1][i[1]-1] == '0 ' or sideCheck(board[i[0]+1][i[1]-1],side):
                        tpos += [[i[0]+1,i[1]-1]]
                pos += [[i]+tpos]
            if T == 'wR':
                #up
                done = 0
                temp = [i[0],i[1]]
                tpos = []
                if i[0] - 1 != -1:
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

                temp = [i[0],i[1]]
                if i[0] + 1 != 8:
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
                
                temp = [i[0],i[1]]
                if i[1] - 1 != -1:
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

                temp = [i[0],i[1]]
                if i[1] + 1 != 8:
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
                pos += [[i]+tpos]

            if T == 'wH':
                tpos = []
                if i[0] + 2 < 8 and i[1] + 1 < 8:
                    if board[i[0]+2][i[1]+1] == '0 ' or sideCheck(board[i[0]+2][i[1]+1],side):
                        tpos += [[i[0]+2,i[1]+1]]
                if i[0] + 2 < 8 and i[1] - 1 > -1:
                    if board[i[0]+2][i[1]-1] == '0 ' or sideCheck(board[i[0]+2][i[1]-1],side):
                        tpos += [[i[0]+2,i[1]-1]]

                if i[0] - 2 > -1 and i[1] + 1 < 8:
                    if board[i[0]-2][i[1]+1] == '0 ' or sideCheck(board[i[0]-2][i[1]+1],side):
                        tpos += [[i[0]-2,i[1]+1]]
                if i[0] - 2 > -1 and i[1] - 1 > -1:
                    if board[i[0]-2][i[1]-1] == '0 ' or sideCheck(board[i[0]-2][i[1]-1],side):
                        tpos += [[i[0]-2,i[1]-1]]

                if i[0] + 1 < 8 and i[1] + 2 < 8:
                    if board[i[0]+1][i[1]+2] == '0 ' or sideCheck(board[i[0]+1][i[1]+2],side):
                        tpos += [[i[0]+1,i[1]+2]]
                if i[0] + 1 < 8 and i[1] - 2 > -1:
                    if board[i[0]+1][i[1]-2] == '0 ' or sideCheck(board[i[0]+1][i[1]-2],side):
                        tpos += [[i[0]+1,i[1]-2]]
                
                if i[0] - 1 > -1 and i[1] + 2 < 8:
                    if board[i[0]-1][i[1]+2] == '0 ' or sideCheck(board[i[0]-1][i[1]+2],side):
                        tpos += [[i[0]-1,i[1]+2]]
                if i[0] - 1 > -1 and i[1] - 2 > -1:
                    if board[i[0]-1][i[1]-2] == '0 ' or sideCheck(board[i[0]-1][i[1]-2],side):
                        tpos += [[i[0]-1,i[1]-2]]
                pos += [[i]+tpos]

            if T == 'wB':
                done = 0
                temp = [i[0],i[1]]
                tpos = []
                #up right
                if i[0] - 1 != -1 and i[1] + 1 != 8:
                    temp[0] -= 1
                    temp[1] += 1
                    done = 0
                    while done == 0:
                        if i[0] - 1 != -1 and i[1] + 1 != 8:
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
                temp = [i[0],i[1]]

                if i[0] - 1 != -1 and i[1] - 1 != -1:
                    temp[0] -= 1
                    temp[1] -= 1
                    done = 0
                    while done == 0:
                        if i[0] - 1 != -1 and i[1] - 1 != -1:
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
                temp = [i[0],i[1]]

                if i[0] + 1 != 8 and i[1] + 1 != 8:
                    temp[0] += 1
                    temp[1] += 1
                    done = 0
                    while done == 0:
                        if i[0] + 1 != 8 and i[1] + 1 != 8:
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
                temp = [i[0],i[1]]

                if i[0] + 1 != 8 and i[1] - 1 != -1:
                    temp[0] += 1
                    temp[1] -= 1
                    done = 0
                    while done == 0:
                        if i[0] + 1 != 8 and i[1] - 1 != -1:
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
                temp = [i[0],i[1]]
                pos += [[i]+tpos]

            if T == 'wQ':
                done = 0
                temp = [i[0],i[1]]
                tpos = []
                #up right
                if i[0] - 1 != -1 and i[1] + 1 != 8:
                    temp[0] -= 1
                    temp[1] += 1
                    done = 0
                    while done == 0:
                        if i[0] - 1 != -1 and i[1] + 1 != 8:
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
                temp = [i[0],i[1]]

                if i[0] - 1 != -1 and i[1] - 1 != -1:
                    temp[0] -= 1
                    temp[1] -= 1
                    done = 0
                    while done == 0:
                        if i[0] - 1 != -1 and i[1] - 1 != -1:
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
                temp = [i[0],i[1]]

                if i[0] + 1 != 8 and i[1] + 1 != 8:
                    temp[0] += 1
                    temp[1] += 1
                    done = 0
                    while done == 0:
                        if i[0] + 1 != 8 and i[1] + 1 != 8:
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
                temp = [i[0],i[1]]

                if i[0] + 1 != 8 and i[1] - 1 != -1:
                    temp[0] += 1
                    temp[1] -= 1
                    done = 0
                    while done == 0:
                        if i[0] + 1 != 8 and i[1] - 1 != -1:
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
                temp = [i[0],i[1]]

                #up
                done = 0
                temp = [i[0],i[1]]
                tpos = []
                if i[0] - 1 != -1:
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

                temp = [i[0],i[1]]
                if i[0] + 1 != 8:
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
                
                temp = [i[0],i[1]]
                if i[1] - 1 != -1:
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

                temp = [i[0],i[1]]
                if i[1] + 1 != 8:
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

                pos += [[i]+tpos]

            if T == 'wP':
                tpos = []
                if i[0] == 6:
                    if board[4][i[1]] == '0 ':
                        tpos += [[4,i[1]]]
                if i[0] - 1 != -1:
                    if board[i[0]-1][i[1]] == '0 ':
                        tpos += [[i[0]-1,i[1]]]
                if i[0] - 1 != -1 and i[1] - 1 != -1:
                    if sideCheck(board[i[0]-1][i[1]-1],side):
                        tpos += [[i[0]-1,i[1]-1]]
                if i[0] - 1 != -1 and i[1] + 1 != 8:
                    if sideCheck(board[i[0]-1][i[1]+1],side):
                        tpos += [[i[0]-1,i[1]+1]]
                pos += [[i]+tpos]

    if side == 1:
        #find all the pieces
        for y in range(8):
            for x in range(8):
                T = board[y][x]
                if T == 'bK' or T == 'bQ' or T == 'bB' or T == 'bP' or T == 'bR' or T == 'bH':
                    uLoc = uLoc + [[y,x]]
        
        for i in uLoc:
            T = board[i[0]][i[1]]
            if T == 'bk':
                tpos = []
                if i[0] + 1 != 8:
                    if board[i[0]+1][i[1]] == '0 ' or sideCheck(board[i[0]+1][i[1]],side):
                        tpos += [[i[0]+1,i[1]]]
                if i[0] - 1 != -1:
                    if board[i[0]-1][i[1]] == '0 ' or sideCheck(board[i[0]-1][i[1]],side):
                        tpos += [[i[0]-1,i[1]]]
                if i[1] + 1 != 8:
                    if board[i[0]][i[1]+1] == '0 ' or sideCheck(board[i[0]][i[1]+1],side):
                        tpos += [[i[0],i[1]]+1]
                if i[1] - 1 != 8:
                    if board[i[0]-1][i[1]] == '0 ' or sideCheck(board[i[0]-1][i[1]],side):
                        tpos += [[i[0],i[1]]-1]
                
                if i[0] - 1 != -1 and i[1] + 1 != 8:
                    if board[i[0]-1][i[1]+1] == '0 ' or sideCheck(board[i[0]-1][i[1]+1],side):
                        tpos += [[i[0]-1,i[1]+1]]
                if i[0] - 1 != -1 and i[1] - 1 != -1:
                    if board[i[0]-1][i[1]-1] == '0 ' or sideCheck(board[i[0]-1][i[1]-1],side):
                        tpos += [[i[0]-1,i[1]-1]]
                if i[0] + 1 != 8 and i[1] + 1 != 8:
                    if board[i[0]+1][i[1]+1] == '0 ' or sideCheck(board[i[0]+1][i[1]+1],side):
                        tpos += [[i[0]+1,i[1]+1]]
                if i[0] + 1 != 8 and i[1] - 1 != -1:
                    if board[i[0]+1][i[1]-1] == '0 ' or sideCheck(board[i[0]+1][i[1]-1],side):
                        tpos += [[i[0]+1,i[1]-1]]
                pos += [[i]+tpos]
            if T == 'bR':
                #up
                done = 0
                temp = [i[0],i[1]]
                tpos = []
                if i[0] - 1 != -1:
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

                temp = [i[0],i[1]]
                if i[0] + 1 != 8:
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
                
                temp = [i[0],i[1]]
                if i[1] - 1 != -1:
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

                temp = [i[0],i[1]]
                if i[1] + 1 != 8:
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
                pos += [[i]+tpos]

            if T == 'bH':
                tpos = []
                if i[0] + 2 < 8 and i[1] + 1 < 8:
                    if board[i[0]+2][i[1]+1] == '0 ' or sideCheck(board[i[0]+2][i[1]+1],side):
                        tpos += [[i[0]+2,i[1]+1]]
                if i[0] + 2 < 8 and i[1] - 1 > -1:
                    if board[i[0]+2][i[1]-1] == '0 ' or sideCheck(board[i[0]+2][i[1]-1],side):
                        tpos += [[i[0]+2,i[1]-1]]

                if i[0] - 2 > -1 and i[1] + 1 < 8:
                    if board[i[0]-2][i[1]+1] == '0 ' or sideCheck(board[i[0]-2][i[1]+1],side):
                        tpos += [[i[0]-2,i[1]+1]]
                if i[0] - 2 > -1 and i[1] - 1 > -1:
                    if board[i[0]-2][i[1]-1] == '0 ' or sideCheck(board[i[0]-2][i[1]-1],side):
                        tpos += [[i[0]-2,i[1]-1]]

                if i[0] + 1 < 8 and i[1] + 2 < 8:
                    if board[i[0]+1][i[1]+2] == '0 ' or sideCheck(board[i[0]+1][i[1]+2],side):
                        tpos += [[i[0]+1,i[1]+2]]
                if i[0] + 1 < 8 and i[1] - 2 > -1:
                    if board[i[0]+1][i[1]-2] == '0 ' or sideCheck(board[i[0]+1][i[1]-2],side):
                        tpos += [[i[0]+1,i[1]-2]]
                
                if i[0] - 1 > -1 and i[1] + 2 < 8:
                    if board[i[0]-1][i[1]+2] == '0 ' or sideCheck(board[i[0]-1][i[1]+2],side):
                        tpos += [[i[0]-1,i[1]+2]]
                if i[0] - 1 > -1 and i[1] - 2 > -1:
                    if board[i[0]-1][i[1]-2] == '0 ' or sideCheck(board[i[0]-1][i[1]-2],side):
                        tpos += [[i[0]-1,i[1]-2]]
                pos += [[i]+tpos]

            if T == 'bB':
                done = 0
                temp = [i[0],i[1]]
                tpos = []
                #up right
                if i[0] - 1 != -1 and i[1] + 1 != 8:
                    temp[0] -= 1
                    temp[1] += 1
                    done = 0
                    while done == 0:
                        if i[0] - 1 != -1 and i[1] + 1 != 8:
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
                temp = [i[0],i[1]]

                if i[0] - 1 != -1 and i[1] - 1 != -1:
                    temp[0] -= 1
                    temp[1] -= 1
                    done = 0
                    while done == 0:
                        if i[0] - 1 != -1 and i[1] - 1 != -1:
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
                temp = [i[0],i[1]]

                if i[0] + 1 != 8 and i[1] + 1 != 8:
                    temp[0] += 1
                    temp[1] += 1
                    done = 0
                    while done == 0:
                        if i[0] + 1 != 8 and i[1] + 1 != 8:
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
                temp = [i[0],i[1]]

                if i[0] + 1 != 8 and i[1] - 1 != -1:
                    temp[0] += 1
                    temp[1] -= 1
                    done = 0
                    while done == 0:
                        if i[0] + 1 != 8 and i[1] - 1 != -1:
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
                temp = [i[0],i[1]]
                pos += [[i]+tpos]

            if T == 'bQ':
                done = 0
                temp = [i[0],i[1]]
                tpos = []
                #up right
                if i[0] - 1 != -1 and i[1] + 1 != 8:
                    temp[0] -= 1
                    temp[1] += 1
                    done = 0
                    while done == 0:
                        if i[0] - 1 != -1 and i[1] + 1 != 8:
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
                temp = [i[0],i[1]]

                if i[0] - 1 != -1 and i[1] - 1 != -1:
                    temp[0] -= 1
                    temp[1] -= 1
                    done = 0
                    while done == 0:
                        if i[0] - 1 != -1 and i[1] - 1 != -1:
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
                temp = [i[0],i[1]]

                if i[0] + 1 != 8 and i[1] + 1 != 8:
                    temp[0] += 1
                    temp[1] += 1
                    done = 0
                    while done == 0:
                        if i[0] + 1 != 8 and i[1] + 1 != 8:
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
                temp = [i[0],i[1]]

                if i[0] + 1 != 8 and i[1] - 1 != -1:
                    temp[0] += 1
                    temp[1] -= 1
                    done = 0
                    while done == 0:
                        if i[0] + 1 != 8 and i[1] - 1 != -1:
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
                temp = [i[0],i[1]]

                #up
                done = 0
                temp = [i[0],i[1]]
                tpos = []
                if i[0] - 1 != -1:
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

                temp = [i[0],i[1]]
                if i[0] + 1 != 8:
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
                
                temp = [i[0],i[1]]
                if i[1] - 1 != -1:
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

                temp = [i[0],i[1]]
                if i[1] + 1 != 8:
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

                pos += [[i]+tpos]

            if T == 'bP':
                tpos = []
                if i[0] == 1:
                    if board[3][i[1]] == '0 ':
                        tpos += [[3,i[1]]]
                if i[0] + 1 != -1:
                    if board[i[0]+1][i[1]] == '0 ':
                        tpos += [[i[0]+1,i[1]]]
                if i[0] + 1 != -1 and i[1] - 1 != -1:
                    if sideCheck(board[i[0]+1][i[1]-1],side):
                        tpos += [[i[0]+1,i[1]-1]]
                if i[0] + 1 != -1 and i[1] + 1 != 8:
                    if sideCheck(board[i[0]-1][i[1]+1],side):
                        tpos += [[i[0]+1,i[1]+1]]
                pos += [[i]+tpos]

    return pos
    
    

def moveChecker(SLr,SLc,FLr,FLc,side):
    #is the move there
    move = fullcheck(side)
    true  = 0
    for i in move:
        if i[0] == [SLr,SLc]:
            if [FLr,FLc] in i:
                true = 1
    if true == 1:
        return True
    else:
        return False
                

def checkmateFind():
    boardtmp = []
    for i in board:
        boardtmp += i
    if boardtmp.count('wK') != 1:
        return 1
    elif boardtmp.count('bK') !=1:
        return 2
    else:
        return 0

def checkmate():
    mate = checkmateFind
    if mate == 1:
        print('black wins')
        gameRun = 1
    if mate == 2:
        print('white wins')
        gameRun = 1

def ai(side):
    pos = fullcheck(side)

    attackM = [] #format [[sy,sx],[fy,fx]]
    nonattackM = []

    for i in pos: #compliling all moves
        if len(i[0]) > 1:
            temp = i.pop(0)
            for a in range(len(i)):
                T = board[i[a][0]][i[a][1]]
                if T  == '0 ':
                    nonattackM += [temp +i[a]]
                else:
                    attackM += [temp +i[a]]
    
    if len(attackM) > 0:
        return attackM[randint(0,len(attackM)-1)]
    else:
        return nonattackM[randint(0,len(nonattackM)-1)]
        



#Game start
print('Welcome to chess, this game will be a bit diffrent than most other games you have played')
print('to make a move you must input you starting cords starting at 0,0 from the top left and down to 7,7 at the bottom left')
print('to finish a move you have to also input the final cords for that piece, if it dosnt work you have to do it again')
print('to end the game you have to capture the opposing king, so regular chess after the checkmate')
print('have fun')
print('as most of my games choices between two words are answered with numbers so let us continue')
run = 0
while run == 0:
    numb = input('will this be a 1 or 2 player game: ')
    numb = int(numb)
    if numb == 1:
        #needs an ai
        side = int(input('what side will you be on 0 white 1 black: '))
        gameRun = 0 
        turn = 0
        printb()
        while gameRun == 0:
            while (turn == 0):
                print('white turn')
                if side == 0:
                    SLr = int(input('start row: '))
                    SLc = int(input('start col: '))
                    FLr = int(input('end row: '))
                    FLc = int(input('end col: '))
                    move = moveChecker(SLr,SLc,FLr,FLc,side)
                    if move:
                        temp = board[SLr][SLc]
                        board[SLr][SLc] = '0 '
                        board[FLr][FLc] = temp
                        turn = 1
                    else:
                        temp ='0 '
                else:
                    move = ai(0)
                    move2 = moveChecker(move[0],move[1],move[2],move[3],0)
                    if move2:
                        temp = board[move[0]][move[1]]
                        board[move[0]][move[1]] = '0 '
                        board[move[2]][move[3]] = temp
                        turn = 1
                    else:
                        temp ='0 '
            printb()
            checkmateFind() 
            while (turn == 1):
                if side == 1:
                    print('black turn')
                    SLr = int(input('start row: '))
                    SLc = int(input('start col: '))
                    FLr = int(input('end row: '))
                    FLc = int(input('end col: '))
                    move = moveChecker(SLr,SLc,FLr,FLc,side)
                    if move:
                        temp = board[SLr][SLc]
                        board[SLr][SLc] = '0 '
                        board[FLr][FLc] = temp
                        turn = 0
                    else:
                        temp ='0 '
                else:
                    print('black turn')
                    move = ai(1)
                    move2 = moveChecker(move[0],move[1],move[2],move[3],1)
                    if move2:
                        temp = board[move[0]][move[1]]
                        board[move[0]][move[1]] = '0 '
                        board[move[2]][move[3]] = temp
                        turn = 0
                    else:
                        temp ='0 '
                checkmateFind() 
                printb()

    if numb == 2:
        print('chose who goes first on your end and we can get started')
        gameRun = 0 
        turn = 0
        printb()
        while gameRun == 0:
            while (turn == 0):
                print('white turn')
                side = 0
                SLr = int(input('start row: '))
                SLc = int(input('start col: '))
                FLr = int(input('end row: '))
                FLc = int(input('end col: '))
                move = moveChecker(SLr,SLc,FLr,FLc,side)
                if move:
                    temp = board[SLr][SLc]
                    board[SLr][SLc] = '0 '
                    board[FLr][FLc] = temp
                    turn = 1
                else:
                    temp ='0 '
            printb()
            checkmate()
            while(turn == 1 and gameRun != 1):
                print('black turn')
                side = 1
                SLr = int(input('start row: '))
                SLc = int(input('start col: '))
                FLr = int(input('end row: '))
                FLc = int(input('end col: '))
                move = moveChecker(SLr,SLc,FLr,FLc,side)
                if move:
                    temp = board[SLr][SLc]
                    board[SLr][SLc] = '0 '
                    board[FLr][FLc] = temp
                    turn = 0
                else:
                    temp ='0 '
            printb()
            checkmate()


    else:
        print('your stupid')
        run = 1 
        