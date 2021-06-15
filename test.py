tL = [1,2,3,4]
ft = []

tmp = []
tmp2 =[]
for i in range(2):
    tmp = tmp + [tmp2]
print(tmp)

for i in range(int(len(tL)/2)):
    ft = ft + [[tL[i*2],tL[i*2+1]]]
print(ft)
fttmp = []
for i in ft:
    fttmp += i
print(fttmp)
print(fttmp.count(1))


allpos = []
for i in range(4):
    allpos = allpos + ft
print(allpos)

print(str(1) + ' players')