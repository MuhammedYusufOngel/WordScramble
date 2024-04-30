import random
import wordDictionary

# Global variables
table = []   # Represents the game board
words = []   # Stores the coordinates and letters of the placed words
wordLetters = []  # Temporary list to hold the letters of a word during placement

# Function to create an empty game board
def createTable():
    global table
    
    table = []

    # Creating a 20x20 grid filled with '-'
    for i in range(20):
        line = []
        for j in range(20):
            line.append('-')
        table.append(line)

# Function to add a word to the game board
def addWord(word):
    global wordLetters

    wordLetters = []
    c = []

    # Function to randomly choose the placement direction and place the word
    def switch(key, isEmpty):
        if key == 0:  # Horizontal placement
            while isEmpty == False:
                isEmpty = True
                x = random.randint(0, 20 - len(word))
                y = random.randint(0, 19)

                for i in range(len(word)):
                    if table[x + i][y] != '-':
                        isEmpty = False
                        break
                
            for i in range(len(word)):
                table[x + i][y] = c[i]
                wordCoord = {"x": x + i, "y": y, "letter": c[i]}
                wordLetters.append(wordCoord)

            words.append(wordLetters)
        
        elif key == 1:  # Vertical placement
            while isEmpty == False:
                isEmpty = True
                x = random.randint(0, 19)
                y = random.randint(0, 20 - len(word))

                for i in range(len(word)):
                    if table[x][y + i] != '-':
                        isEmpty = False
                        break
            
            for i in range(len(word)):
                table[x][y + i] = c[i]
                wordCoord = {"x": x, "y": y + i, "letter": c[i]}
                wordLetters.append(wordCoord)

            words.append(wordLetters)

        elif key == 2:  # Diagonal placement
            while isEmpty == False:
                isEmpty = True
                x = random.randint(0, 20 - len(word))
                y = random.randint(0, 20 - len(word))

                for i in range(len(word)):
                    if table[x + i][y + i] != '-':
                        isEmpty = False
                        break
            
            for i in range(len(word)):
                table[x + i][y + i] = c[i]
                wordCoord = {"x": x + i, "y": y + i, "letter": c[i]}
                wordLetters.append(wordCoord)

            words.append(wordLetters)

    # Convert word into a list of characters
    for character in word:
        c.append(character)

    # Randomly choose the placement direction
    randSituation = random.randint(0, 2)

    # Call switch function to place the word
    switch(randSituation, False)

# Function to fill empty spaces on the game board with random letters
def inTheEnd():

    # Fill empty spaces with random letters
    for i in range(20):
        for j in range(20):
            if table[i][j] == '-':
                randChar = chr(random.randint(97, 122))  # Random lowercase letter
                table[i][j] = randChar