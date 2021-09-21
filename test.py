board = [['wR','wN','wB','wQ','wK','wB','wN','wR'],
        ['wP','wP','wP','wP','wP','wP','wP','wP'],
        ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
        ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
        ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
        ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
        ['bP','bP','bP','bP','bP','bP','wP','wP'],
        ['bR','bN','bB','bQ','bK','bB','bN','wR']]
small = [
    ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
    ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
    ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
    ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
    ['0 ','0 ','0 ','0 ','wB','0 ','0 ','0 '],
    ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
    ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 '],
    ['0 ','0 ','0 ','0 ','0 ','0 ','0 ','0 ']
    ]


Flatboard = [] #making a 2d board into a 1d board
for i in small:
    for a in i:
        Flatboard += [a]
print(Flatboard)
a = -1
wLoc = []
bloc = []


for i in Flatboard: #geting cords of any piece using 1 number
    a += 1
    b = [int(a/8),a%8]

    for t in i:
        if t == 'w':
            wLoc += [[i,b]]


print(wLoc)


def  bishopCheck(loc,side):
    print(2)

for i in wLoc:
    if i[0] == 'wB':
        print(bishopCheck(i[1], 0))
