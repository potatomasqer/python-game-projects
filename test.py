words = open("dictionary.txt")
words = words.readlines()
n = words.index(('cloud'+'\n'))
print(n,words[n])