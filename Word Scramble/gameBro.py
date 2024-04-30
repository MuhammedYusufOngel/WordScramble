import tkinter as tk
from tkinter import *
import addWord
from tkinter import messagebox
import subprocess


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

select = 0
firstSquare = []
lastSquare = []
word = ""
isError = False


def run(root):
    frame2 = tk.Frame(root, relief="ridge", borderwidth=2, width=1080, height=840)
    frame2.pack()
    canvas = tk.Canvas(frame2, width=1080, height=840)
    tk.Label(frame2, text=addWord.selectedWords[0][0], font=("Helvetica", 18)).place(x = 900, y = 100)
    tk.Label(frame2, text=addWord.selectedWords[1][0], font=("Helvetica", 18)).place(x = 900, y = 150)
    tk.Label(frame2, text=addWord.selectedWords[2][0], font=("Helvetica", 18)).place(x = 900, y = 200)
    tk.Label(frame2, text=addWord.selectedWords[3][0], font=("Helvetica", 18)).place(x = 900, y = 250)
    tk.Label(frame2, text=addWord.selectedWords[4][0], font=("Helvetica", 18)).place(x = 900, y = 300)
    tk.Label(frame2, text=addWord.selectedWords[5][0], font=("Helvetica", 18)).place(x = 900, y = 350)
    tk.Label(frame2, text=addWord.selectedWords[6][0], font=("Helvetica", 18)).place(x = 900, y = 400)
    tk.Label(frame2, text=addWord.selectedWords[7][0], font=("Helvetica", 18)).place(x = 900, y = 450)


    def timer():
        global elapsed_time, timerRunning

        if(timerRunning):
            elapsed_time += 1
            tk.Label(frame2, text=str(elapsed_time), font=("Helvetica", 18)).place(x = 0, y = 0)
            root.after(1000, timer)

    def showMessage():
        messagebox.showinfo("Congratulations","Congratulations! You finished test at " + str(elapsed_time) + " seconds")
        result = messagebox.askquestion("New Game", "New Game?")
        if result == "yes":
            root.destroy()
            subprocess.run(["python", "game.py"])
        if result == "no":
            root.destroy()
            subprocess.run(["python", "main.py"])

    def strollInWord(wordCoord, color):
        for letter in wordCoord:
            canvas.create_rectangle(letter["x0"], letter["y0"], letter["x1"], letter["y1"], outline = "black", fill = color, width=2)
            canvas.create_text(letter["letterX"], letter["letterY"], text=letter["letter"], font=("Helvetica", 12))

    def control():
        global timerRunning

        if(isFindW1 and isFindW2 and isFindW3 and isFindW4 and isFindW5 and isFindW6 and isFindW7 and isFindW8):
            timerRunning = False
            showMessage()
        
    def reverse(string):
        string = string[::-1]
        return string

    def chooseWord(index):
        global squares, canvas, word

        print(squares[index])
        word = word + squares[index]["letter"]

        squareCoord = {"x0": squares[index]["x0"], "y0": squares[index]["y0"], "x1": squares[index]["x1"], "y1": squares[index]["y1"], "letterX":squares[index]["letterX"], "letterY":squares[index]["letterY"], "letter":squares[index]["letter"] }
        return squareCoord

    def switch(key, index, fark):
        global squares, canvas, word, isError

        if key == 0:
            for i in range(fark+1):
                wordCoord.append(chooseWord(index-20*i))
            isError = False

        elif key == 1:
            for i in range(fark+1):
                wordCoord.append(chooseWord(index-i))
            isError = False

        elif key == 2:
            for i in range(fark+1):
                wordCoord.append(chooseWord(index-21*i))
            isError = False

        elif key == 3:
            wordCoord.append(chooseWord(firstIndex))
            isError = True
            
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
        global select, firstSquare, lastSquare, word, wordCoord, isTrue, firstIndex
        global isFindW1, isFindW2, isFindW3, isFindW4, isFindW5, isFindW6, isFindW7, isFindW8 
        
        word = ""

        for index in range(400):

            if squares[index]["x0"] < event.x and squares[index]["x1"] > event.x and squares[index]["y0"] < event.y and squares[index]["y1"] > event.y:
                select = select + 1

                if select == 1:
                    firstSquare.append(squares[index]["x"])
                    firstSquare.append(squares[index]["y"])
                    
                    firstSquare[0] = squares[index]["x"]
                    firstSquare[1] = squares[index]["y"]
                    
                elif select == 2:
                    lastSquare.append(squares[index]["x"])
                    lastSquare.append(squares[index]["y"])
                    
                    lastSquare[0] = squares[index]["x"]
                    lastSquare[1] = squares[index]["y"]

            if select == 1 and firstSquare[0] == squares[index]["x"] and firstSquare[1] == squares[index]["y"]:
                canvas.create_rectangle(squares[index]["x0"], squares[index]["y0"], squares[index]["x1"], squares[index]["y1"], outline = "black", fill = "yellow", width=2)
                canvas.create_text(squares[index]["letterX"], squares[index]["letterY"], text=squares[index]["letter"], font=("Helvetica", 12))
                firstIndex = index

                if(isTrue == False):
                    for letter in wordCoord:
                        canvas.create_rectangle(letter["x0"], letter["y0"], letter["x1"], letter["y1"], outline = "black", fill = "white", width=2)
                        canvas.create_text(letter["letterX"], letter["letterY"], text=letter["letter"], font=("Helvetica", 12))
                
                wordCoord = []
                
            if select == 2 and lastSquare[0] == squares[index]["x"] and lastSquare[1] == squares[index]["y"]:
                fark = lastSquare[0] - firstSquare[0] if lastSquare[0] > firstSquare[0] else lastSquare[1] - firstSquare[1]
                
                if (lastSquare[0] >= firstSquare[0] and lastSquare[1] >= firstSquare[1] and (lastSquare[0] - firstSquare[0] == lastSquare[1] - firstSquare[1] or lastSquare[0] == firstSquare[0] or lastSquare[1] == firstSquare[1])):
                    if lastSquare[0] > firstSquare[0]:
                        if lastSquare[1] > firstSquare[1]:
                            durum = 2
                        else:
                            durum = 0
                    else:
                        durum = 1

                else:
                    print("You can't do that!!!")
                    durum = 3

                switch(key=durum, index=index, fark=fark)
                
                isTrue = False

                if isError != True:
                    count = 0
                    wordCoordOrder = 0

                    for searchWordList in addWord.selectedWords:
                        count = count + 1

                        if word == reverse(searchWordList[0]):
                            strollInWord(wordCoord, "green")

                            word = tk.Label(root, text=reverse(word), font=("Helvetica", 18), foreground="green")
                            
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