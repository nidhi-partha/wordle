#===========================================================================
# Description: WordleWord(word)
# Inherits from the FancyWord class and adds methods for the Wordle game
#
# Methods
#    isCorrect(pos) - boolean - return True if character at pos is correct
#    isMisplaced(pos) - boolean - return True if character at pos is misplaced
#    isNotUsed(pos) - boolean - return True if character at pos is not in word
#    setCorrect(pos) - integer - set character are pos correct and colors accordingly
#    setMisplaced(pos) - integer - set character are pos misplaced and colors accordingly
#    setNotUsed(pos) - integer - set character are pos misplaced and colors accordingly
#===========================================================================
from curses import COLOR_GREEN, COLOR_RED, COLOR_YELLOW
from fancyword import FancyWord

class WordleWord(FancyWord):
    def isCorrect(self, pos):
        return self.colorAt(pos) == "green"

    def isMisplaced(self, pos):
        return self.colorAt(pos) == "yellow"
    
    def isNotUsed(self, pos):
        return self.colorAt(pos) == "gray"
    
    def setCorrect(self, pos):
        self.setColorAt(pos, "green")
    
    def setMisplaced(self, pos):
        self.setColorAt(pos, "yellow")

    def setNotUsed(self, pos):
        self.setColorAt(pos, "gray")