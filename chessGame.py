#chess attempt #3
#build a system where i can test each piece individualy
#incorperate algebraic notation
#pieces
import chess

board = chess.Board()
showBoard:list = []
tshowBoard = []

def evaluate():
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
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_stalemate():
            return 0
    if board.is_insufficient_material():
            return 0
    
    #material count
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))
    #calculate the scores
    #dont ask me whats going on here. we calculating matterial for the current slice or something
    material = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)
    pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)]
                        for i in board.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
                            for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq = sum([bishopstable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq = bishopsq + sum([-bishopstable[chess.square_mirror(i)]
                            for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
    rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)]
                        for i in board.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([queenstable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
    queensq = queensq + sum([-queenstable[chess.square_mirror(i)]
                            for i in board.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)])
    kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                        for i in board.pieces(chess.KING, chess.BLACK)])
    #evaluate our math
    eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
    if board.turn:
        return eval
    else:
        return -eval

# Searching the best move using minimax and alphabeta algorithm with negamax implementation
def alphabeta(alpha, beta, depthleft):
    bestscore = -9999
    if (depthleft == 0):
        return quiesce(alpha, beta)
    for move in board.legal_moves:
        board.push(move)
        score = -alphabeta(-beta, -alpha, depthleft - 1)
        board.pop()
        if (score >= beta):
            return score
        if (score > bestscore):
            bestscore = score
        if (score > alpha):
            alpha = score
    return bestscore

def quiesce(alpha, beta):
    stand_pat = evaluate()
    if (stand_pat >= beta):
        return beta
    if (alpha < stand_pat):
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -quiesce(-beta, -alpha)
            board.pop()

            if (score >= beta):
                return beta
            if (score > alpha):
                alpha = score
    return alpha

def AiCore(depth): #move list, ai side, current turn
    #mostly written by Ansh Gaikwad
    #https://medium.com/dscvitpune/lets-create-a-chess-ai-8542a12afef

    #set up piece square tables 
    #make board up to date
    #part i added
    print('thinking')
    try:
        move = chess.polyglot.MemoryMappedReader("C:/Users/aabre/books/human.bin").weighted_choice(board).move
        # move = chess.polyglot.MemoryMappedReader("C:/Users/your_path/books/computer.bin").weighted_choice(board).move
        # move = chess.polyglot.MemoryMappedReader("C:/Users/your_path/books/pecg_book.bin").weighted_choice(board).move
        return move
    except:
        bestMove = chess.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000
        for move in board.legal_moves:
            board.push(move)
            boardValue = -alphabeta(-beta, -alpha, depth - 1)
            #print(board,'\n',boardValue)
            if boardValue > bestValue:
                bestValue = boardValue
                bestMove = move
            if (boardValue > alpha):
                alpha = boardValue
            board.pop()
        print(bestMove,'best move')
        return bestMove
    
def putInShow(lis,piece):
    for i in lis:
        tshowBoard[i] = piece

def printShow():
    wp = list(board.pieces(chess.PAWN, chess.WHITE))
    bp = list(board.pieces(chess.PAWN, chess.BLACK))
    wn = list(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = list(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = list(board.pieces(chess.BISHOP, chess.WHITE))
    bb = list(board.pieces(chess.BISHOP, chess.BLACK))
    wr = list(board.pieces(chess.ROOK, chess.WHITE))
    br = list(board.pieces(chess.ROOK, chess.BLACK))
    wq = list(board.pieces(chess.QUEEN, chess.WHITE))
    bq = list(board.pieces(chess.QUEEN, chess.BLACK))
    wk = list(board.pieces(chess.KING, chess.WHITE))
    bk = list(board.pieces(chess.KING, chess.BLACK))
    
    tshowBoard.clear()
    for _ in range(64):
        tshowBoard.append('.')
    putInShow(wp,'P')
    putInShow(bp,'p')
    putInShow(wn,'N')
    putInShow(bn,'n')
    putInShow(wb,'B')
    putInShow(bb,'b')
    putInShow(wr,'R')
    putInShow(br,'r')
    putInShow(wq,'Q')
    putInShow(bq,'q')
    putInShow(wk,'K')
    putInShow(bk,'k')
    #print(tshowBoard)

    showBoard = []
    #add template
    showBoard.append(['.','a','b','c','d','e','f','g','h'])
    showBoard.append(['1'])
    showBoard.append(['2'])
    showBoard.append(['3'])
    showBoard.append(['4'])
    showBoard.append(['5'])
    showBoard.append(['6'])
    showBoard.append(['7'])
    showBoard.append(['8'])
    
    for pn in range(len(tshowBoard)):
        if pn < 8:
            showBoard[1].append(tshowBoard[pn])
        if pn > 7 and pn < 16:
            showBoard[2].append(tshowBoard[pn])
        if pn > 15 and pn < 24:
            showBoard[3].append(tshowBoard[pn])
        if pn > 23 and pn < 32:
            showBoard[4].append(tshowBoard[pn])
        if pn > 31 and pn < 40:
            showBoard[5].append(tshowBoard[pn])
        if pn > 39 and pn < 48:
            showBoard[6].append(tshowBoard[pn])
        if pn > 47 and pn < 56:
            showBoard[7].append(tshowBoard[pn])
        if pn > 55:
            showBoard[8].append(tshowBoard[pn])

    for i in showBoard:
        print(i)

def moveCheck(Move):
    try:
        board.push_uci(Move)
    except:
        move = input('try again: ')
        moveCheck(move)

GameRun = True
print('chess lol')
print('every move uses the position of the piece and where its going. ex e4e5. no need to spesify what the piece is')
p = input('type run to start a normal match. type ai to fight against an ai. type vs to watch the ai fight itself: ')
mode = 0
for i in p: #spliting up a string
    if i == 'r' or i == 'R':
        mode = 1
    if i == 'a' or i == 'A':
        mode = 2
    if i == 't' or i == 'T':
        mode = 3
    if i == 'v' or i == 'V':
        mode = 4
    
if mode == 0:
    print('idiot')
    GameRun = False

side = 1
turn = 0
while GameRun:
    if mode == 1: #starts a normal game
        printShow()
        if side == 1: #white to move
            move = input("White's move: ")
            moveCheck(move)
            side = 2
            if board.is_checkmate:
                GameRun = False
                print('white wins')
            if board.is_stalemate:
                GameRun = False
                print('nobody wins')  
        elif side == 2 and GameRun == True: #black to move
            move = input("Black's move: ")
            moveCheck(move)
            side = 1
            if board.is_checkmate:
                GameRun = False
                print('black wins')     
            if board.is_stalemate:
                GameRun = False
                print('nobody wins')  
    elif mode == 2: #against ai. player is white
        printShow()
        turn += 1
        if side == 1: #white to move
            move = input("White's move: ")
            moveCheck(move)
            side = 2
            if board.is_checkmate == True:
                GameRun = False
                print('white wins')
            if board.is_stalemate == True:
                GameRun = False
                print('nobody wins')  
        elif side == 2 and GameRun == True: #black to move (ai)
            if turn < 5 or turn > 15:
                depth = 3
            else: depth = 2
            move = AiCore(depth)
            moveCheck(str(move))
            side = 1
            if board.is_checkmate == True:
                GameRun = False
                print('black wins')
            if board.is_stalemate == True:
                GameRun = False
                print('nobody wins')
    elif mode == 4:
        printShow()
        if side == 1: #white to move
            if turn < 5 or turn > 15:
                depth = 3
            else: depth = 2
            move = AiCore(depth)
            moveCheck(str(move))
            side = 2
            if board.is_checkmate == True:
                GameRun = False
                print('black wins')
            if board.is_stalemate == True:
                GameRun = False
                print('nobody wins') 
        elif side == 2 and GameRun == True: #black to move (ai)
            if turn < 5 or turn > 15:
                depth = 3
            else: depth = 2
            move = AiCore(depth)
            moveCheck(str(move))
            side = 1
            if board.is_checkmate == True:
                GameRun = False
                print('black wins')
            if board.is_stalemate == True:
                GameRun = False
                print('nobody wins')
    elif mode == 3:
        printShow()
        GameRun = False
