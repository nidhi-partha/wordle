from wordleword import WordleWord

# def markGuess(word, guess, alphabet):
#    # think about corner cases where there are two of the same letter
#    prev = -1
#    for i in range(5):
#        if guess.charAt(i) == word[i].lower():
#             print("hello", word, guess)
#             guess.setCorrect(i)
#             for j in range(26):
#                 if alphabet.charAt(j) == guess.charAt(i):
#                     alphabet.setCorrect(j)
#                     break
#             word = word[:i] + word[i].upper() + word[i+1:]
#        elif guess.charAt(i) in word:
#             if guess.charAt(i) == word[i]:
#                guess.setCorrect(i)
#                for j in range(26):
#                    if alphabet.charAt(j) == guess.charAt(i):
#                        alphabet.setCorrect(j)
#                        break
#             else:
#                guess.setMisplaced(i)
#                for j in range(26):
#                    if alphabet.charAt(j) == guess.charAt(i) :
#                        if not(alphabet.isCorrect(j)):
#                            alphabet.setMisplaced(j)
#                            break
#             pos = word.index(guess.charAt(i))
#             word = word[:pos] + word[pos].upper() + word[pos+1:]
#        else:
#            guess.setNotUsed(i)
#            for j in range(26):
#                if alphabet.charAt(j) == guess.charAt(i):
#                    alphabet.setNotUsed(j)
#                    break

def markGuess(word, guess, alphabet):
    # Check for all correct
    for i in range(5):
        if guess.charAt(i) == word[i]:
            guess.setCorrect(i)
            for j in range(26):
               if alphabet.charAt(j) == guess.charAt(i):
                   alphabet.setCorrect(j)
                   break
            word = word[:i] + word[i].upper() + word[i+1:]
    
    # Check for all misplaced
    for i in range(5):
        if guess.charAt(i) in word:
            if not guess.isCorrect(i):
                guess.setMisplaced(i)
                for j in range(26):
                    if alphabet.charAt(j) == guess.charAt(i) :
                        if not(alphabet.isCorrect(j)):
                            alphabet.setMisplaced(j)
                            break
                pos = word.index(guess.charAt(i))
                word = word[:pos] + word[pos].upper() + word[pos+1:]
    
    # Check for all wrong
    for i in range(5):
        if not guess.isCorrect(i) and not guess.isMisplaced(i):
            for j in range(26):
                if alphabet.charAt(j) == guess.charAt(i):
                    if not alphabet.isCorrect(j) and not alphabet.isMisplaced(j):
                        alphabet.setNotUsed(j)
                        break


word = "stalk"
alphabet = WordleWord("abcdefghijklmnopqrstuvwxyz")
guess = WordleWord("zcbdy")
markGuess(word, guess, alphabet)
print(guess)