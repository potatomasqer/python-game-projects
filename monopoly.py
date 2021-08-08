#monopoly
from random import seed
from random import randint
#to do list
#board rendering
players = []
gamerun = 1
truerun = 1

def printb(player,deck,effect):
    if deck[5] == -1 or deck[5] == -2:
        print('-----------------------------------')
        print('                                   ')
        print('         ' + player[0] + '         ')#name
        print('                                   ')
        print('           ' + deck[0] + '         ')#location
        print('           ' + deck[1] + '         ')#cost
        print('  ' + effect + '   ')#effect
        print('-----------------------------------')
    else:
        print('-----------------------------------')
        print('                                   ')
        print('         ' + player[0] + '         ')#name
        print('                                   ')
        print('           ' + deck[0] + '         ')#location
        print('      ' + deck[2][deck[4]] + '     ')#cost
        print('  ' + effect + '   ')#effect
        print('-----------------------------------')





map = [ #map indexs position to the place of storage in publicTable
    [0,'Go'],[6,'Mediterranean avanue'],[1,'Comunity chest'],[7,'Baltic avanue'],[2,'Income tax'],[7,'South railroad'],[6,'Central avanue'],[3,'Chance'],[8,'Vermont avanue'],[9,'Connectatite avanue'],
    [5,'jail'],[11,'St. Olanise place'],[12,'Eletric company'],[13,'States avanue'],[14,'Victoria avanue'],[15,'West railroad'],[16,'St.james place'],[1,'Comunity chest'],[18,'Chicago avanue'],[19,'New york avanue'],
    [20,'Free parking'],[21,'Kentucky avanue'],[3,'Chance'],[23,'Indiana avanue'],[24,'Illnois avanue'],[25,'North railroad'],[26,'Atlantic avanue'],[27,'Wilmont avanue'],[28,'Water works'],[29,'Marvon gardens'],
    [4,'jail'],[31,'Pacific avanue'],[32,'North carolina avanue'],[1,'Comunity chest'],[34,'Pensilvania avanue'],[35,'East railroad'],[3,'chance'],[37,'Park place'],[2,'Luxury Tax'],[39,'Boardwalk']    
    ]
publicTable = [ #format: name,buy cost, rents, house cost, number of houses, who owns it
    ['Go', -200, [],0,0,-2],
    ['Comunity chest',0,[],0,0,-2],
    ['Income tax',200,[],0,0,-2],
    ['Chance',0,[],0,0,-2],
    ['jail',0,[],0,0,-2],
    ['Mediterranean avanue',60,[2,10,30,90,160,250],50,0,-1],
    ['Baltic avanue',60,[4,20,60,180,320,450],50,0,-1]
    ['Park Place',350,[100,200,300,400,500,1500],200,0,-1]


    ]
chance = [

]
comunityChest = [

]
    
while truerun == 1:
    print('welcome to monoplay your classic game where you commit corprate fellonies')
    print('each player will get 1500 to start, lets play')
    pcount = input('how many players are playing today?(2-8):')
    for i in range(pcount):
        name = input('what is player', i,"'s name? \n")
        players += [[i,name,1500,[],0]] #id,name,money,[Hand],position
    gamerun = 1
    while gamerun == 1:
        for i in players:
            canbuy = 0
            effect = ''
            i[4] += randint[2,12]
            if i[4] >= 40:
                i[4] == 0
            Iid = map[i[4]]
            locD = publicTable[Iid[0]]
            if locD[5] == -2:#not a properity
                if locD[0] == 'Go' or locD[0] == 'Income tax':
                    i[3] -= locD[1]
                if locD[0] == 'Chance':
                    i[3] += chance[randint(0,len(chance-1))]
                if locD[0] == 'Comunity chest':
                    i[3] += comunityChest[randint(0,len(comunityChest-1))]
            elif locD[5] == -1: #nobody owns it
                if locD[1] <= i[3]:
                    canbuy = 1
                    effect = 'you can buy' + locD[0]
                else:
                    effect = 'you cant buy' + locD[0]
            else: #somebody owns it
                i[3] -= locD[2][locD[4]]
                players[locD[5]][3] += locD[2][locD[4]]
                effect = 'you paied' + locD[2][locD[4]] +'to'+ players[locD[5]][3]
            #print what happened
            printb(i,locD,effect)
            if canbuy == 1:
                ans = input('do you want to buy ths property?(y/n)')
                if ans == 'y' or ans == 'yes':
                    i[2] -= locD[1]
                    print('bought')
                else:
                    print('not bought')
                    

                


    
    