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

def sideCheck(pos,side,temp):
    T = board[temp[0]][temp[1]]
    if side == 0: #white 
        if (T == 'bP' or T == 'bR' or T == 'bH' or T == 'bK' or T == 'bQ' or T == 'bB'):
            pos = pos + [temp]
    elif  side == 1: #black
        if (T == 'wP' or T == 'wR' or T == 'wH' or T == 'wK' or T == 'wQ' or T == 'wB'):
            pos = pos + [temp]
    return temp


def crossCheck(SLr,SLc,side):
    #the goal is to draw a line and see if the 
    #check is valid first
    done = 0 #stops while loops when 1
    pos = [] #list of all xy cords
    piece = board[SLr][SLc]
    if (piece == 'bR' or piece == 'wR'): #rook
        for i in range(4):
            done = 0
            while (done == 0): # loop through all cords in one direction
                temp = [SLr,SLc]
                if i == 0: #down
                    temp[0] += 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: #something is in the way
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                elif i == 1: #up
                    temp[0] -= 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                elif i == 2: #right
                    temp[1] += 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                elif i == 3: #left
                    temp[1] -= 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                    done = 1
    elif (piece == 'bB' or piece == 'wB'): #bishop
        for i in range(4):
            done = 0
            while (done == 0):
                temp = [SLr,SLc]
                if i == 0: #down right
                    temp[1] += 1
                    temp[0] += 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                if i == 1: #down left
                    temp[1] -= 1
                    temp[0] += 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                if i == 2: #up left
                    temp[1] -= 1
                    temp[0] -= 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                if i == 3: #up right
                    temp[1] += 1
                    temp[0] -= 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
    elif (piece == 'bH' or piece == 'wH'): #knight specal
        for i in range(4):
            for a in range(1): #i is main direction a is side direction
                temp = [SLr,SLc]
                if i == 0: #up
                    temp[0] -= 2
                    if a == 0: #left
                        temp[1] -= 1
                    else:
                        temp[1] += 1

                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + temp
                        else: 
                            temp = sideCheck(pos,side,temp)
                    else:
                        done = 1
                if i == 1: #down
                    temp[0] += 2
                    if a == 0: #left
                        temp[1] -= 1
                    else:
                        temp[1] += 1

                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                    else:
                        done = 1
                if i == 2: #right
                    temp[1] += 2
                    if a == 0: #up
                        temp[0] -= 1
                    else:
                        temp[0] += 1

                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                    else:
                        done = 1
                if i == 3: #left
                    temp[1] -= 2
                    if a == 0: #up
                        temp[0] -= 1
                    else:
                        temp[0] += 1

                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                    else:
                        done = 1
    elif (piece == 'bQ' or piece == 'wQ'): #queen. the rook and bishop combined
        for i in range(7):
            done = 0
            while (done == 0):
                temp = [SLr,SLc]
                if i == 0: #down right
                    temp[0] += 1
                    temp[1] += 1

                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                if i == 1: #down left
                    temp[0] -= 1
                    temp[1] += 1

                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                if i == 2: #up left
                    temp[0] -= 1
                    temp[1] -= 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                if i == 3: #up right
                    temp[0] += 1
                    temp[1] -= 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                if i == 4: #down
                    temp[1] += 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: #something is in the way
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                elif i == 5: #up
                    temp[1] -= 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                elif i == 6: #right
                    temp[0] += 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
                elif i == 7: #left
                    temp[0] -= 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                    else:
                        done = 1
    elif (piece == 'bK' or piece == 'wK'): #king 
        for i in range(2):
            for a in range(2): #i up and down a is left and right
                temp = [SLr,SLc]
                if i == 0: #non moving
                    if a == 1: #up
                        temp[0] -= 1
                        if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                        else:
                            done = 1
                    elif a == 2: #down
                        temp[0] += 1
                        if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                        else:
                            done = 1
                if i == 1: #left
                    temp[1] -= 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if a == 9: #nonmoving
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                        else:
                            done = 1
                    elif a == 1: #up
                        temp[0] -= 1
                        if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                        else:
                            done = 1
                    elif a == 2: #down
                        temp[0] += 1
                        if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                        else:
                            done = 1
                if i == 2: #right
                    temp[1] += 1
                    if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                        if a == 9: #nonmoving
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                        else:
                            done = 1
                    elif a == 1: #up
                        temp[0] -= 1
                        if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                        else:
                            done = 1
                    elif a == 2: #down
                        temp[0] += 1
                        if (temp[0] >= 0 and temp[0] < 8) and (temp[1] >= 0 and temp[1] < 8):
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                        else:
                            done = 1
    if (piece == 'bP' or piece == 'wP'):#pawn
        #forword 1 (up for white down for black)
        if side == 0: #white
            if SLr == 6:
                if board[5][SLc] == '0 ':
                    pos = pos + [5,SLc]
                if board[4][SLc] == '0 ':
                    pos = pos + [4,SLc]
            else:
                if board[SLr-1][SLc] == '0 ':
                    pos = pos + [SLr-1,SLc]
        if side == 1: #black
            if SLr == 1:
                if board[3][SLc] == '0 ':
                    pos = pos + [4,SLc]
                if board[2][SLc] == '0 ':
                    pos = pos + [3,SLc]
            else:
                if board[SLr-1][SLc] == '0 ':
                    pos = pos + [SLr-1,SLc]
    
        #up left/right
        if side == 0:
            if SLc != 7 and SLr != 0 and SLc != 0:
                if board[SLr-1][SLc+1] != '0 ':
                    T = board[SLr-1][SLc+1]
                    if (T == 'bP' or T == 'bR' or T == 'bH' or T == 'bK' or T == 'bQ' or T == 'bB'):
                        pos = pos + [SLr-1,SLc+1]
            if SLc != 7 and SLr != 0 and SLc != 0:
                if board[SLr-1][SLc-1] != '0 ':
                    T = board[SLr-1][SLc-1]
                    if (T == 'bP' or T == 'bR' or T == 'bH' or T == 'bK' or T == 'bQ' or T == 'bB'):
                        pos = pos + [SLr-1,SLc-1]
        if side == 1:
            if SLc != 7 and SLr != 0 and SLc != 0:
                if board[SLr+1][SLc+1] != '0 ':
                    T = board[SLr+1][SLc+1]
                    if (T == 'wP' or T == 'wR' or T == 'wH' or T == 'wK' or T == 'wQ' or T == 'wB'):
                        pos = pos + [SLr+1,SLc+1]
            if SLc != 7 and SLr != 0 and SLc != 0:
                if board[SLr-1][SLc-1] != '0 ':
                    T = board[SLr+1][SLc-1]
                    if (T == 'wP' or T == 'wR' or T == 'wH' or T == 'wK' or T == 'wQ' or T == 'wB'):
                        pos = pos + [SLr+1,SLc-1]
    
    if len(pos) != 0:
        postemp = []
        for i in range(int(len(pos)/2)):
            postemp = postemp + [[pos[i*2],pos[i*2+1]]]
        pos = postemp

    return pos

    

def moveChecker(SLr,SLc,FLr,FLc,side):
    #is the move there
    move = crossCheck(SLr,SLc,side)
    if ([FLr,FLc] in move):
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
    #get a list of all pieces and there locations
    #number of pieces
    #location of each piece
    boardtmp = []
    for i in board:
        boardtmp += i

    if side == 0:
        units = boardtmp.count('wK') + boardtmp.count('wP') + boardtmp.count('wB') + boardtmp.count('wR') + boardtmp.count('wQ') + + boardtmp.count('wH') 
        uids = []
        for i in range(units):
            found = 0
            num = 0
            while found == 0:
                if boardtmp[num] == 'wK' or boardtmp[num] == 'wP' or boardtmp[num] == 'wB' or boardtmp[num] == 'wQ' or boardtmp[num] == 'wR' or boardtmp[num] == 'wH':
                    uids += [num]
                    found = 1
                    boardtmp[num] = '0'
                else:
                    num += 1 
                if num > 63:
                    found = 1
        #take the list of 0 - 63 and make it 8 by 8
        ucords = []
        for i in uids:
            ucords = ucords + [[int(i/8),int(i%8)]]
        allpos = []
        for i in ucords:
            allpos = allpos + [[i] + crossCheck(int(i[0]),int(i[1]),0)]
        #check for attacking moves
        attackmoves = []
        nonattackmoves = []
        for i in range(len(allpos)):
            #starting pos then all other pos
            for a in allpos[i]:
                if len(allpos[i]) > 1:
                    if board[a[0]][a[1]] == '0':
                        nonattackmoves = nonattackmoves + [[allpos[0]]+a]
                    else:
                        attackmoves = attackmoves + [[allpos[0]]+a]

        if len(attackmoves) != 0:
            return attackmoves[randint(0,len(attackmoves)-1)]
        else:
            return nonattackmoves[randint(0,len(nonattackmoves)-1)]


    if side == 1:
        units = boardtmp.count('bK') + boardtmp.count('bP') + boardtmp.count('bB') + boardtmp.count('bR') + boardtmp.count('bQ') + + boardtmp.count('bH') 
        uids = []
        for i in range(units):
            found = 0
            num = 0
            while found == 0:
                if boardtmp[num] == 'bK' or boardtmp[num] == 'bP' or boardtmp[num] == 'bB' or boardtmp[num] == 'bQ' or boardtmp[num] == 'bR' or boardtmp[num] == 'bH':
                    uids += [num]
                    found = 1
                    boardtmp[num] = '0'
                else:
                    num += 1 
                if num > 63:
                    found = 1
        #take the list of 0 - 63 and make it 8 by 8
        ucords = []
        for i in uids:
            ucords = ucords + [[int(i/8),int(i%8)]]
        allpos = []
        for i in ucords:
            allpos = allpos + [[i] + crossCheck(int(i[0]),int(i[1]),1)]
        #check for attacking moves
        attackmoves = []
        nonattackmoves = []
        for i in range(len(allpos)):
            #starting pos then all other pos
            for a in allpos[i]:
                if len(allpos[i]) > 1:
                    if board[a[0]][a[1]] == '0':
                        nonattackmoves = nonattackmoves + [[allpos[0]]+a]
                    else:
                        attackmoves = attackmoves + [[allpos[0]]+a]

        if len(attackmoves) != 0:
            return attackmoves[randint(0,len(attackmoves)-1)]
        else:
            return nonattackmoves[randint(0,len(nonattackmoves)-1)]
        



#Game start
print('Welcome to chess, this game will be a bit diffrent than most other games you have played')
print('to make a move you must input you starting cords starting at 0,0 from the top left and down to 7,7 at the bottom left')
print('to finish a move you have to also input the final cords for that piece, if it dosnt work you have to do it again')
print('to end the game you have to capture the opposing king, so regular chess after the checkmate')
print('have fun')
print('as most of my games choices between two words are answered with numbers so let us continue')
run = 0
while run == 0:
    numb = input('will this be a 1 or 2 player game: "WARNING THE AI DOSE NOT WORK RN. ITS BEING FIXED CHOOSE 2 PLAYER')
    numb = int(numb)
    if numb == 1:
        #needs an ai
        side = int(input('what side will you be on 0 white 1 black: '))
        gameRun = 0 
        turn = 0
        printb()
        while gameRun == 0:
            while (turn == 0):
                if side == 0:
                    print('white turn')
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
                    print('white turn')
                    move = ai(0)
                    move2 = moveChecker(move[0][0],move[0][1],move[1][0],move[1][1],0)
                    if move2:
                        temp = board[SLr][SLc]
                        board[SLr][SLc] = '0 '
                        board[FLr][FLc] = temp
                        turn = 1
                    else:
                        temp ='0 '
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
                        turn = 1
                    else:
                        temp ='0 '
                else:
                    print('black turn')
                    move = ai(1)
                    move2 = moveChecker(move[0][0],move[0][1],move[1][0],move[1][1],1)
                    if move2:
                        temp = board[SLr][SLc]
                        board[SLr][SLc] = '0 '
                        board[FLr][FLc] = temp
                        turn = 1
                    else:
                        temp ='0 '

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
                    turn = 1
                else:
                    temp ='0 '
            printb()
            checkmate()


    else:
        print('your stupid')
        run = 1 
        