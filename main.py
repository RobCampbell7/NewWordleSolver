from functions import makeGuess, minIndex, filterWordList, findWorstCase    

WORDS = []
with open("possibleWords.txt", "r") as guessesFile:
    for li in guessesFile.readlines():
        WORDS.append(li.replace("\n", "").lower())

def resultInput():
    result = ""
    valid = False
    chars = ("G", "Y", ".")
    while not valid:
        valid = True
        result = input("Enter the result : ").upper()
        if len(result) > 5:
            print("Invalid input")
        else:
            for c in result:
                if c not in chars:
                    print("Invalid input")
                    valid = False
                    break
    return result

def guessInput():
    guess = ""
    valid = False
    chars = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    while not valid:
        valid = True
        guess = input("Enter your guess : ").lower()
        if len(guess) > 5:
            print("Invalid input")
        else:
            for c in guess:
                if c not in chars:
                    print("Invalid input")
                    valid = False
                    break
    return guess

def bestGuess(wordlist):
    worstCaseLen = []
    for w in wordlist:
        worstCaseLen.append(findWorstCase(w, wordlist))

    return wordlist[minIndex(worstCaseLen)]

guessResults = {}
for w1 in WORDS:
    for w2 in WORDS:
        guessResults[(w1, w2)] = makeGuess(w1, w2)

if __name__=="__main__":
    wordlst = WORDS
    guess = wordlst[0]
    # guess = bestGuess(wordlst)
    print("  Initial guess : '" + guess.upper() + "'")
    for i in range(5):
        guess = guessInput()
        result = resultInput()
        wordlst = filterWordList(wordlst, guess, result)
        if len(wordlst) == 0:
            print("No possible solutions")
            break
        else:
            print("\nBest next guess : '" + wordlst[0].upper() + "'")
            # print("\nBest next guess : '" + bestGuess(wordlst).upper() + "'")
