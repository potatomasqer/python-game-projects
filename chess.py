#chess attempt #3
#build a system where i can test each piece individualy
#incorperate algebraic notation
#pieces


board = []

def printB(B):
    print()
    for i in B: #print the board
        print(i)
    print()

def makeNewB():
    #row by row
    board = [
        ['|_|','|A| ','|B| ','|C| ','|D| ','|E| ','|F| ','|G| ','|H| '],
        ['|8|','|bR|','|bN|','|bB|','|bQ|','|bK|','|bB|','|bN|','|bR|'],
        ['|7|','|bP|','|bP|','|bP|','|bP|','|bP|','|bP|','|bP|','|bP|'],
        ['|6|','|__|','|__|','|__|','|__|','|__|','|__|','|__|','|__|'],
        ['|5|','|__|','|__|','|__|','|__|','|__|','|__|','|__|','|__|'],
        ['|4|','|__|','|__|','|__|','|__|','|__|','|__|','|__|','|__|'],
        ['|3|','|__|','|__|','|__|','|__|','|__|','|__|','|__|','|__|'],
        ['|2|','|wP|','|wP|','|wP|','|wP|','|wP|','|wP|','|wP|','|wP|'],
        ['|1|','|wR|','|wN|','|wB|','|wQ|','|wK|','|wB|','|wN|','|wR|']]
    return board

def makeTestB():
    board = [
        ['|_|','|A| ','|B| ','|C| ','|D| ','|E| ','|F| ','|G| ','|H| '],
        ['|8|','|__|','|__|','|__|','|wK|','|bP|','|bP|','|__|','|__|'],
        ['|7|','|wP|','|__|','|__|','|wP|','|bP|','|bP|','|wP|','|__|'],
        ['|6|','|__|','|wP|','|__|','|__|','|bP|','|bP|','|__|','|__|'],
        ['|5|','|__|','|wN|','|__|','|wR|','|bP|','|bP|','|wB|','|__|'],
        ['|4|','|__|','|__|','|__|','|__|','|bP|','|bP|','|__|','|__|'],
        ['|3|','|__|','|wQ|','|__|','|__|','|bP|','|bP|','|__|','|__|'],
        ['|2|','|__|','|__|','|__|','|__|','|bP|','|bP|','|__|','|__|'],
        ['|1|','|__|','|__|','|__|','|__|','|bP|','|bP|','|__|','|__|']]
    return board

def sideCheck(side,L,mark,piece):
    if side == 1:
        if piece == '|bP|' or piece == '|bR|' or piece == '|bN|' or piece == '|bB|' or piece == '|bQ|' or piece == '|bk|':
            mark += [L]
    if side == 2:
        if piece == '|wP|' or piece == '|wR|' or piece == '|wN|' or piece == '|wB|' or piece == '|wQ|' or piece == '|wk|':
            mark += [L]
    return mark
def directionalCheck(L,Xmod,Ymod,mark,side): #beams in one direction for moves
    if L[0]+Xmod < 9 and L[1]+Ymod < 9 and  L[0]+Xmod > 0 and L[1]+Ymod > 0: #check for bounds
        if board[L[1]+Ymod][L[0]+Xmod] == '|__|': #check if blank
            mark += [[L[0]+Xmod,L[1]+Ymod]]
            directionalCheck([L[0]+Xmod,L[1]+Ymod],Xmod,Ymod,mark,side) #mark and repeat
        else: mark = sideCheck(side,[L[0]+Xmod,L[1]+Ymod],mark,board[L[1]+Ymod][L[0]+Xmod]) #check if on the same side
    return mark
def bishopCheck(L,side):
    mark = directionalCheck(L,1,1,[],side)
    mark += directionalCheck(L,-1,1,mark,side)
    mark += directionalCheck(L,-1,-1,mark,side)
    mark += directionalCheck(L,1,-1,mark,side)
    return mark
def rookCheck(L,side):
    mark = directionalCheck(L,0,1,[],side)
    mark += directionalCheck(L,0,-1,mark,side)
    mark += directionalCheck(L,1,0,mark,side)
    mark += directionalCheck(L,-1,0,mark,side)
    return mark
def queenCheck(L,side):
    mark = bishopCheck(L,side)
    mark += rookCheck(L,side)
    return mark
def knightCheck(L,side):
    allPos = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[1,2],[1,-2]] # a list of all moves that a knight can do
    mark = []
    for i in allPos:
        if (L[0]+i[0] > 0 and L[0]+i[0] < 9) and (L[1]+i[1] > 0 and L[1]+i[1] < 9):
            if board[L[1]+i[1]][L[0]+i[0]] == '|__|':
                mark += [[L[0]+i[0],L[1]+i[1]]]
            else:
                mark = sideCheck(side,[L[0]+i[0],L[1]+i[1]],mark,board[L[1]+i[1]][L[0]+i[0]])
    return mark
def kingCheck(L,side):
    allPos = [[1,1],[1,-1],[1,0],[0,1],[0,-1],[-1,1],[-1,-1],[-1,0]] # a list of all moves that the king can do
    mark = []
    for i in allPos:
        if (L[0]+i[0] > 0 and L[0]+i[0] < 9) and (L[1]+i[1] > 0 and L[1]+i[1] < 9):
            if board[L[1]+i[1]][L[0]+i[0]] == '|__|':
                mark += [[L[0]+i[0],L[1]+i[1]]]
            else:
                mark = sideCheck(side,[L[0]+i[0],L[1]+i[1]],mark,board[L[1]+i[1]][L[0]+i[0]])
    return mark
def pawnCheck(L,side): #no ep. just no
    mark = []
    if side == 1: # sides are very importent for pawns
        if L[1] == 2:
            if board[4][L[0]] == '|__|':
                mark += [[L[0],4]]
        if L[1]+1 < 9: #not at edge and not blocked
            t = board[L[1]+1][L[0]] 
            if t == '|__|':
                mark += [[L[0],L[1]+1]]
        if L[0] > 1:
            mark = sideCheck(side,[L[0]-1,L[1]+1],mark,board[L[1]+1][L[0]-1])
        if L[0] < 8:
            mark = sideCheck(side,[L[0]+1,L[1]+1],mark,board[L[1]+1][L[0]+1])
    if side == 2: # sides are very importent for pawns
        if L[1] == 7:
            if board[5][L[0]] == '|__|':
                mark += [[L[0],5]]
        if L[1]-1 > 0: #not at edge and not blocked
            t = board[L[1]-1][L[0]] 
            if t == '|__|':
                mark += [[L[0],L[1]-1]]
        if L[0] > 1:
            mark = sideCheck(side,[L[0]-1,L[1]-1],mark,board[L[1]-1][L[0]-1])
        if L[0] < 8:
            mark = sideCheck(side,[L[0]+1,L[1]-1],mark,board[L[1]-1][L[0]+1])
    return mark




def moveCheck(piece,L,side): #location is [x,y]
    legalmoves = []
    if piece == '|wB|' or piece == '|bB|':
        legalmoves = bishopCheck(L,side)
    if piece == '|wR|' or piece == '|bR|':
        legalmoves = rookCheck(L,side)
    if piece == '|wQ|' or piece == '|bQ|':
        legalmoves = queenCheck(L,side)
    if piece == '|wN|' or piece == '|bN|':
        legalmoves = knightCheck(L,side)
    if piece == '|wK|' or piece == '|bK|':
        legalmoves = kingCheck(L,side)
    if piece == '|wP|' or piece == '|bP|':
        legalmoves = pawnCheck(L,side)



    #print('legal moves',legalmoves) #debug stuff
    return legalmoves


def letertoNum(l):
    if l == 'A' or l == 'a':
        return 1
    if l == 'B' or l == 'b':
        return 2
    if l == 'C' or l == 'c':
        return 3
    if l == 'D' or l == 'd':
        return 4
    if l == 'E' or l == 'e':
        return 5
    if l == 'F' or l == 'f':
        return 6
    if l == 'G' or l == 'g':
        return 7
    if l == 'H' or l == 'h':
        return 8
    #now tranlating the numbers. just trust me here we have to do this
    if l == '1':
        return 8
    if l == '2':
        return 7
    if l == '3':
        return 6
    if l == '4':
        return 5
    if l == '5':
        return 4
    if l == '6':
        return 3
    if l == '7':
        return 2
    if l == '8':
        return 1


def Translator(move:str):
    #translates chess notation into piece movement
    p1 = '' 
    p2 = ''
    part = 1
    for i in move: #each letter
        #location of piece to desired location
        if part == 1:
            p1 += i
        else:
            p2 += i

        try:
            int(i) #check if i is a number
            part = 2 #if it is things change
        except:
            str(i) #filler. cant remove

    startx = letertoNum(p1[0])
    starty = letertoNum(p1[1])
    endx = letertoNum(p2[0])
    endy = letertoNum(p2[1])
    return [[startx,starty],[endx,endy]]

def moveMaker(move,side,board):
    cords = Translator(move) #words to cords
    start = cords[0]
    end = cords[1]
    Spiece = board[start[1]][start[0]]
    legal = []
    if side == 1: #white
        if Spiece == '|wP|' or Spiece == '|wR|' or Spiece == '|wN|' or Spiece == '|wB|' or Spiece == '|wQ|' or Spiece == '|wK|': #confirm
            legal = moveCheck(Spiece,start,side)
    if side == 2: #black
        if Spiece == '|bP|' or Spiece == '|bR|' or Spiece == '|bN|' or Spiece == '|bB|' or Spiece == '|bQ|' or Spiece == '|bk|': #confirm
            legal = moveCheck(Spiece,start,side)
        

    try:
        legal.index(end)
        #valid move
        board[start[1]][start[0]] = '|__|'
        board[end[1]][end[0]] = Spiece
    except:
        print('illegal move')
    
    return board
        

GameRun = True
print('chess lol')
p = input('white or black: ')
mode = 0
for i in p: #spliting up a string
    if i == 't':
        mode = 3
    if i == 'w' or i == 'W':
        mode = 1
    if i == 'b' or i == 'B':
        mode = 2

if mode == 0:
    print('idiot')
    GameRun = False

if mode == 3:
    board = makeTestB()
else: board = makeNewB()

while GameRun:
    if mode == 3:
        printB(board)
        move = input('whats your move: ')
        print(Translator(move))
        board = moveMaker(move,1, board)

        
    



        

        
