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
    if side == 0: #white 
        T = board[temp[0]][temp[1]]
        if (T == 'bP' or T == 'bR' or T == 'bH' or T == 'bK' or T == 'bQ' or T == 'bB'):
            pos = pos + [temp]
    elif  side == 1: #black
        if (T == 'wP' or T == 'wR' or T == 'wH' or T == 'wK' or T == 'wQ' or T == 'wB'):
            pos = pos + [temp]
    return temp


def crossCheck(SLr,SLc,FLr,FLc,side):
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
                    temp[1] += 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: #something is in the way
                            temp = sideCheck(pos,side,temp)
                            done = 1
                elif i == 1: #up
                    temp[1] -= 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                elif i == 2: #right
                    temp[0] += 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                elif i == 3: #left
                    temp[0] -= 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
    elif (piece == 'bB' or piece == 'wB'): #bishop
        for i in range(4):
            done = 0
            while (done == 0):
                temp = [SLr,SLc]
                if i == 0: #down right
                    temp[1] += 1
                    temp[0] += 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                if i == 1: #down left
                    temp[1] -= 1
                    temp[0] += 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                if i == 2: #up left
                    temp[1] -= 1
                    temp[0] -= 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                if i == 3: #up right
                    temp[1] += 1
                    temp[0] -= 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
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

                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + temp
                        else: 
                            temp = sideCheck(pos,side,temp)
                if i == 1: #down
                    temp[0] += 2
                    if a == 0: #left
                        temp[1] -= 1
                    else:
                        temp[1] += 1

                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                if i == 2: #right
                    temp[1] += 2
                    if a == 0: #up
                        temp[0] -= 1
                    else:
                        temp[0] += 1

                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                if i == 3: #left
                    temp[1] -= 2
                    if a == 0: #up
                        temp[0] -= 1
                    else:
                        temp[0] += 1

                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                print(temp,'temp')
                print(pos,'pos')
    elif (piece == 'bQ' or piece == 'wQ'): #queen. the rook and bishop combined
        for i in range(7):
            done = 0
            while (done == 0):
                temp = [SLr,SLc]
                if i == 0: #down right
                    temp[0] += 1
                    temp[1] += 1

                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                if i == 1: #down left
                    temp[0] -= 1
                    temp[1] += 1

                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                if i == 2: #up left
                    temp[0] -= 1
                    temp[1] -= 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                if i == 3: #up right
                    temp[0] += 1
                    temp[1] -= 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                if i == 4: #down
                    temp[1] += 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: #something is in the way
                            temp = sideCheck(pos,side,temp)
                            done = 1
                elif i == 5: #up
                    temp[1] -= 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
                elif i == 6: #right
                    temp[0] += 1
                    if (board[temp[0]][temp[1]] == '0 '):
                        pos = pos + [temp]
                    else: 
                        temp = sideCheck(pos,side,temp)
                        done = 1
                elif i == 7: #left
                    temp[0] -= 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if (board[temp[0]][temp[1]] == '0 '):
                            pos = pos + [temp]
                        else: 
                            temp = sideCheck(pos,side,temp)
                            done = 1
    elif (piece == 'bK' or piece == 'wK'): #king 
        for i in range(2):
            for a in range(2): #i up and down a is left and right
                temp = [SLr,SLc]
                if i == 0: #non moving
                    if a == 1: #up
                        temp[0] -= 1
                        if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                    elif a == 2: #down
                        temp[0] += 1
                        if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                if i == 1: #left
                    temp[1] -= 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if a == 9: #nonmoving
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                    elif a == 1: #up
                        temp[0] -= 1
                        if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                    elif a == 2: #down
                        temp[0] += 1
                        if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                if i == 2: #right
                    temp[1] += 1
                    if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                        if a == 9: #nonmoving
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                    elif a == 1: #up
                        temp[0] -= 1
                        if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
                    elif a == 2: #down
                        temp[0] += 1
                        if (temp[0] >= 0 and temp[0] <= 8) and (temp[1] >= 0 and temp[1] <= 8):
                            if (board[temp[0]][temp[1]] == '0 '):
                                pos = pos + [temp]
                            else: 
                                temp = sideCheck(pos,side,temp)
    if (piece == 'bP' or piece == 'wP'):#pawn
        #forword 1 (up for white down for black)
        if side == 0: #white
            if SLr == 6:
                if board[5][SLc] == '0 ':
                    pos += [5,SLc]
                if board[4][SLc] == '0 ':
                    pos += [4,SLc]
            else:
                if board[SLr-1][SLc] == '0 ':
                    pos += [SLr-1,SLc]
        if side == 1: #black
            if SLr == 1:
                if board[3][SLc] == '0 ':
                    pos += [4,SLc]
                if board[2][SLc] == '0 ':
                    pos += [3,SLc]
            else:
                if board[SLr-1][SLc] == '0 ':
                    pos += [SLr-1,SLc]
    
        #up left/right
        if side == 0:
            if board[SLr-1][SLc+1] != '0 ':
                T = board[SLr-1][SLc+1]
                if (T == 'bP' or T == 'bR' or T == 'bH' or T == 'bK' or T == 'bQ' or T == 'bB'):
                    pos += [SLr-1,SLc+1]
            if board[SLr-1][SLc-1] != '0 ':
                T = board[SLr-1][SLc-1]
                if (T == 'bP' or T == 'bR' or T == 'bH' or T == 'bK' or T == 'bQ' or T == 'bB'):
                    pos += [SLr-1,SLc-1]
        if side == 1:
            if board[SLr+1][SLc+1] != '0 ':
                T = board[SLr+1][SLc+1]
                if (T == 'wP' or T == 'wR' or T == 'wH' or T == 'wK' or T == 'wQ' or T == 'wB'):
                    pos += [SLr+1,SLc+1]
            if board[SLr-1][SLc-1] != '0 ':
                T = board[SLr+1][SLc-1]
                if (T == 'wP' or T == 'wR' or T == 'wH' or T == 'wK' or T == 'wQ' or T == 'wB'):
                    pos += [SLr+1,SLc-1]


    

def moveChecker(SLr,SLc,FLr,FLc,side):
    #is the move there
    move = crossCheck(SLr,SLc,FLr,FLc,side)
    if ([FLr,FLc] in move):
        return True
    else: 
        return False

    


#Game start
print('Welcome to chess, this game will be a bit diffrent than most other games you have played')
print('to make a move you must input you starting cords starting at 0,0 from the top left and down to 7,7 at the bottom left')
print('to finish a move you have to also input the final cords for that piece, if it dosnt work you have to do it again')
print('have fun')
print('as most of my games choices between two words are answered with numbers so let us continue')
run = 0
while run == 0:
    numb = input('will this be a 1 or 2 player game: ')
    numb = int(numb)
    if numb == 1:
        #needs an ai
        side = int(input('what side will you be on 0 white 1 black: '))
    if numb == 2:
        print('chose who goes first on your end and we can get started')
        gameRun = 0 
        turn = 0
        while gameRun == 0:
            printb()
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
            while(turn == 1):
                print('black turn')
                side = 1
                SLr = int(input('start row: '))
                SLc = int(input('start col: '))
                FLr = int(input('end row: '))
                FLc = int(input('end col: '))


    else:
        print('your stupid')
        run = 1 
        