import unittest
def alphabetsoup(word,):   
    letters = []
    for i in range(len(word)):
        letters.append(word[i])
        letters.sort()
    print(*letters, sep='')


word = input('enter a word: ').lower()

alphabetsoup(word)




