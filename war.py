from random import seed
from random import randint

#WAR
#this was origionaly done in swift on the plane lol
deck1 = []
deck2 = []

#ask the observer how many cards to put in each deck
acards = int(input('how many cards will go in each hand? \n'))
print('There are', str(acards*2), 'cards in play')
print('you better not blink or you will miss 50 rounds')

for i in range(acards):
    deck1 += [randint(1,13)]
    deck2 += [randint(1,13)]   

input('press enter to start')
rc = 0
tdeck2 = []
tdeck1 = []
while len(deck1) != 0 and len(deck2) != 0:
    rc += 1
    print(deck1[0], deck2[0], 'cards left', len(deck1), len(deck2), 'round', rc)
    if deck1[0] == deck2[0]:
        if len(deck1) >= 3 and len(deck2) >= 3:
            tdeck1 = [deck1[0], deck1[1], deck1[2]]
            tdeck2 = [deck2[0], deck2[1], deck2[2]]
            deck1.pop(0)
            deck1.pop(0)
            deck1.pop(0)
            deck2.pop(0)
            deck2.pop(0)
            deck2.pop(0)
            if tdeck1[2] == tdeck2[2]:
                if randint(0,1) == 0:
                    deck1.append(tdeck1[0])
                    deck1.append(tdeck1[1])
                    deck1.append(tdeck1[2])
                    deck1.append(tdeck2[0])
                    deck1.append(tdeck2[1])
                    deck1.append(tdeck2[2])
                else:
                    deck2.append(tdeck1[0])
                    deck2.append(tdeck1[1])
                    deck2.append(tdeck1[2])
                    deck2.append(tdeck2[0])
                    deck2.append(tdeck2[1])
                    deck2.append(tdeck2[2])
                
            elif tdeck1[2] > tdeck2[2]:
                deck1.append(tdeck1[0])
                deck1.append(tdeck1[1])
                deck1.append(tdeck1[2])
                deck1.append(tdeck2[0])
                deck1.append(tdeck2[1])
                deck1.append(tdeck2[2])
            else:
                deck2.append(tdeck1[0])
                deck2.append(tdeck1[1])
                deck2.append(tdeck1[2])
                deck2.append(tdeck2[0])
                deck2.append(tdeck2[1])
                deck2.append(tdeck2[2])
        else:
            deck1[0] = randint(1,13)
            deck2[0] = randint(1,13)
        
    elif deck1[0] == 1:
        deck1.append(deck1[0])
        deck1.append(deck2[0])
        deck1.pop(0)
        deck2.pop(0)
    elif deck2[0] == 1:
        deck2.append(deck1[0])
        deck2.append(deck2[0])
        deck1.pop(0)
        deck2.pop(0)
    elif deck1[0] > deck2[0]:
        deck1.append(deck1[0])
        deck1.append(deck2[0])
        deck1.pop(0)
        deck2.pop(0)
    else:
        deck2.append(deck1[0])
        deck2.append(deck2[0])
        deck1.pop(0)
        deck2.pop(0)
    

print('cards left', len(deck1), len(deck2),'round', rc)