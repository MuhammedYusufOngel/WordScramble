import tkinter as tk
from tkinter import *
import addWord
from tkinter import messagebox
import homepage
import wordDictionary

isTrue = False
timerRunning = True
squareInfo = set()
squares = []
wordCoord = []
wordsPlace = [900,100,900,150,900,200,900,250,900,300,900,350,900,400,900,450]
firstIndex = 0
lastIndex = 0
x = -1
y = -1

elapsed_time = 0

isFindW1 = False
isFindW2 = False
isFindW3 = False
isFindW4 = False
isFindW5 = False
isFindW6 = False
isFindW7 = False
isFindW8 = False


isFinished = True

select = 0
firstSquare = []
lastSquare = []
word = ""
isError = False

# Function to add words to the game
def addWordGame():
    addWord.createTable()
    addWord.selectedWords = wordDictionary.randomWords()
    
     # Adding selected words to the game
    for selectedWord in addWord.selectedWords:
        addWord.addWord(selectedWord[0])

    addWord.inTheEnd()

# Function to reset the game
def reset():
    addWordGame()

    addWord.words = []
    addWord.table = []
    global isTrue, timerRunning, squareInfo, squares, wordCoord, wordsPlace, firstIndex, x, y, elapsed_time
    global isFindW1, isFindW2, isFindW3, isFindW4, isFindW5, isFindW6, isFindW7, isFindW8
    global select, firstSquare, lastSquare, word, isError, isFinished

    isTrue = False
    timerRunning = True
    squareInfo = set()
    squares = []
    wordCoord = []
    wordsPlace = [900,100,900,150,900,200,900,250,900,300,900,350,900,400,900,450]
    firstIndex = 0
    x = -1
    y = -1

    elapsed_time = 0

    isFindW1 = False
    isFindW2 = False
    isFindW3 = False
    isFindW4 = False
    isFindW5 = False
    isFindW6 = False
    isFindW7 = False
    isFindW8 = False

    isFinished = True

    select = 0
    firstSquare = []
    lastSquare = []
    word = ""
    isError = False

def run(root):
    addWordGame()

    frame2 = tk.Frame(root, relief="ridge", borderwidth=2, width=1080, height=840)
    frame2.pack()
    canvas = tk.Canvas(frame2, width=1080, height=840)

    for i in range(8):
        tk.Label(frame2, text=addWord.selectedWords[i][0], font=("Helvetica", 18)).place(x=900, y=100+50*i)

    # This function provides that show answers
    def answer(count):
        for wordCoord in addWord.words[count]:
            canvas.create_rectangle(100+35*wordCoord["x"], 30+35*wordCoord["y"],  135+35*wordCoord["x"], 65+35*wordCoord["y"], outline = "black", fill = "red", width=2)
            canvas.create_text(117+35*wordCoord["x"], 47+35*wordCoord["y"], text=wordCoord["letter"], font=("Helvetica", 12))
            
    # This function provides that show answers.
    def answers():
        global isFindW1,isFindW2,isFindW3,isFindW4,isFindW5,isFindW6,isFindW7,isFindW8
        global timerRunning, isFinished

        #If user's answer is wrong, restores user selected boxes.
        if(isTrue == False):
            for letter in wordCoord:
                canvas.create_rectangle(letter["x0"], letter["y0"], letter["x1"], letter["y1"], outline = "black", fill = "white", width=2)
                canvas.create_text(letter["letterX"], letter["letterY"], text=letter["letter"], font=("Helvetica", 12))
        

        #Count is word index.
        count = -1
        
        #It does not display the words that the user knows correctly
        #Just display words that the user didn't knows
        for count in range(0, 8):

            if count == 0 and isFindW1 == False:
                answer(count)
            
            elif count == 1 and isFindW2 == False:
                answer(count)
            
            elif count == 2 and isFindW3 == False:
                answer(count)
            
            elif count == 3 and isFindW4 == False:
                answer(count)
            
            elif count == 4 and isFindW5 == False:
                answer(count)
            
            elif count == 5 and isFindW6 == False:
                answer(count)
            
            elif count == 6 and isFindW7 == False:
                answer(count)
            
            elif count == 7 and isFindW8 == False:
                answer(count)
        
        timerRunning = False
        isFinished = False
    
    #Restart the game
    def newGame():
        frame2.destroy()
        reset()
        run(root=root)

    #Go to home page
    def goHome():
        frame2.destroy()
        reset()
        homepage.home(root=root)

    tk.Button(frame2, text="Answers", font=("Helvetica", 14), command=answers).place(x = 900, y = 600)
    tk.Button(frame2, text="New Game", font=("Helvetica", 14), command=newGame).place(x = 900, y = 650)
    tk.Button(frame2, text="Home Page", font=("Helvetica", 14), command=goHome).place(x = 900, y = 700)

    def timer():
        global elapsed_time, timerRunning

        if(timerRunning):
            elapsed_time += 1
            tk.Label(frame2, text=str(elapsed_time), font=("Helvetica", 18)).place(x = 0, y = 0)
            root.after(1000, timer)

    def showMessage():
        if isFinished:
            messagebox.showinfo("Congratulations","Congratulations! You finished test at " + str(elapsed_time) + " seconds")

    #This function provides that navigation in selected boxes.
    def strollInWord(wordCoord, color):
        for letter in wordCoord:
            canvas.create_rectangle(letter["x0"], letter["y0"], letter["x1"], letter["y1"], outline = "black", fill = color, width=2)
            canvas.create_text(letter["letterX"], letter["letterY"], text=letter["letter"], font=("Helvetica", 12))

    #This function control that the game is over or not.
    def control():
        global timerRunning

        if(isFindW1 and isFindW2 and isFindW3 and isFindW4 and isFindW5 and isFindW6 and isFindW7 and isFindW8):
            timerRunning = False
            showMessage()
        
    def reverse(string):
        string = string[::-1]
        return string

    #This function combines word boxes
    def chooseWord(index):
        global squares, canvas, word

        print(squares[index])
        word = word + squares[index]["letter"]

        squareCoord = {"x0": squares[index]["x0"], "y0": squares[index]["y0"], "x1": squares[index]["x1"], "y1": squares[index]["y1"], "letterX":squares[index]["letterX"], "letterY":squares[index]["letterY"], "letter":squares[index]["letter"] }
        return squareCoord

    #Switch-case: 
    def switch(key, index, gap):
        global squares, canvas, word, isError

        #Key0 = Left to right
        if key == 0:
            for i in range(gap+1):
                wordCoord.append(chooseWord(index-20*i))
            isError = False

        #Key1 = Up to down
        elif key == 1:
            for i in range(gap+1):
                wordCoord.append(chooseWord(index-i))
            isError = False

        #Key2 = Cross
        elif key == 2:
            for i in range(gap+1):
                wordCoord.append(chooseWord(index-21*i))
            isError = False

        #Key3 = Answer is wrong
        elif key == 3:
            wordCoord.append(chooseWord(firstIndex))
            wordCoord.append(chooseWord(lastIndex))
            isError = True


    #This function displays and saves letters
    def squareFunc():
        global x, y

        for i in range(20):
            x = x + 1
            for j in range(20):
                y = y + 1
                x0 = 100+35*i
                y0 = 30+35*j
                x1 = 135+35*i
                y1 = 65+35*j
                letterX = 117+35*i
                letterY = 47+35*j
                letter = addWord.table[i][j]

                squareInfo = {"x0": x0, "y0": y0, "x1": x1, "y1": y1, "letter": letter, "letterX":letterX, "letterY":letterY, "x":x, "y":y}
                squares.append(squareInfo)

                canvas.create_rectangle(x0, y0, x1, y1, outline = "black", fill = "white", width=2)
                canvas.create_text(letterX, letterY, text=letter, font=("Helvetica", 12))
            y = -1

    def double_click(event):
        global select, firstSquare, lastSquare, word, wordCoord, isTrue, firstIndex, lastIndex
        global isFindW1, isFindW2, isFindW3, isFindW4, isFindW5, isFindW6, isFindW7, isFindW8 

        word = ""
        #400 = 20 * 20
        #This loop combines the first and last boxes the user selected.
        for index in range(400):
            
            #If the user clicked on any box of the game
            if squares[index]["x0"] < event.x and squares[index]["x1"] > event.x and squares[index]["y0"] < event.y and squares[index]["y1"] > event.y:
                select = select + 1

                #If select is 1, the box is the first box selected.
                if select == 1:
                    firstSquare.append(squares[index]["x"])
                    firstSquare.append(squares[index]["y"])
                    
                    firstSquare[0] = squares[index]["x"]
                    firstSquare[1] = squares[index]["y"]
                    
                #If select is 1, the box is the last box selected.
                elif select == 2:
                    lastSquare.append(squares[index]["x"])
                    lastSquare.append(squares[index]["y"])
                    
                    lastSquare[0] = squares[index]["x"]
                    lastSquare[1] = squares[index]["y"]

            if select == 1 and firstSquare[0] == squares[index]["x"] and firstSquare[1] == squares[index]["y"]:
                
                #If isTrue is False, previous choice was wrong. Therefore, the boxes selected by the user are restored.
                if(isTrue == False):
                    for letter in wordCoord:
                        canvas.create_rectangle(letter["x0"], letter["y0"], letter["x1"], letter["y1"], outline = "black", fill = "white", width=2)
                        canvas.create_text(letter["letterX"], letter["letterY"], text=letter["letter"], font=("Helvetica", 12))
                
                canvas.create_rectangle(squares[index]["x0"], squares[index]["y0"], squares[index]["x1"], squares[index]["y1"], outline = "black", fill = "yellow", width=2)
                canvas.create_text(squares[index]["letterX"], squares[index]["letterY"], text=squares[index]["letter"], font=("Helvetica", 12))
                firstIndex = index

                wordCoord = []
                
            if select == 2 and lastSquare[0] == squares[index]["x"] and lastSquare[1] == squares[index]["y"]:
                #gap is how many letters the selected word has.
                gap = lastSquare[0] - firstSquare[0] if lastSquare[0] > firstSquare[0] else lastSquare[1] - firstSquare[1]
                
                
                if (lastSquare[0] >= firstSquare[0] and lastSquare[1] >= firstSquare[1] and (lastSquare[0] - firstSquare[0] == lastSquare[1] - firstSquare[1] or lastSquare[0] == firstSquare[0] or lastSquare[1] == firstSquare[1])):
                    if lastSquare[0] > firstSquare[0]:
                        if lastSquare[1] > firstSquare[1]:
                            #Cross
                            situation = 2
                        else:
                            #Left to right
                            situation = 0
                    else:
                        #Up to down
                        situation = 1
                #If lastSquare's index is less than firstSquare's index
                #If the resulting line is not diagonal, horizontal or vertical
                else:
                    messagebox.showinfo("Warning", "You can't make a move like this!!! You can only move left to right, top to bottom and diagonally.")
                    canvas.create_rectangle(squares[index]["x0"], squares[index]["y0"], squares[index]["x1"], squares[index]["y1"], outline = "black", fill = "yellow", width=2)
                    canvas.create_text(squares[index]["letterX"], squares[index]["letterY"], text=squares[index]["letter"], font=("Helvetica", 12))
                    lastIndex = index
                    #Error situation
                    situation = 3

                switch(key=situation, index=index, gap=gap)
                
                isTrue = False

                #If there is no error
                if isError != True:
                    count = 0
                    wordCoordOrder = 0

                    for searchWordList in addWord.selectedWords:
                        count = count + 1
                        
                        #We try to find out which word it is
                        if word == reverse(searchWordList[0]):
                            strollInWord(wordCoord, "green")

                            word = tk.Label(frame2, text=reverse(word), font=("Helvetica", 18), foreground="green")
                            
                            wordCoordOrder = wordCoordOrder + 2

                            if count == 1: 
                                isFindW1 = True
                                word.place(x = 900, y = 100)

                            elif count == 2: 
                                isFindW2 = True
                                word.place(x = 900, y = 150)

                            elif count == 3: 
                                isFindW3 = True
                                word.place(x = 900, y = 200)

                            elif count == 4: 
                                isFindW4 = True
                                word.place(x = 900, y = 250)

                            elif count == 5: 
                                isFindW5 = True
                                word.place(x = 900, y = 300)

                            elif count == 6: 
                                isFindW6 = True
                                word.place(x = 900, y = 350)

                            elif count == 7: 
                                isFindW7 = True
                                word.place(x = 900, y = 400)

                            elif count == 8: 
                                isFindW8 = True
                                word.place(x = 900, y = 450)
                            
                            isTrue = True

                            control()

                    #Answer is wrong
                    if isTrue == False:
                        strollInWord(wordCoord, "red")
                        isTrue = False

                    select = 0
                    break
                
                else:
                    isTrue = False

                select = 0

    squareFunc()
    timer()

    root.bind('<Button-1>', double_click)

    canvas.pack()