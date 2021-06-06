from random import seed
from random import randint

deckcop = [1,2,3,4,5,6,7,8,9,10,10,10,10]
deckcop = deckcop + deckcop + deckcop + deckcop
deck = []
pcards = []
dcards = []

betamount = 0
tmoney = 500
minbet = 5

def makeDeck():
    global deck
    for _ in range(207):
        add = randint(0, 51)
        deck += [deckcop[add]]

def cardDealer():
    card = deck.pop(0)
    return card

def printBoard():
    print(' ________________________________________')
    print('(_______________________________________)')
    print(' ')
    print('                   ' + str(dcards))
    print(' ')
    print(' ')
    print('                   ' + str(pcards))
    print(' _________________________________________')
    print('(________________________________________)')

def check(c): #takes a list of numbers and addes them
    total = 0
    for i in c:
        total += i
    return total


gamedone = 0
while(gamedone == 0):
    #start of the game
    print('welcome to blackjack you start with $510 and end when you either loose it all or end the program')
    done = 0
    turn = 0
    deck = []
    makeDeck()
    pcards =[]
    dcards = []
    betamount = 10

    #pre game
    print('The entry fee is $10')
    if (tmoney >= 10):
        print('You now have $' + str(tmoney) + ' left')
    else:
        print("You dont have the required money, goodbye")
        done = 1
        gamedone = 1

    while (done == 0 and gamedone == 0):

        partdone = 0

        if (done != 1 and turn == 0):
            printBoard()
            pcards += [cardDealer()]
            dcards += [cardDealer()]
            printBoard()
            pcards += [cardDealer()]
            printBoard()

            bet = input('How much more money are you going to bet \n')
            betamount += int(bet)
            print('you now have $' + str(betamount) + ' on the line')

        while(turn%2 == 0 and done != 1): #player
            move = input('choose your move, 0 stand, 1 hit \n')
            if (int(move) == 1):
                pcards += [cardDealer()]
                printBoard()
                turn += 1
            else:
                turn += 1
                partdone = 1
        
        if (turn == 1): #delers responce
                dcards += [cardDealer()]
                printBoard()
                turn += 1
            
        while(turn%2 == 1 and done != 1): # dealer
            #if the delers cards are less than 18 hit
            if (check(dcards) <= 18):
                dcards += [cardDealer()]
                turn += 1
            else:
                partdone += 1
                turn += 1
                
        printBoard()
        #21 check
        dcheck = check(dcards)
        pcheck = check(pcards)

        if (pcheck > 21):
            print('you have a total over 21 you lost')
            tmoney -= betamount
            done = 1
        elif (pcheck == 21 and dcheck != 21):
            print('you win')
            tmoney += betamount
            done = 1
        elif (dcheck > 21):
            print('you win')
            tmoney += betamount
            done = 1
        elif (pcheck == 21 and dcheck == 21):
            print('tie')
            tmoney += 10
            done = 1
        elif (partdone == 2):
            if (dcards > pcards):
                print('you lose')
                tmoney -= betamount
                done = 1
            else:
                print('you win')
                tmoney += betamount
                done = 1
        if (done == 1):
            n = input('do you want to continue (y,n)')
            if (n == 'n'):
                gamedone = 1
