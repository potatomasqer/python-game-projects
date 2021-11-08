#minesweeper
#automaticaly solve minesweeper always
import random
hight = 10
length = 20 #size of the to be minesweeper field
amountOfMines = 50 #ammount of mines
going = True

Trueboard = []

def printTrueb(): #print board
    for i in Trueboard:
        print(i)

def formatBoard():
    board = []
    for _ in range(hight):# setting up board with empty squares
        board += [[]]
    for i in board:
        for _ in range(length):
            i += ['|0|']
    return board

def formatShow():
    board = []
    for _ in range(hight):# setting up board with empty squares
        board += [[]]
    for i in board:
        for _ in range(length):
            i += ['|_|']
    return board

Trueboard = formatBoard()

def randomMinePlacer(): #chose a random point in the board and place a mine there 
    Rx = random.randint(0,length-1)
    Ry = random.randint(0,hight-1)
    if Trueboard[Ry][Rx] == '|X|': #if a mine is there run again
        randomMinePlacer()
    else:
        Trueboard[Ry][Rx] = '|X|'

def incrementor(space): #increments numbers from 1 to 8 
    if space == '|0|':
        space = '|1|'
    elif space == '|1|':
        space = '|2|'
    elif space == '|2|':
        space = '|3|'
    elif space == '|3|':
        space = '|4|'
    elif space == '|4|':
        space = '|5|'
    elif space == '|5|':
        space = '|6|'
    elif space == '|6|':
        space = '|7|'
    elif space == '|7|':
        space = '|8|'
    return space #mines are uneffected

def searchY(tobesearched,y):
    marked = []
    for i in range(len(tobesearched)-1):
        if tobesearched[i][1] == y: #look through all of tobesearched and mark every thing that could crash
            marked += [tobesearched[i]]
    for a in marked:
        tobesearched.remove(a)
    return tobesearched

def searchX(tobesearched,x):
    marked = []
    for i in range(len(tobesearched)-1):
        if tobesearched[i][0] == x: #look through all of tobesearched and mark every thing that could crash
            marked += [tobesearched[i]]
    for a in marked:
        tobesearched.remove(a)
    return tobesearched

def printShow(): #print board
    for i in showBoard:
        print(i)

def clearAround(x,y): # clear every space around the designated space reusing some code
    tobesearched = [[1,-1],[1,0],[1,1],[0,-1],[0,1],[-1,-1],[-1,0],[-1,1]] #a list of all 8 directions. can be removed
    if y == 0: #top row
        #remove all -1's to y
        tobesearched = searchY(tobesearched,-1)
    if y == hight-1: #bottom row
        #remove all 1 to y's
        tobesearched = searchY(tobesearched,1)
        tobesearched.remove([-1,1])#was forced to do this here because the FUCKING FUNCTION DID NOT WANT TO
    if x == 0:#left edge
        tobesearched = searchX(tobesearched, -1)
    if x == length-1:#right edge
        tobesearched = searchX(tobesearched,1)
    return tobesearched


def makeBoard():
    Trueboard = formatBoard()
    for _ in range(amountOfMines): #place an amount of mines randomly into the board
        randomMinePlacer()

    for Cy in range(hight): #Cy is for current y position
        for Cx in range(length): #Cx is for current x position
            if Trueboard[Cy][Cx] == '|X|': #mine spotted
                tobesearched = clearAround(Cx,Cy)
                
                for i in tobesearched: #search everything thats left and increment all of them
                    Trueboard[Cy+i[1]][Cx+i[0]] = incrementor(Trueboard[Cy+i[1]][Cx+i[0]])







running = True
while(running):
    showBoard = formatShow()#format a new board
    printShow()

    Trueboard = formatBoard()
    for _ in range(amountOfMines): #place an amount of mines randomly into the board
        randomMinePlacer()

    for Cy in range(hight): #Cy is for current y position
        for Cx in range(length): #Cx is for current x position
            if Trueboard[Cy][Cx] == '|X|': #mine spotted
                #search the 8 around it
                tobesearched = [[1,-1],[1,0],[1,1],[0,-1],[0,1],[-1,-1],[-1,0],[-1,1]] #a list of all 8 directions. can be removed
                if Cy == 0: #top row
                    #remove all -1's to y
                    tobesearched = searchY(tobesearched,-1)
                if Cy == hight-1: #bottom row
                    #remove all 1 to y's
                    tobesearched = searchY(tobesearched,1)
                    tobesearched.remove([-1,1])#was forced to do this here because the FUCKING FUNCTION DID NOT WANT TO
                if Cx == 0:#left edge
                    tobesearched = searchX(tobesearched, -1)
                if Cx == length-1:#right edge
                    tobesearched = searchX(tobesearched,1)
                
                for i in tobesearched: #search everything thats left and increment all of them
                    Trueboard[Cy+i[1]][Cx+i[0]] = incrementor(Trueboard[Cy+i[1]][Cx+i[0]])

    
    finalBoard = Trueboard
    for Cy in range(hight): #Cy is for current y position
        for Cx in range(length):
           if finalBoard[Cy][Cx] == '|X|':
               finalBoard[Cy][Cx] = '|_|'
            

    ingame = True
    while(ingame):
        cords = input('cord format #,#; top left is 0,0 have fun: ')
        xCord = '' #strings for now but will be changed to int
        yCord = ''
        t = 0#temperary var there just to switch between x and y
        for i in cords: #seperate a string into single letters and numbers in string format
            if t == 3:
                t=1
            if i == ',':
                t=3
            if t == 0:
                xCord += i
            if t == 1:
                yCord += i
        xCord = int(xCord)
        yCord = int(yCord)

        #pierce showboard into true board
        showBoard[yCord][xCord] = Trueboard[yCord][xCord]

        if Trueboard[yCord][xCord] == '|0|': #when you hit a 0 reveal all around it
            remove = clearAround(xCord,yCord)
            while len(remove) != 0: #continue while there are still markes
                i = remove[0]
                showBoard[yCord+i[1]][xCord+i[0]] = Trueboard[yCord+i[1]][xCord+i[0]] #pull marked spot into show
                remove.remove(i)
                if showBoard[yCord+i[1]][xCord+i[0]] == '|0|': #if we run into another 0
                    tmark = clearAround(xCord+i[0],yCord+i[1]) #collect new marks for that 0
                    for t in tmark:
                        if remove.count(t) == 0 and showBoard[yCord+t[1]+i[1]][xCord+t[0]+i[0]] == '|_|': #if a spot isnt already marked mark it
                            remove += [[t[0]+i[0],t[1]+i[1]]] #account for location

        #printTrueb()
        printShow()

        if Trueboard[yCord][xCord] == '|X|':
            print('YOU LOSE \n \n')
            ingame = False
        
        if showBoard == finalBoard:
            print('YOU WIN \n \n')
            ingame = False

        
    printTrueb()
    for i in input('New Game?  '):
        if i == 'n': #check for a no responce of any kind
            running = False


print('\n \n \n')
printTrueb()