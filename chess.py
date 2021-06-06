#the goal is to create chess or something like chess.
#to  do list
#make a board done
#put pieces on board done
#make pieces move the way the have to
#have the player control one side.(white or black)
#something in the way checker
#how the ai works
    #check the current board 
    #make a move

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

def movePiece(SLr,SLc,FLr,FLc): #SL - start location FL -final location. dose not check side of player
    #pawns
    if (board[SLr][SLc] == 'bP'): #check if FL is valid
        if ((SLr + 1 == FLr) and (SLc == FLc)):
            return [1,1] #valid non attacking / pawn
        elif ((SLr == 2 and SLr + 2 == FLr) and (SLc == FLc)): #specal first move
            return [1,1] #valid non attacking / pawn
        elif ((SLr + 1 == FLr) and (SLc + 1 == FLc or SLc - 1 == FLc)):
            return [2,1] #valid attacking move /pawn
        else:
            return [0, 1] #not valid move
    if (board[SLr][SLc] == 'wP'): #check if FL is valid
        if ((SLr - 1 == FLr) and (SLc == FLc)):
            return [1,1] #valid non attacking / cant destroy anything
        elif ((SLr == 5 and SLr - 2 == FLr) and (SLc == FLc)):
            return [1,1] #valid non attacking / cant destroy anything
        elif ((SLr - 1 == FLr) and (SLc - 1 == FLc or SLc + 1 == FLc)):
            return [2,1] #valid attacking move
        else:
            return [0, 1] #not valid move
    #rooks
    if (board[SLr][SLc] == 'bR'): #check if FL is valid
        if (SLr == FLr != SLc == FLc):
            return [3,2] #valid move attacking or not
        else:
            return [0,2] #not valid move
    if (board[SLr][SLc] == 'wR'): #check if FL is valid
        if (SLr == FLr != SLc == FLc):
            return [0,2] #valid move attacking or not
        else:
            return [0,2] #not valid move
    #bishops
    if (board[SLr][SLc] == 'bB'): #check if FL is valid
        if (SLr - FLr == SLc - FLc):
            return [3,3]#valid move attacking or not
        else:
            return [0,3] #not valid move
    if (board[SLr][SLc] == 'wB'): #check if FL is valid
        if (SLr - FLr == SLc - FLc):
            return [3,3] #valid move attacking or not
        else:
            return [0,3] #not valid move
    #knights
    #move in a direction 2 than the other 1
    if (board[SLr][SLc] == 'bH'):
        if((SLc + 2 == FLc or SLc - 2 == FLc) and (SLr + 1 == FLr or SLr - 1 == FLr)): #up and down 4
            return [3,4]
        if ((SLr + 2 == FLr or SLr - 2 == FLr) and (SLc + 1 == FLc or SLc - 1 == FLc)): #left and right 4
            return [3,4]
        else:
            return [0,4]
    if (board[SLr][SLc] == 'wH'):
        if((SLc + 2 == FLc or SLc - 2 == FLc) and (SLr + 1 == FLr or SLr - 1 == FLr)): #up and down 4
            return [3,4]
        if ((SLr + 2 == FLr or SLr - 2 == FLr) and (SLc + 1 == FLc or SLc - 1 == FLc)): #left and right 4
            return [3,4]
        else:
            return [0,4]
    #queen
    if (board[SLr][SLc] == 'bQ'):
        if (SLr == FLr != SLc == FLc):
            return [3,5] #valid move attacking or not
        if (SLr - FLr == SLc - FLc):
            return [3,5] #valid move attacking or not
        else:
            return [0,5]
    if (board[SLr][SLc] == 'wQ'):
        if (SLr == FLr != SLc == FLc):
            return [3,5] #valid move attacking or not
        if (SLr - FLr == SLc - FLc):
            return [3,5] #valid move attacking or not
        else:
            return [0,5]
    #king
    if (board[SLr][SLc] == 'bK'):
        if (((SLr + 1 == FLr or SLr - 1 == FLr) or SLr == FLr) or ((SLc + 1 == FLc or SLc -1 == FLc) or SLc == FLc)):
            return [3,6]
        else:
            return [0,6]
    if (board[SLr][SLc] == 'wK'):
        if (((SLr + 1 == FLr or SLr - 1 == FLr) or SLr == FLr) or ((SLc + 1 == FLc or SLc -1 == FLc) or SLc == FLc)):
            return [3,6]
        else:
            return [0,6]
    if (board[SLr][SLc] == '0'):
        return [0,0]

def crossCheck(SLr,SLc,FLr,FLc):
    #the goal is to draw a line and see if the 
    piece = movePiece(SLr,SLc,FLr,FLc) # first number is if its valid second is what piece

printb()