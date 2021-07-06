#Briscas
#40 cards 1-12 times
#5 cards in each hand and a trump card.
#4 types of cards
# 1 type is always trump.(wins against everything exept itself.)
from random import seed
from random import randint

deck = []
p1Thand = []
p2Thand = []
p1Shand = []
p2Shand = []
p1Taken = []
p2Taken = []
trump = []
turn = 0

def cardtoshow(card):
    show = ''
    if card[0] == 1:
        show += 'B'
    if card[0] == 2:
        show += 'C'
    if card[0] == 3:
        show += 'M'
    if card[0] == 4:
        show += 'S'

    if card[1] == 1:
        show += '1'
    if card[1] == 2:
        show += '2'
    if card[1] == 3:
        show += '3'
    if card[1] == 3:
        show += '3'
    if card[1] == 4:
        show += '4'
    if card[1] == 5:
        show += '5'
    if card[1] == 6:
        show += '6'
    if card[1] == 7:
        show += '7'
    if card[1] == 8:
        show += '8'
    if card[1] == 9:
        show += '9'
    if card[1] == 10:
        show += '10'
    if card[1] == 11:
        show += '11'
    if card[1] == 12:
        show += '12'
    return 

def printB(p1card,p2card):
    print(' ________________________________________')
    print('(_______________________________________)')
    print('')
    print('                ' + '[0,0,0,0,0,0]' )
    print('')
    print('')
    print('                    ' + p2card)
    print('')
    print('')
    print('                  ' + '[0] ' + trump)
    print('')
    print('')
    print('                    ' + p1card)
    print('')
    print('')
    print('                ' + p1Shand)
    print(' _________________________________________')
    print('(________________________________________)')

def ai():
    trump[0]
    return




    
gamedone = 0
while gamedone == 0:
    run = 0
    temp = []
    for i in range(4):
        for a in range(12):
            temp += [[i+1,a+1]]
    for _ in range(len(temp)-1):
        deck = [temp[randint(0,len(temp)-1)]]
    
    for _ in range(5):
        p1Thand = deck.pop(0)
        p2Thand = deck.pop(0)

        for i in p1Thand:
            p1Shand = cardtoshow(i)
        for i in p2Thand:
            p2Shand = cardtoshow(i)
    
    trump = deck.pop(0)
    trump = deck.pop(0)
        
    while run == 0:
        printB("","")
        if turn == 0:
            done = 0
            while done == 0
                move = input('what card will you play? \n')
                if p1Shand.count(move) == 1:
                    done = 1
            printB(move,'')
            amove = ai()

        p1Shand = []
        p2Shand = []
        for i in p1Thand:
            p1Shand = cardtoshow(i)
        for i in p2Thand:
            p2Shand = cardtoshow(i)


