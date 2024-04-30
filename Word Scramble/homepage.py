import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import game

frameHome = 0  # Initializing a global variable for the home frame

def disable(event):
    """
    This function is used to disable all mouse clicks on the window.
    """
    return "break"

def home(root):
    """
    This function creates the home screen of the game.

    Args:
        root (tkinter.Tk): The main Tkinter window.
    """
    global frameHome  # Accessing the global variable

    def goToGame():
        """
        Function to transition from the home screen to the game screen.
        Destroys the current home frame and runs the game.
        """
        frameHome.destroy()  # Destroying the current home frame
        game.run(root=root)  # Running the game function with the main window as an argument

    # Binding all mouse clicks to the disable function, preventing interaction with the window
    root.bind('<Button-1>', disable)

    # Creating the frame for the home screen
    frame = tk.Frame(root, relief="ridge", borderwidth=2, width=720, height=720)
    frame.pack(padx=10, pady=10)

    # Adding a title label and buttons for starting a new game or exiting
    tk.Label(frame, text="WELCOME WORD SCRAMBLE GAME!", font=("The Last Of Us Rough", 30)).place(x=175, y=50)
    tk.Button(frame, text="NEW GAME", command=goToGame, width=30, height=2).place(x=250, y=150)
    tk.Button(frame, text="EXIT", command=exit, width=30, height=2).place(x=250, y=200)

    # Storing the frame for future reference
    frameHome = frame