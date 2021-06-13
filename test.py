tL = [1,2,3,4]
ft = []

print(len(tL)/2)
for i in range(int(len(tL)/2)):
    ft = ft + [[tL[i*2],tL[i*2+1]]]
    print(i)
print(ft)
fttmp = []
for i in ft:
    fttmp += i
print(fttmp)
print(fttmp.count(1))

print(int(1/8))