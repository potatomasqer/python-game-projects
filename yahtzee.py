from random import seed
from random import randint

# player gets three rolls of the dice 5 max
# abilty to lock dice

# things to make
# dice roller
# a board to fill out
    #looks like https://www.ultraboardgames.com/yahtzee/gfx/score-sheet.jpg
# locking dice

def newDice():
    return randint(1,6)

def diceManager(dice,locked):
    #dice is a list of all 5 die
    #locked is a list of the ids of locked dice
    for i in range(len(dice)):
        if dice.count(i) == 0:
            #skiping locked id's
            dice[i] = newDice()
    return dice

def printb(Score):
    print('Higher section')
    print('_______________________________________________________________')
    print('')
    print('Aces	Any combination	The sum of dice with the number 1: ' + str(Score[0]))
    print('')
    print('Twos	Any combination	The sum of dice with the number 2: ' + str(Score[1]))
    print('')
    print('Threes Any combination The sum of dice with the number 3: ' + str(Score[2]))
    print('')
    print('Fours Any combination The sum of dice with the number 4: ' + str(Score[3]))
    print('')
    print('Fives Any combination The sum of dice with the number 5: ' + str(Score[4]))
    print('')
    print('Sixes Any combination The sum of dice with the number 6: ' + str(Score[5]))
    print('')
    print('_______________________________________________________________')
    print('Lower section')
    print('_______________________________________________________________')
    print('3 of a kind	At least three dice the same	Sum of all dice: ' + str(Score[6]))
    print('')
    print('4 of a kind	At least four dice the same	    Sum of all dice: ' + str(Score[7]))
    print('')
    print('Full House	Three of one number and two of another	25: ' + str(Score[8]))
    print('')
    print('Low Straight	Four sequential dice	30: ' + str(Score[9]))
    print('')
    print('High Straight	Five sequential dice: ' + str(Score[10]))
    print('')
    print('YAHTZEE	All five dice the same	50: ' + str(Score[11]))
    print('')
    print('Chance	Any combination	Sum of all dice: ' + str(Score[12]))
    print('_______________________________________________________________')

def movemaker():
    movedone = 0
    move = [] # list of locked ids
    while movedone == 0:
        temp = input('what dice would you like to lock? left to right 1-5, input 6 to stop picking: ')
        if temp != '6':
            move += [int(temp)]
        else:
            movedone = 1
    return move

def scoremaker(dice,score):
    # higer
    if dice.count(1) > score[0]:
        score[0] = dice.count(1)
    if dice.count(2)*2 > score[1]:
        score[1] = dice.count(2)*2
    if dice.count(3)*3 > score[2]:
        score[2] = dice.count(3)*3
    if dice.count(4)*4 > score[3]:
        score[3] = dice.count(4)*4
    if dice.count(5)*5 > score[4]:
        score[4] = dice.count(5)*5
    if dice.count(6)*6 > score[5]:
        score[5] = dice.count(6)*6
    #lower
    #3 of a kind
    if dice.count(1) == 3 and 3 > score[6]:
        score[6] = 3
    if dice.count(2) == 3 and 6 > score[6]:
        score[6] = 6
    if dice.count(3) == 3 and 9 > score[6]:
        score[6] = 9
    if dice.count(4) == 3 and 12 > score[6]:
        score[6] = 12 
    if dice.count(5) == 3 and 15 > score[6]:
        score[6] = 15 
    if dice.count(6) == 3 and 18 > score[6]:
        score[6] = 18
    #4 of a kind
    if dice.count(1) == 4 and 4 > score[7]:
        score[7] = 6
    if dice.count(2) == 4 and 8 > score[7]:
        score[7] = 8
    if dice.count(3) == 4 and 12 > score[7]:
        score[7] = 12
    if dice.count(4) == 4 and 16 > score[7]:
        score[7] = 16 
    if dice.count(5) == 4 and 20 > score[7]:
        score[7] = 20 
    if dice.count(6) == 4 and 24 > score[7]:
        score[7] = 24
    #full house
    for i in range(5):
        for a in range(5):
            if dice.count(i+1) == 3:
                if dice.count(a+1) == 2:
                    score[8] == 25
    #Low Straight
    if dice.count(1) == 1 and dice.count(2) == 1 and dice.count(3) == 1 and dice.count(4) == 1:
        score[9] = 30
    if dice.count(2) == 1 and dice.count(3) == 1 and dice.count(4) == 1 and dice.count(5) == 1:
        score[9] = 30
    if dice.count(3) == 1 and dice.count(4) == 1 and dice.count(5) == 1 and dice.count(6) == 1:
        score[9] = 30
    #high streaght
    if dice.count(1) == 1 and dice.count(2) == 1 and dice.count(3) == 1 and dice.count(4) == 1 and dice.count(5):
        score[10] = 40
    if dice.count(6) == 1 and dice.count(2) == 1 and dice.count(3) == 1 and dice.count(4) == 1 and dice.count(5):
        score[10] = 40
    #YAHTZEE
    for a in range(5):
        if dice.count(a+1) == 5:
            score[11] = 50
    #chance
    score[12] = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
    return score


prun = 0
while prun == 0:
    gamerun = 0
    print('Welcome to yahtzee a simple game of rolling die and counting score')
    numb = input('How many people will be playing: ')
    numb = int(numb)
    score = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    printb(score)
    while gamerun == 0:
        for Pid in range(numb):
            print('Player ' + str(Pid+1) + "'s turn")
            dice = []
            for _ in range(5):
                dice += [newDice()]
            print(dice)
            movedone = 0
            move = [] # list of locked ids
            move = movemaker()
            #second spin
            dice = diceManager(dice,move)
            print(dice)
            move = []
            move = movemaker()
            #third spin
            dice = diceManager(dice,move)
            print(dice)
            print('out of spins')
            score = scoremaker(dice,score)
            printb(score)

        if numb == 0:
            gamerun == 1