# Import module
from tkinter import *
from tkinter import font
import string
from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer
import random
 
def playWordle(tries, playerName):
    wordle = Toplevel(root)
    wordle.title("Wordle")
    wordle.geometry("500x500")

    players = []
    all_words = WordBank("words_alpha.txt")
    words = WordBank("common5letter.txt")
    settings = Setting()
    settings.setSetting('wordlen', 5)
    settings.setSetting('maxguess', int(tries))
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

    player = WordlePlayer(playerName, 6)
    players.append(player)

    

    # end game by displaying player stats
    players[0].displayStats()





def openWordle ():  
    playerName = entry1.get()
    tries = entry2.get()
    try:
        tries = int(tries)
        playWordle(tries, playerName)
    except:
        canvas1.create_text(250, 300, text = "Please input a number for tries!", fill="red", font=('HelvLight',15))

root = Tk()
root.geometry("500x500")
root.title("Lets play wordle!")

canvas1= Canvas(root, width= 500, height= 500, bg="white")

canvas1.create_text(250, 100, text="Lets Play Wordle!", fill="black", font=('HelvLight',25, "bold"))

canvas1.create_text(150, 150, text = "What is your name?", fill="black", font=('HelvLight',15))
entry1 = Entry(root) 
canvas1.create_window(325, 150, window=entry1)

canvas1.create_text(150, 200, text = "How many tries?", fill="black", font=('HelvLight',15))
entry2 = Entry(root) 
canvas1.create_window(325, 200, window=entry2)

canvas1.pack()


    
    # label1 = Label(root, text= float(x1)**0.5)
    # canvas.create_window(200, 230, window=label1)
    
button1 = Button(text='Lets go!', command=openWordle)
canvas1.create_window(250, 250, window=button1)

# Execute tkinter
root.mainloop()