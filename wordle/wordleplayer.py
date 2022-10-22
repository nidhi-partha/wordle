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
# from tkinter import *
# from tkinter import font

class WordlePlayer(Player):
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

    def displayStats(self):
        print("Games Played:", self.gamesPlayed())
        print("Win %:",str(self.winPercentage())+"%")
        print("Current Streak:",self.currStreak)
        print("Max Streak:", self.mStreak)
        print("Guess Distribution")
        maxTries = max(self.triesPerGame)
        for i in range(1,self.maxTry+1):
            if maxTries == self.triesPerGame[i-1] and maxTries != 0:
                print(str(i)+":", "#" + "#"*20, self.triesPerGame[i-1])
            elif maxTries == 0:
                print(str(i)+":","#")
            else:
                print(str(i)+":", "#" + "#"*((20 * self.triesPerGame[i-1])//maxTries), self.triesPerGame[i-1])

# p = WordlePlayer("Mark", 6)
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
# p.displayStats()