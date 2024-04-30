#This file is the game's start menu.
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import game

def goToGame():
    frame.destroy()
    game.run(root=root)

def exit():
    root.destroy()

#Create a home page
root = tk.Tk()
root.geometry("1080x840")
root.title("Word Scramble")

frame = tk.Frame(root, relief="ridge", borderwidth=2, width=720, height=720)
frame.pack(padx=10, pady=10)

# Adding a title label and buttons for starting a new game or exiting
tk.Label(frame, text="WELCOME WORD SCRAMBLE GAME!", font=("The Last Of Us Rough", 30)).place(x=175, y=50)
tk.Button(frame, text="NEW GAME", command=goToGame, width=30, height=2).place(x=250, y=150)
tk.Button(frame, text="EXIT", command=exit, width=30, height=2).place(x=250, y=200)

root.mainloop()