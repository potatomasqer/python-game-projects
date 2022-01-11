#chess attempt #3
#build a system where i can test each piece individualy
#incorperate algebraic notation
#pieces
import chess

board = chess.Board()

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
def alphabeta(alpha, beta, depthleft,board):
    bestscore = -9999
    if (depthleft == 0):
        return quiesce(alpha, beta,board)
    for move in board.legal_moves:
        board.push(move)
        score = -alphabeta(-beta, -alpha, depthleft - 1,board)
        board.pop()
        if (score >= beta):
            return score
        if (score > bestscore):
            bestscore = score
        if (score > alpha):
            alpha = score
    return bestscore

def quiesce(alpha, beta,board):
    stand_pat = evaluate(board)
    if (stand_pat >= beta):
        return beta
    if (alpha < stand_pat):
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -quiesce(-beta, -alpha,board)
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
            boardValue = -alphabeta(-beta, -alpha, depth - 1,board)
            #print(board,'\n',boardValue)
            if boardValue > bestValue:
                bestValue = boardValue
                bestMove = move
            if (boardValue > alpha):
                alpha = boardValue
            board.pop()
        print(bestMove,'best move')
        return bestMove

def moveCheck(Move):
    try:
        board.push(Move)
    except:
        move = print('try again: ')
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
        print('make sure your moves are in perfect algebraic format. else this crashes')
    

if mode == 0:
    print('idiot')
    GameRun = False


side = 1
moveList = []
turn = 0
while GameRun:
    if mode == 1: #starts a normal game
        print(board)
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
        print(board)
        turn += 1
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
        elif side == 2 and GameRun == True: #black to move (ai)
            if turn < 5 or turn > 15:
                depth = 3
            else: depth = 2
            move = AiCore(depth)
            moveCheck(move)
            side = 1
            if board.is_checkmate:
                GameRun = False
                print('black wins')
            if board.is_stalemate:
                GameRun = False
                print('nobody wins')  