#goal make wordle then make a bot that can solve any wordle word
import BetterLists

possiableWords = open("dictionary.txt")

lists = BetterLists.BetterLists({})
lists.newList('Words',possiableWords.readlines()) #put into a custom dictionary for better prossing
currentWord = "AAAAA"


#how does wordle work
#you start with a blank text box that you can put a 5 letter word in
#when you enter a word it splites it into letters
#it will then tell you if the letter is present in the word and if the letter is in the right position in the word
#you have 6 total attempts to get the word right else you loose

def Check(Guess,correctLetters:list,IncorrectLetters:list,correctPositions:list,incorrectPositions:list):
    output = ""
    for i in range(len(Guess)): #split string into letters
        c = "⬛"
        for a in currentWord.replace('\n',''):
            if Guess[i] == a:
                c = "🟨"
                try:correctLetters.index(a)
                except:correctLetters += a
                if Guess[i] == currentWord[i]: #are they in the same spot
                    c = "🟩"
                
                if c == "🟩":
                    try:correctPositions.index([a,[i]])
                    except: correctPositions += [[a,[i]]]
                else:
                    try:incorrectPositions.index([a,[i]])
                    except: incorrectPositions += [[a,[i]]]
        if c == '⬛':
            try: IncorrectLetters.index(Guess[i])
            except: IncorrectLetters.append(Guess[i])
        output += c
    return output

def EndCheck(Guess:str):
    if Guess.replace('\n','') == currentWord.replace('\n',''):
        print("You Win")
        return False
    elif AtemptsLeft == 1:
        print("You loose \n The word was "+currentWord)
        return False
    else: return True

def Used(UsedLetters):
    #calculate used letters
    if len(UsedLetters) == 0:
        UsedLetters += guess #automaticaly splites everything up
    else:
        for i in guess:
            try: UsedLetters.index(i) #see if the letter is there
            except: UsedLetters += i #if not add it
    return UsedLetters

print("Welcome to Wordle the clasic game where you have 6 guesses to guess the right 5 letter word")
Run = True
while Run:
    answer = input("Human or Ai: ")
    for i in answer: #spliting up a string
        if i == 'h' or i == 'H':
            mode = 1
        if i == 'i' or i == 'I':
            mode = 2
        if i == 'e' or i == 'e':
            Run = False

    currentWord = lists.Random('Words') # get a random word
    UsedLetters = []
    AtemptsLeft = 6
    correctLetters = []
    IncorrectLetters = []
    correctLetters = []
    correctPositions = []
    incorrectPositions = []
    InGame = True
    while InGame and Run:
        if mode == 1: #human gameplay
            print(str(AtemptsLeft) + " Attempts left")
            WordNumb = -1
            while WordNumb == -1:
                guess = input("Guess: ")
                guess = guess.lower()
                try:
                    WordNumb = lists.Find('Words',guess + '\n') #add the /n bc thats how read lines gives it to us
                except:
                    print("Not a word")
            

            #Garenteed a valid word
            #check all letters
            output = Check(guess,correctLetters,IncorrectLetters)
            print(output)
            #calculate used letters
            UsedLetters = Used(UsedLetters)
            #check if done
            InGame = EndCheck(guess)
            if InGame == True:
                print("Used Letters: " , UsedLetters)
                AtemptsLeft -= 1
        if mode == 2:
            print(str(AtemptsLeft) + " Attempts left")
            output = ''
            guess = ''
            if AtemptsLeft == 6:
                guess = 'crane\n'
            else:
                lists.newList('excluded',lists.ExcludeByLetters('Words',IncorrectLetters))
                if len(correctLetters) > 0:
                    lists.newList('Ai',lists.FindByLetters('excluded',correctLetters))
                    lists.newList('Ai',lists.ExcludeByPositions('Ai',correctPositions,incorrectPositions))
                    guess = lists.Random('Ai')
                else:
                    lists.newList('Ai',lists.listOfLists['excluded'])
                    guess = lists.Random('Ai')
                
            #give it back to the game to prossess
            print(guess.replace('\n',''))
            output = Check(guess.replace('\n',''),correctLetters,IncorrectLetters,correctPositions,incorrectPositions)
            print(output)
            UsedLetters = Used(UsedLetters)
            InGame = EndCheck(guess)
            if InGame == True:
                AtemptsLeft -= 1

            


            


    