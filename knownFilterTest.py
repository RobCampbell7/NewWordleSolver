
def letterCount(letter, string):
    count = 0
    for c in string:
        if letter == c:
            count += 1
    return count

def removeFirst(item, lst):
    newLst = []
    for i in range(len(lst)):
        if item == lst[i]:
            return newLst + lst[i + 1:]
        else:
            newLst.append(lst[i])
    return newLst

def makeGuess(answer, guess):
    res = ""
    foundYellows = {}
    for c in answer:
        try:
            foundYellows[c] += 1
        except KeyError:
            foundYellows[c] = 1
    for i in range(5):
        if answer[i] == guess[i]:
            foundYellows[guess[i]] -= 1
            res += "G"
        elif guess[i] in answer:
            if foundYellows[guess[i]] > 0:
                res += "Y"
                foundYellows[guess[i]] -= 1
            else:
                res += "."
        else:
            res += "."
    return res

def knownFilter(word, guess, result):
    remaining = list(word)
    for i in range(5):
        if result[i] == "G":
            if word[i] != guess[i]:
                return False
        elif result[i] == "Y":
            if guess[i] == word[i]:
                return False
            elif guess[i] in remaining:
                remaining = removeFirst(guess[i], remaining)
            else:
                return False
        else:
            if guess[i] in remaining:
                return False
            
    return True

# assert knownFilter("FIGGY", "BLADE", ".GGGG")
# assert knownFilter("GLADE", "CUNTS", "GGGGG")
# assert knownFilter("ABEAT", "CUNTS", ".....")
# assert knownFilter("GLADE", "DREAM", "Y.YY.")
# assert knownFilter("GLADE", "BLADE", ".GGGG")

assert knownFilter("GHOST", "BLADE", ".GGGG")

# WORDS = []
# with open("possibleWords.txt", "r") as guessesFile:
#     for li in guessesFile.readlines():
#         WORDS.append(li.replace("\n", "").upper())

# wordlst = [word for word in WORDS if knownFilter(word, "BLADE", ".GGGG")]
# print(wordlst)