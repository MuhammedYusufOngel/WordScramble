#This file provides choose random words in text files. 
import random

def randomWords():
    words = []
    for j in range(3,11):
        #Open file
        file = open('./Words/words' + str(j) + ".txt", 'r')

        #random value for word to be chosen
        rand = random.randint(1,99)
        i = 0

        #It chooses the word randomly
        for word in file:
            i = i + 1
            if i == rand:
                words.append(word.lower().split())
        
    return words
