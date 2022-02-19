from random import randint


class BetterLists:
    def __init__(self,listOfLists:dict[str,list]) -> None:
        self.listOfLists = listOfLists
    def newList(self,Name: str,Data:list):
        self.listOfLists.update({Name:Data}) #dictionary :p
    def FindLetter(self,Name,Letter:str):
        try:
            data = self.listOfLists[Name]
            c = -1
            loc = []
            for i in data:
                c += 1
                for a in i:
                    if a.lower() == Letter.lower():
                        try:loc.index[c] #just in case a word has more than one of the same letter
                        except:loc += [c]
            found = []
            for i in loc:
                try: found.index(data[i])
                except: found += [data[i]]
            return found
        except: return ValueError
    def Random(self,Name:str):
        return self.listOfLists[Name][randint(0,len(self.listOfLists[Name])-1)]
    def Find(self,Name:str,item):
        try:
            position = self.listOfLists[Name].index(item)
            return position
        except: return ValueError
    def FindByLetters(self,Name:str,Letters:list[str]):
        self.newList('Found',self.FindLetter(Name,Letters[0]))
        try:
            if len(Letters) > 1:
                for i in range(len(Letters)-1): #to keep track of what letter we are on
                    self.newList('Found',self.FindLetter('Found',Letters[i+1]))
            return self.listOfLists['Found']
        except:return ValueError
    def ExcludeByLetters(self,Name:str,Letters:list[str]):
        edited = []
        try:
            for i in self.listOfLists[Name]:#every word
                exclud = False
                for a in i: #every letter 
                    for b in Letters:
                        if b == a: #if the letter is banned 
                            exclud = True
                if not exclud:
                    try: edited.index(i)
                    except: edited += [i]
            return edited
        except:return ValueError
    def ExcludeByPosition(self,Name:str,Letter:str,position:int):
        edited = []
        try:
            for i in self.listOfLists[Name]: #every word
                exclud = False
                if i[position] == Letter: #if the two letters are the same
                    exclud = True
                if not exclud:
                    edited += [i]
            return edited
        except:return ValueError
        #positions sintax
        #[[letter,[position]]
    def ExcludeByPositions(self,Name:str,CorrectPositions:list,IncorrectPositions:list):
        unknownpos = [0,1,2,3,4]
        if len(CorrectPositions) > 0:
            for i in CorrectPositions:
                try: 
                    p = unknownpos.index(i[1][0])
                    unknownpos.pop(p)
                except: True
        self.newList('Edited',self.listOfLists[Name])
        try:
            for i in self.listOfLists[Name]: #word
                if len(CorrectPositions) > 0:
                    for b in CorrectPositions:#[[letter,[position]]]
                            for c in range(5):
                                try: 
                                    b[1].index(c) #remove everywhere but this position
                                except: 
                                    try: 
                                        unknownpos.index(c)
                                        #if unknown dont remove
                                    except:
                                        cnt = 0
                                        skp = False
                                        for d in CorrectPositions:
                                            if d[0] == b[0]: #check if the letter has multiple correct positions
                                                cnt +=1
                                                if d[1] == c: #skip the current position
                                                    skp = True
                                        if cnt > 1: #letter has more then one copy
                                            if skp:True #do nothing
                                            else: self.newList('Edited',self.ExcludeByPosition('Edited',b[0],c))
                                        else: self.newList('Edited',self.ExcludeByPosition('Edited',b[0],c))
                if len(IncorrectPositions) > 0:
                    for b in IncorrectPositions:
                        for c in b[1]:
                            self.newList('Edited',self.ExcludeByPosition('Edited',b[0],c))
            return self.listOfLists['Edited']
        except:return ValueError


