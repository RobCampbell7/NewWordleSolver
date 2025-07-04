from random import sample
from functions import makeGuess, minIndex, filterWordList, findWorstCase    

WORDS = []
with open("possibleAnswers.txt", "r") as guessesFile:
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

guessLookup = {}
def findWorstCase(guess, wordlist):
    worst = 0
    for potentialAnswer in wordlist:
        # try:
        #     result = guessLookup[(potentialAnswer, guess)]
        # except KeyError:
        #     guessLookup[(potentialAnswer, guess)] = makeGuess(potentialAnswer, guess)
        #     result = guessLookup[(potentialAnswer, guess)]
        result = makeGuess(potentialAnswer, guess)
        worst = max(worst, len(filterWordList(wordlist, guess, result)))
    
    return worst

def bestGuess(wordlist):
    worstCaseLen = []
    for w in wordlist:
        worstCaseLen.append(findWorstCase(w, wordlist))

    return wordlist[minIndex(worstCaseLen)]

def displayWordList(lst, lineSize = 10):
    line = []
    for w in lst:
        if len(line) > lineSize - 1:
            print(*line, sep=", ")
            line = []
        line.append(w)
    if line != []:
        print(*line, sep=", ")

def displayWordList(lst, valueLst, lineSize = 8):
    line = []
    numLen = max([len(str(x)) for x in valueLst])
    for i in range(len(lst)):
        if len(line) > lineSize - 1:
            print(*line, sep=", ")
            line = []
        line.append(("{0:5} : {1:<" + str(numLen) + "}").format(lst[i], valueLst[i]))
    if line != []:
        print(*line, sep=", ")

wordlst = WORDS
# wordlst = sample(WORDS, 50)

worstCaseLen = []
i = 0
for w in wordlst:
    i += 1
    if i % 10 == 0:
        print(str(i) + " words completed")
    worstCaseLen.append(findWorstCase(w, wordlst))
    
# bestIndex = minIndex(worstCaseLen)
# g = wordlst[bestIndex]
# gScore = worstCaseLen[bestIndex]

# wordlst = sorted(wordlst, key = lambda w : worstCaseLen[wordlst.index(w)])
# worstCaseLen.sort()

# displayWordList(wordlst, worstCaseLen)

with open("answersData.csv", "w") as dataFile:
    for i in range(len(wordlst)):
        dataFile.write("{0}, {1}\n".format(wordlst[i], worstCaseLen[i]))

# print()
# print(g + ": " + str(gScore))

if __name__=="__main__" and False:
    wordlst = WORDS
    guess = bestGuess(wordlst)
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
            # print("\nBest next guess : '" + wordlst[0].upper() + "'")
            print("\nBest next guess : '" + bestGuess(wordlst).upper() + "'")
