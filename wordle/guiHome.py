# Import module
from tkinter import *
from tkinter import font 

# Home page where user inputs name and tries sends this information to playWordle where game begins

def renderGuiHome():
    from playWordle import render_playwordle
    # OPENS UP WORDLE
    def openWordle ():
        name = entry1.get().capitalize()
        tries = entry2.get()
        try:
            tries = int(tries)
            if tries > 8 or tries < 2:
                canvas1.delete("num")
                canvas1.create_text(250, 300, text = "Please input a number inbetween 2 and 8 for tries!", fill="red", font=('HelvLight',15), tag = "range")
            else:
                root.destroy()
                render_playwordle(name, tries)
        except:
            canvas1.delete("range")
            canvas1.create_text(250, 300, text = "Please input a number for tries!", fill="red", font=('HelvLight',15), tag="num")


    # INITIALIZE PAGE
    root = Tk()
    root.geometry("500x500")
    root.title("Lets play Wordle!")

    canvas1= Canvas(root, width= 500, height= 500, bg="white")

    canvas1.create_text(250, 100, text="Lets Play Wordle!", fill="black", font=('HelvLight',25, "bold"))

    canvas1.create_text(150, 150, text = "What is your name?", fill="black", font=('HelvLight',15))
    entry1 = Entry(root) 
    canvas1.create_window(325, 150, window=entry1)

    canvas1.create_text(150, 200, text = "How many tries?", fill="black", font=('HelvLight',15))
    entry2 = Entry(root) 
    entry2.config({"background": "white"})
    canvas1.create_window(325, 200, window=entry2)

    canvas1.pack()

    button1 = Button(text='Lets go!', command=openWordle)
    canvas1.create_window(250, 250, window=button1)

    # Execute tkinter
    root.mainloop()