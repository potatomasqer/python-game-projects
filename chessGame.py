#chess attempt #3
#build a system where i can test each piece individualy
#incorperate algebraic notation
#pieces
import chess
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
def directionalCheck(L,Xmod,Ymod,mark,side): #beams in one direction for moves can do lines and diagonals
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
    allPos = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]] # a list of all moves that a knight can do
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
    if side == 2: # sides are very importent for pawns
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
    if side == 1: # sides are very importent for pawns
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

def evaluate(aiBoard):
    pawntable = [
        0, 0, 0, 0, 0, 0, 0, 0,
        5, 10, 10, -20, -20, 10, 10, 5,
        5, -5, -10, 0, 0, -10, -5, 5,
        0, 0, 0, 20, 20, 0, 0, 0,
        5, 5, 10, 25, 25, 10, 5, 5,
        10, 10, 20, 30, 30, 20, 10, 10,
        50, 50, 50, 50, 50, 50, 50, 50,
        0, 0, 0, 0, 0, 0, 0, 0]

    knightstable = [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20, 0, 5, 5, 0, -20, -40,
        -30, 5, 10, 15, 15, 10, 5, -30,
        -30, 0, 15, 20, 20, 15, 0, -30,
        -30, 5, 15, 20, 20, 15, 5, -30,
        -30, 0, 10, 15, 15, 10, 0, -30,
        -40, -20, 0, 0, 0, 0, -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50]
    bishopstable = [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10, 5, 0, 0, 0, 0, 5, -10,
        -10, 10, 10, 10, 10, 10, 10, -10,
        -10, 0, 10, 10, 10, 10, 0, -10,
        -10, 5, 5, 10, 10, 5, 5, -10,
        -10, 0, 5, 10, 10, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -10, -10, -10, -10, -20]
    rookstable = [
        0, 0, 0, 5, 5, 0, 0, 0,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        5, 10, 10, 10, 10, 10, 10, 5,
        0, 0, 0, 0, 0, 0, 0, 0]
    queenstable = [
        -20, -10, -10, -5, -5, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 5, 5, 5, 5, 5, 0, -10,
        0, 0, 5, 5, 5, 5, 0, -5,
        -5, 0, 5, 5, 5, 5, 0, -5,
        -10, 0, 5, 5, 5, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -5, -5, -10, -10, -20]
    kingstable = [
        20, 30, 10, 0, 0, 10, 30, 20,
        20, 20, 0, 0, 0, 0, 20, 20,
        -10, -20, -20, -20, -20, -20, -20, -10,
        -20, -30, -30, -40, -40, -30, -30, -20,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30]
    #checkmate and stalemate
    if aiBoard.is_checkmate():
        if aiBoard.turn:
            return -9999
        else:
            return 9999
    if aiBoard.is_stalemate():
            return 0
    if aiBoard.is_insufficient_material():
            return 0
    
    #material count
    wp = len(aiBoard.pieces(chess.PAWN, chess.WHITE))
    bp = len(aiBoard.pieces(chess.PAWN, chess.BLACK))
    wn = len(aiBoard.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(aiBoard.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(aiBoard.pieces(chess.BISHOP, chess.WHITE))
    bb = len(aiBoard.pieces(chess.BISHOP, chess.BLACK))
    wr = len(aiBoard.pieces(chess.ROOK, chess.WHITE))
    br = len(aiBoard.pieces(chess.ROOK, chess.BLACK))
    wq = len(aiBoard.pieces(chess.QUEEN, chess.WHITE))
    bq = len(aiBoard.pieces(chess.QUEEN, chess.BLACK))
    #calculate the scores
    #dont ask me whats going on here. we calculating matterial for the current slice or something
    material = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)
    pawnsq = sum([pawntable[i] for i in aiBoard.pieces(chess.PAWN, chess.WHITE)])
    pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)]
                        for i in aiBoard.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([knightstable[i] for i in aiBoard.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
                            for i in aiBoard.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq = sum([bishopstable[i] for i in aiBoard.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq = bishopsq + sum([-bishopstable[chess.square_mirror(i)]
                            for i in aiBoard.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([rookstable[i] for i in aiBoard.pieces(chess.ROOK, chess.WHITE)])
    rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)]
                        for i in aiBoard.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([queenstable[i] for i in aiBoard.pieces(chess.QUEEN, chess.WHITE)])
    queensq = queensq + sum([-queenstable[chess.square_mirror(i)]
                            for i in aiBoard.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([kingstable[i] for i in aiBoard.pieces(chess.KING, chess.WHITE)])
    kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                        for i in aiBoard.pieces(chess.KING, chess.BLACK)])
    #evaluate our math
    eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
    if aiBoard.turn:
        return eval
    else:
        return -eval

# Searching the best move using minimax and alphabeta algorithm with negamax implementation
def alphabeta(alpha, beta, depthleft,aiBoard):
    bestscore = -9999
    if (depthleft == 0):
        return quiesce(alpha, beta,aiBoard)
    for move in aiBoard.legal_moves:
        aiBoard.push(move)
        score = -alphabeta(-beta, -alpha, depthleft - 1,aiBoard)
        aiBoard.pop()
        if (score >= beta):
            return score
        if (score > bestscore):
            bestscore = score
        if (score > alpha):
            alpha = score
    return bestscore

def quiesce(alpha, beta,aiBoard):
    stand_pat = evaluate(aiBoard)
    if (stand_pat >= beta):
        return beta
    if (alpha < stand_pat):
        alpha = stand_pat

    for move in aiBoard.legal_moves:
        if aiBoard.is_capture(move):
            aiBoard.push(move)
            score = -quiesce(-beta, -alpha,aiBoard)
            aiBoard.pop()

            if (score >= beta):
                return beta
            if (score > alpha):
                alpha = score
    return alpha

def AiCore(Mlist,depth): #move list, ai side, current turn
    #mostly written by Ansh Gaikwad
    #https://medium.com/dscvitpune/lets-create-a-chess-ai-8542a12afef

    #set up piece square tables 
    #make board up to date
    #part i added
    aiBoard = chess.Board()
    for m in Mlist:
        aiBoard.push_san(m)
    #print(aiBoard)
    print('thinking')
    try:
        move = chess.polyglot.MemoryMappedReader("C:/Users/your_path/books/human.bin").weighted_choice(aiBoard).move
        # move = chess.polyglot.MemoryMappedReader("C:/Users/your_path/books/computer.bin").weighted_choice(aiBoard).move
        # move = chess.polyglot.MemoryMappedReader("C:/Users/your_path/books/pecg_book.bin").weighted_choice(aiBoard).move
        return move
    except:
        bestMove = chess.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000
        for move in aiBoard.legal_moves:
            aiBoard.push(move)
            aiBoardValue = -alphabeta(-beta, -alpha, depth - 1,aiBoard)
            #print(aiBoard,'\n',aiBoardValue)
            if aiBoardValue > bestValue:
                bestValue = aiBoardValue
                bestMove = move
            if (aiBoardValue > alpha):
                alpha = aiBoardValue
            aiBoard.pop()
        print(bestMove,'best move')
        return bestMove


    




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
        board[end[1]][end[0]] = Spiece #set board to piece
    except:
        print('illegal move')
        if side == 1: move = input("White's move: ")
        else: move = input("Backs's move: ")
        board = moveMaker(move,side,board)
    
    return board

def checkmateCheck():
    Wk = False
    Bk = False
    for a in board:
        for i in a:
            if i == '|wK|':
                Wk = True
            if i == '|bK|':
                Bk = True
    if Wk == False:
        return 2
    elif Bk == False:
        return 1
    else: return 0

GameRun = True
print('chess lol')
print('every move uses the position of the piece and where its going. ex e4e5. no need to spesify what the piece is')
p = input('type run to start a normal match. type ai to fight against an ai: ')
mode = 0
for i in p: #spliting up a string
    if i == 't':
        mode = 2
    if i == 'r' or i == 'R':
        mode = 1
    if i == 'a' or i == 'A':
        mode = 3
        print('make sure your moves are in perfect algebraic format. else this crashes')
    

if mode == 0:
    print('idiot')
    GameRun = False


if mode == 2:
    board = makeTestB()
else: board = makeNewB()

side = 1
moveList = []
while GameRun:
    if mode == 2:
        printB(board)
        move = input('whats your move: ')
        print(Translator(move))
        board = moveMaker(move,1, board)
    elif mode == 1: #starts a normal game
        printB(board)
        if side == 1: #white to move
            move = input("White's move: ")
            board = moveMaker(move,1, board)
            side = 2
            t = checkmateCheck()
            if t == 1:
                GameRun = False
                print('white wins')
            if t == 2:
                GameRun = False
                print('black wins')
        elif side == 2: #black to move
            move = input("Black's move: ")
            board = moveMaker(move,2, board)
            side = 1
            t = checkmateCheck()
            if t == 1:
                GameRun = False
                print('white wins')
            if t == 2:
                GameRun = False
                print('black wins')
    else: #against ai. player is white
        printB(board)
        if side == 1: #white to move
            move = input("White's move: ")
            moveList += [move]
            board = moveMaker(move,1, board)
            side = 2
            t = checkmateCheck()
            if t == 1:
                GameRun = False
                print('white wins')
            if t == 2:
                GameRun = False
                print('black wins')
        elif side == 2: #black to move ai
            move = AiCore(moveList,2)
            moveList += [str(move)] #we use the str of move to get rid of the move.from_uci() thing
            board = moveMaker(str(move),2, board)
            side = 1
            t = checkmateCheck()
            if t == 1:
                GameRun = False
                print('white wins')
            if t == 2:
                GameRun = False
                print('black wins')

        



        
    



        

        
