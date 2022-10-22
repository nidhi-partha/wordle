#===========================================================================
# class FancyWord
# Description: a colored word - each letter has a color attribute
#
# Methods
#    updateStats(won, tries) - 'won' - True if guessed word correctly
#                            - 'tries' - number of tries it took to guess word
#                            - This is called at the end of each game to update
#                              the game stats for this player
#    winPercentage() - returns % of how many games were won over all time
#    gamesPlayed() - returns the number of games played over all time 
#    currentStreak() - returns the current win streak; it will return 0 if
#                      the last game was lost
#    maxStreak() - returns the longest winning streak
#    displayStats() - prints out nice display of all the Wordle player stats
#    
#    Games Played: 3
#    Win %: 100.00
#    Current Streak: 3
#    Max Streak: 3
#    Guess Distribution
#      1: ########### 1
#      2: # 0                        <-- min bar length is 1
#      3: # 0
#      4: ##################### 2    <-- max bar length is 21
#      5: # 0
#      6: # 0
#=============
from player import Player
from tkinter import *
from tkinter import font
import matplotlib.pyplot as plt

class guiWordlePlayer(Player):
    def __init__(self, name ,mt):
        super().__init__(name)
        self.maxTry = mt
        self.games = 0
        self.triesPerGame = [0 for i in range(mt)]
        self.gamesWon = []
        self.currStreak = 0
        self.mStreak = 0

    def updateStats(self, won, tries):
        if tries > self.maxTry:
            won = False
        self.gamesWon.append(won)
        if won:
            self.triesPerGame[tries-1] += 1
            self.currStreak += 1
            if self.currStreak > self.mStreak:
                self.mStreak = self.currStreak
        else:
            self.currStreak = 0
        self.games += 1

    def winPercentage(self):
        return round((self.gamesWon.count(True)/len(self.gamesWon))*100)

    def gamesPlayed(self):
        return self.games

    def currentStreak(self):
        return self.currStreak

    def maxStreak(self):
        return self.mStreak
    

    
    def guiDisplayStats(self):
        displayStats = Tk()
        displayStats.title("STATS")
        displayStats.geometry("500x350")
        canvas3 = Canvas(displayStats, width= 500, height= 500, bg="white")
        canvas3.create_text(250,40, text="STATISTICS", fill="black", font=('HelvLight',20, "bold"))

        canvas3.create_text(150,90, text=str(self.gamesPlayed()), fill="black", font=('HelvLight',30))
        canvas3.create_text(150,120, text="Played", fill="black", font=('Helvetica Nue',12))

        canvas3.create_text(220,90, text=str(self.winPercentage()), fill="black", font=('HelvLight',30))
        canvas3.create_text(220,120, text="Win %", fill="black", font=('HelvLight',12))

        canvas3.create_text(290,90, text=str(self.currStreak), fill="black", font=('HelvLight',30))
        canvas3.create_text(290,120, text="Current", fill="black", font=('HelvLight',12))
        canvas3.create_text(290,135, text="Streak", fill="black", font=('HelvLight',12))

        canvas3.create_text(360,90, text=str(self.mStreak), fill="black", font=('HelvLight',30))
        canvas3.create_text(360,120, text="Max", fill="black", font=('HelvLight',12))
        canvas3.create_text(360,135, text="Streak", fill="black", font=('HelvLight',12))

        canvas3.create_text(250,175, text="GUESS DISTRIBUTION", fill="black", font=('HelvLight',18,"bold"))



        def displayGraph():

            # creates x and y of graphs
            y = []
            x = []
            for i in range(1,self.maxTry+1):
                y.append(i)
                x.append(self.triesPerGame[i-1])
            
            plt.barh(y, x, color= '#6AA964', height=0.7)
            plt.ylabel("Tries Taken")
            plt.xlabel("# of times won")

            # making sure tick marks are whole numbers
            plt.yticks(range(0,self.maxTry+1))
            plt.xticks(range(0,max(self.triesPerGame)+1))


            plt.title("Display Stats",fontweight='bold')
            plt.show()


        B = Button(displayStats, text ="View Graph", height = 5, width = 20,command = displayGraph)
        canvas3.create_window(250, 250, window=B)

        canvas3.pack()

        displayStats.mainloop()

# p = guiWordlePlayer("nidhi", 6)
# p.updateStats(True, 3)
# p.updateStats(True, 3)
# p.updateStats(True, 4)
# p.updateStats(False, 0)
# p.updateStats(True, 5)
# p.updateStats(True, 5)
# p.updateStats(True, 3)
# p.updateStats(True, 2)
# p.updateStats(False, 20)
# p.updateStats(True, 2)
# p.updateStats(True, 3)
# p.guiDisplayStats()