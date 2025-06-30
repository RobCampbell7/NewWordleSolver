from random import sample
from functions import makeGuess, minIndex, filterWordList, findWorstCase    

WORDS = []
with open("possibleAnswers.txt", "r") as guessesFile:
    for li in guessesFile.readlines():
        WORDS.append(li.replace("\n", "").lower())

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

# wordlst = sample(WORDS, 50)

worstCaseLen = []
dataFile = open("answersData.csv", "w")
i = 0 # The index to start at
for w in WORDS[i:]:
    i += 1
    value = findWorstCase(w, WORDS)
    dataFile.write("{0}, {1}\n".format(w, value))
    if i % 10 == 0:
        print(str(i) + " words completed")

dataFile.close()
    
    
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

