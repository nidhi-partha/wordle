# Import modules
from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
from wordbank import WordBank
# from wordleplayer import WordlePlayer
from guiwordleplayer import guiWordlePlayer
import time


# RENDERS ALL OF PLAYWORDLE
def render_playwordle(name, tries):

    # Initialize all variables as global so that it can be accessed in all functions
    # This is necessary due to the fact there are cannot be parameters in functions (when called from a button) and the variables are all objects
    global count
    global words
    global all_words
    global word
    global stringVars
    global alphabetText
    count = 0
    words = WordBank("common5letter.txt")
    all_words = WordBank("words_alpha.txt")
    word = words.getRandom()
    print(word)
    player = guiWordlePlayer(name, tries)

    # reset() resets the canvas for second, third, fourth... games
    def reset():
        global stringVars
        global word
        global count
        global img, resized_image, new_image
        global alphabetText
        play_again.destroy()
        canvas2.delete("all")
        count = 0
        stringVars = [[StringVar() for i in range(5)] for i in range(tries)]
        img= (Image.open("wordleLIGHTMODE.png"))
        resized_image= img.resize((115,40), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        canvas2.create_image(355-115/2,30, anchor=NW, image=new_image)
        canvas2.create_line(0,75,710,75,fill="#D3D6DA",width=1)
        canvas2.create_text(355, 100, text="Hi, " + name + "! You have " + str(tries) + " tries to guess the word!", fill="black", font=('HelvLight',15))
        word = words.getRandom()
        print(word)
        canvas2.create_line(0,675,710,675,fill="#D3D6DA",width=1)
        alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split()
        alphabetText = []
        for i in range(26):
            alphabetText.append(canvas2.create_text(40 + i*25, 720, text=alphabet[i], fill="black", font=('HelvLight',20, "bold")))
        createRow(0)
    
    # stop() ends the game and displays stats
    def stop():
        # player.displayStats()
        wordle.destroy()
        play_again.destroy()
        player.guiDisplayStats()


    # playAgain prompts the user if they want to play again
    def playAgain(pos, result, color):
        global play_again
        play_again = Tk()
        play_again.title("Play Again?")
        play_again.geometry("500x350")
        play_again_canvas = Canvas(play_again, width= 500, height= 350, bg="white")
        play_again_canvas.create_text(250, 100, text="You "+ result + "!" + " The word was " + word + ".", fill=color, font=('HelvLight',30))
        play_again_canvas.create_text(250, 150, text="Do you want to play again?", fill="black", font=('HelvLight',15))
        yes = Button(play_again, text='Yes', bg = "green", command=reset)
        play_again_canvas.create_window(195, 200, height=30, width=100, window=yes)
        no = Button(play_again, text='No', command=stop)
        play_again_canvas.create_window(315, 200, height=30, width=100, window=no)
        play_again_canvas.pack()
        play_again.mainloop()

    # Creates alphabet_colors which will be used in markguess to check if a word is already correct or misplaced
    global alphabet_colors
    alphabet_colors = ["" for i in range(26)]
    # MARKS GUESS CHECKS IF RIGHT OR WRONG AND MOVES ON TO NEXT ROW
    def markGuess():
        global count
        global word
        global alphabet_colors
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        w = word
        count+=1

        char1.config(fg="white")
        char2.config(fg="white")
        char3.config(fg="white")
        char4.config(fg="white")
        char5.config(fg="white")

        chars = [char1, char2, char3, char4, char5]

        guess = (char1.get() + char2.get() + char3.get() + char4.get() + char5.get()).lower()
        guess_colors = ["" for i in range(5)]
        
        # Check for all correct
        for i in range(5):
            if guess[i] == w[i]:
                chars[i].config({"background": "#538D4E"}) # make it green
                guess_colors[i] = "g"
                for j in range(26):
                    if alphabet[j] == guess[i]:
                        alphabet_colors[j] = "g"
                        canvas2.itemconfig(alphabetText[j],fill='#538D4E')
                        break
                w = w[:i] + w[i].upper() + w[i+1:]
        
        # Check for all misplaced
        for i in range(5):
            if guess[i] in w:
                if guess_colors[i] != "g":
                    chars[i].config({"background": "#C9B458"}) #make it yellow
                    guess_colors[i] = "y"
                    for j in range(26):
                        if alphabet[j] == guess[i] :
                            if alphabet_colors[j] != "g":
                                alphabet_colors[j] = "y"
                                canvas2.itemconfig(alphabetText[j],fill='#B49F3A')
                                break
                    pos = w.index(guess[i])
                    w = w[:pos] + w[pos].upper() + w[pos+1:]
        
        # Check for all wrong
        for i in range(5):
            if guess_colors[i] != "g" and guess_colors[i] != "y":
                chars[i].config({"background": "#787C7E"})
                for j in range(26):
                    if alphabet[j] == guess[i]:
                        if alphabet_colors[j] != "g" and alphabet_colors[j] != "y":
                            alphabet_colors[j] = "b"
                            canvas2.itemconfig(alphabetText[j],fill='#9fa4a6')
                            break
        
        if word == guess:
            player.updateStats(True, count)
            playAgain(count+1, "won", "green")
        elif count < tries:
            createRow(count)
        else:
            player.updateStats(False, count)
            time.sleep(1)
            playAgain(count+1, "lost", "red")

    # VALIDATES WORDS
    def validate(event):
        guess = char1.get() + char2.get() + char3.get() + char4.get() + char5.get()
        if (all_words.contains(guess.lower()) or words.contains(guess.lower())) and len(guess) == 5:
            canvas2.delete("validate")
            markGuess()
        else:
            x = canvas2.create_text(355, 160+(count+1)*65, text="Please type a valid word", fill="red", font=('HelvLight',15), tag = "validate")
        
        
    # THESE FUNCTIONS capitalize the characters (caps1 --> char1.. etc.) They also move the cursor to the next value 
    def caps1(event):
        stringVars[count][0].set(stringVars[count][0].get().upper())
        char2.focus_set()
    def caps2(event):
        stringVars[count][1].set(stringVars[count][1].get().upper())
        char3.focus_set()
    def caps3(event):
        stringVars[count][2].set(stringVars[count][2].get().upper())
        char4.focus_set()
    def caps4(event):
        stringVars[count][3].set(stringVars[count][3].get().upper())
        char5.focus_set()
    def caps5(event):
        stringVars[count][4].set(stringVars[count][4].get().upper())
    
    # This code only allows one character in each box
    def char_limit1(char1):
        if len(char1.get()) > 1:
            stringVars[count][0].set(char1.get()[0])
    
    def char_limit2(char2):
        if len(char2.get()) > 1:
            stringVars[count][1].set(char2.get()[0])
    
    def char_limit3(char3):
        if len(char3.get()) > 1:
            stringVars[count][2].set(char3.get()[0])
    
    def char_limit4(char4):
        if len(char4.get()) > 1:
            stringVars[count][3].set(char4.get()[0])
    
    def char_limit5(char5):
        if len(char5.get()) > 1:
            stringVars[count][4].set(char5.get()[0])

    # CREATE ENVIRONMENT
    wordle = Tk()
    wordle.title("Wordle")
    wordle.geometry("710x765")
    stringVars = [[StringVar() for i in range(5)] for j in range(tries+1)]
    canvas2 = Canvas(wordle, width= 710, height= 765, bg="white")

    img= (Image.open("wordleLIGHTMODE.png"))
    resized_image= img.resize((115,40), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    canvas2.create_image(355-115/2,30, anchor=NW, image=new_image)

    canvas2.create_line(0,75,710,75,fill="#D3D6DA",width=1)

    canvas2.create_text(355, 100, text="Hi, " + name + "! You have " + str(tries) + " tries to guess the word!", fill="black", font=('HelvLight',15))

    # CREATE ALPHABET DISPLAYED ON THE BOTTOM

    canvas2.create_line(0,675,710,675,fill="#D3D6DA",width=1)
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split()
    alphabetText = []
    for i in range(26):
        alphabetText.append(canvas2.create_text(40 + i*25, 720, text=alphabet[i], fill="black", font=('HelvLight',20, "bold")))
    

    # Creats row of entries where user can input their word
    def createRow(i):
        global char1
        global char2
        global char3
        global char4
        global char5

        char1 = Entry(wordle, font=('HelvLight',25, "bold"),fg="black",justify='center', textvariable=stringVars[i][0], highlightthickness=1) 
        char1.bind("<KeyRelease>", caps1)
        char1.bind('<Return>', validate)
        stringVars[i][0].trace("w", lambda *args: char_limit1(char1))
        canvas2.create_window(225, 160+i*65, height=60, width=60, window=char1)


        char2 = Entry(wordle, font=('HelvLight',25, "bold"),fg="black",justify='center', textvariable=stringVars[i][1], highlightthickness=1) 
        char2.bind("<KeyRelease>", caps2)
        char2.bind('<Return>', validate)
        stringVars[i][1].trace("w", lambda *args: char_limit2(char2))
        canvas2.create_window(290, 160+i*65, height=60, width=60, window=char2)

        char3 = Entry(wordle, font=('HelvLight',25, "bold"),fg="black",justify='center', textvariable=stringVars[i][2], highlightthickness=1) 
        char3.bind("<KeyRelease>", caps3)
        char3.bind('<Return>', validate)
        stringVars[i][2].trace("w", lambda *args: char_limit3(char3))
        canvas2.create_window(355, 160+i*65, height=60, width=60, window=char3)

        char4 = Entry(wordle, font=('HelvLight',25, "bold"),fg="black",justify='center', textvariable=stringVars[i][3], highlightthickness=1) 
        char4.bind("<KeyRelease>", caps4)
        char4.bind('<Return>', validate)
        stringVars[i][3].trace("w", lambda *args: char_limit4(char4))
        canvas2.create_window(420, 160+i*65, height=60, width=60, window=char4)

        char5 = Entry(wordle, font=('HelvLight',25, "bold"),fg="black",justify='center', textvariable=stringVars[i][4], highlightthickness=1) 
        char5.bind("<KeyRelease>", caps5)
        char5.bind('<Return>', validate)
        stringVars[i][4].trace("w", lambda *args: char_limit5(char5))
        canvas2.create_window(485, 160+i*65, height=60, width=60, window=char5)

    # CREATE FIRST ROW
    createRow(0)




    canvas2.pack()

    wordle.mainloop()
# render_playwordle("Nidhi",6)