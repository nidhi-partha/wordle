import string
from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer
import random
from guiHome import renderGuiHome

#======
# markGuess - will "mark" the guess and the alphabet according to the word
#   word - String of word to be guessed
#   guess - WordleWord that have been guessed
#   alphabet - WordleWord of the letters a-z that have been marked
#======
def markGuess(word, guess, alphabet):
    # Check for all correct
    for i in range(5):
        if guess.charAt(i) == word[i]:
            guess.setCorrect(i)
            # Mark alphabet
            for j in range(26):
               if alphabet.charAt(j) == guess.charAt(i):
                   alphabet.setCorrect(j)
                   break
            # make it upper so it doesn't come across this again
            word = word[:i] + word[i].upper() + word[i+1:]
    
    # Check for all misplaced
    for i in range(5):
        if guess.charAt(i) in word:
            # make sure it is not already correct
            if not guess.isCorrect(i):
                guess.setMisplaced(i)
                # Mark alphabet
                for j in range(26):
                    if alphabet.charAt(j) == guess.charAt(i) :
                        if not(alphabet.isCorrect(j)):
                            alphabet.setMisplaced(j)
                            break
                # make it upper so it doesn't come across this again
                pos = word.index(guess.charAt(i))
                word = word[:pos] + word[pos].upper() + word[pos+1:]
    
    # Check for all wrong
    for i in range(5):
        if not guess.isCorrect(i) and not guess.isMisplaced(i):
            # mark alphabet if if it is not already set correct or misplaced
            for j in range(26):
                if alphabet.charAt(j) == guess.charAt(i):
                    if not alphabet.isCorrect(j) and not alphabet.isMisplaced(j):
                        alphabet.setNotUsed(j)
                        break

#======
# playRound(players, words, all_words, settings)
# Plays one round of Wordle. 
# Returns nothing, but modifies the player statistics at end of round
#
#   players - List of WordlePlayers
#   words - Wordbank of the common words to select from
#   all_words - Wordbank of the legal words to guess
#   settings - Settings of game
#======
def playRound(players, words, all_words, settings):
    alphabet = WordleWord("abcdefghijklmnopqrstuvwxyz")
    word_len = 5
    word = words.getRandom()
    # print(word)
    guesses = []
    for i in range(settings.getValue('maxguess')):
        # Input
        guess = input("Guess a "+ str(word_len)+"-letter word: ")

        # Validation
        while guess != "hint" and (len(guess) != word_len or not all_words.contains(guess)):
            print("Please guess a VALID word.")
            guess = input("Guess a "+ str(word_len)+"-letter word: ")
        
        # hint code
        if guess == "hint":
            pos = random.randint(0,4)
            won = False
            print("_"*(word_len - (word_len-pos)) + word[pos] + "_"*(word_len-pos-1))
        else:
            guess = WordleWord(guess)
            markGuess(word, guess, alphabet)
            guesses.append(guess)
            count = 1
            for g in guesses:
                print(str(count) + ":", g)
                count += 1
            print()
            # print(guess)
            print(alphabet)
            print()
            #check if game was won
            won = False
            if guess.getWord() == word:
                won = True
                print("You guessed it! Great job!")
                break

    if not won: print("Aww! Maybe next time! The word was",word+".")
    players[0].updateStats(won, i+1)



def playWordle():
    players = []
    print("Let's play the game of Wordle!")

    game = input("Do you want to play basic or GUI? ").lower()
    while game != "basic" and game != "gui":
        print("Please enter either 'gui' or 'basic'!")
        game = input("Do you want to play basic or GUI? ").lower()
    
    if game == "gui":
        renderGuiHome()
    
    else:

        playerName = input("Hi! What is your name: ")
        print("Hello,",playerName+"!","Lets play wordle!")

        # initialize WordBanks
        all_words = WordBank("words_alpha.txt")
        words = WordBank("common5letter.txt")

        # intialize settings to the baseline settings
        settings = Setting()
        settings.setSetting('wordlen', 5)
        # settings.setSetting('maxguess', int(maxGuess))
        settings.setSetting('numplayers', 1)
        settings.setSetting('difficulty', 'normal')

        # make the player
        maxGuess = input("How many chances do you want while guessing? ")
        settings.setSetting('maxguess', int(maxGuess))
        player = WordlePlayer(playerName, int(maxGuess))
        players.append(player)

        # start playing rounds of Wordle
        play_wordle = 'y'
        while play_wordle == 'y':
            playRound(players, words, all_words, settings)
            play_wordle = input("Do you want to play again? (y/n) ").lower()
            while play_wordle != 'y' and play_wordle != 'n':
                print("Please input y or n!")
                play_wordle = input("Do you want to play again? (y/n) ").lower()

        # end game by displaying player stats
        players[0].displayStats()

def main():
    playWordle()

if __name__ == "__main__":
    main()