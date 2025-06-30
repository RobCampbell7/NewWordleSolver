from functools import cache
from random import sample
from math import inf
from functions import makeGuess, minIndex, filterWordList, knownFilter 

WORDS = []
with open("possibleAnswers.txt", "r") as guessesFile:
    for li in guessesFile.readlines():
        WORDS.append(li.replace("\n", "").lower())

@cache
def wordAllowed(answer, lastGuess, newGuess):
    result = makeGuess(answer, lastGuess)
    return knownFilter(newGuess, lastGuess, result)

def displayWordList(lst, lineSize = 10):
    line = []
    for w in lst:
        if len(line) > lineSize - 1:
            print(*line, sep=", ")
            line = []
        line.append(w)
    if line != []:
        print(*line, sep=", ")

def displayWordListAndValues(lst, valueLst, lineSize = 8):
    line = []
    numLen = max([len(str(x)) for x in valueLst])
    for i in range(len(lst)):
        if len(line) > lineSize - 1:
            print(*line, sep=", ")
            line = []
        line.append(("{0:5} : {1:<" + str(numLen) + "}").format(lst[i], valueLst[i]))
    if line != []:
        print(*line, sep=", ")

def bestGuessHandler(wordlist, bestCase = inf):
    if len(wordlist) == 1:
        return 1
    elif bestCase < 2:
        return bestCase
    maxGuessNo = 0
    for guess in wordlist: 
        for potentialAnswer in wordlist:
            if potentialAnswer == guess:
                continue
            maxGuessNo = max(maxGuessNo, 1 + bestGuessHandler([w for w in wordlist if wordAllowed(potentialAnswer, guess, w)], bestCase - 1))
            if maxGuessNo >= bestCase:
                # print("'" + guess + "' disregared, " + str(maxGuessNo) + " vs " + str(bestResult))
                return maxGuessNo
    return maxGuessNo
    
def bestGuess(wordlist):
    # bestCase = inf
    bestCase = inf
    bestWord = None
    for guess in wordlist:
        maxGuessNo = 0
        for potentialAnswer in wordlist:
            if potentialAnswer == guess:
                continue
            maxGuessNo = max(maxGuessNo, bestGuessHandler([w for w in wordlist if wordAllowed(potentialAnswer, guess, w)], bestCase))
        # print(guess + " : " + str(maxGuessNo))
        if maxGuessNo < bestCase:
            bestCase = maxGuessNo
            bestWord = guess
            print("new best word: " + bestWord + " with a score of " + str(maxGuessNo))
                
    return bestWord
        
WORDS = sample(WORDS, 300)
# n = 2000
# WORDS = WORDS[n : n + 100]
WORDS.sort()

displayWordList(WORDS, 12)
print()

chosenWord = bestGuess(WORDS)
print("\nBest guess : " + chosenWord)
# worstCaseLen = []
# dataFile = open("answersData.csv", "w")
# i = 0 # The index to start at
# for w in WORDS[i:]:
#     i += 1
#     value = findWorstCase(w, WORDS)
#     dataFile.write("{0}, {1}\n".format(w, value))
#     if i % 10 == 0:
#         print(str(i) + " words completed")

# dataFile.close()
    
    
# bestIndex = minIndex(worstCaseLen)
# g = wordlst[bestIndex]
# gScore = worstCaseLen[bestIndex]

# wordlst = sorted(wordlst, key = lambda w : worstCaseLen[wordlst.index(w)])
# worstCaseLen.sort()

# displayWordList(wordlst, worstCaseLen)

# with open("answersData.csv", "w") as dataFile:
#     for i in range(len(wordlst)):
#         dataFile.write("{0}, {1}\n".format(wordlst[i], worstCaseLen[i]))

# print()
# print(g + ": " + str(gScore))

