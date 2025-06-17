WORDS = []
with open("possibleWords.txt", "r") as guessesFile:
    for li in guessesFile.readlines():
        WORDS.append(li.replace("\n", ""))

WORDSPROB = {}
N = len(WORDS)
x = 1/N
for w in WORDS:
    WORDSPROB[w] = x

# Keeping some functions from the old version, may come in handy
def normalise(x, lowerBound, upperBound):
    return (x - lowerBound) / (upperBound - lowerBound)

def maxFromDict(d):
    maxItem = None
    for item in d.keys():
        if maxItem == None or d[item] > d[maxItem]:
            maxItem = item
    return maxItem

def knownFilter(word, green=".....", yellow=".....", grey = ""):
    for i in range(5):
        if green[i] != ".":
            if word[i] == green[i]:
                word = word[:i] + "." + word[i + 1:]
            else:
                return False

    for i in range(5):
        if yellow[i] != ".":
            if word[i] == yellow[i]:
                return False
            else:
               found = False
               for j in range(5):
                   if word[j] == yellow[i]:
                       word = word[:j] + "." + word[j + 1:]
                       found = True
                       break
               if found == False:
                   return False 

    for i in range(5):
        if word[i] != "." and word[i] in grey:
            return False
    return True

def remove(string, char):
    newString = ""
    for i in range(len(string)):
        if string[i] == char:
            break
        else:
            newString += string[i]
    return newString + string[i + 1:]

if __name__=="__main__":
    wordlst = WORDS
    guess = wordlst[0]
    print("  Initial guess : '" + guess.upper() + "'")
    for i in range(5):
        green = input("  Green letters : ").lower()
        if "." not in green:
            print("success")
            break
        yellow = input(" Yellow letters : ").lower()
        grey = input("   Grey letters : ").lower().replace(", ", "").replace(" ", "")
        wordlst = [word for word in wordlst if knownFilter(word, green, yellow, grey)]
        if len(wordlst) == 0:
            print("No possible solutions")
            break
        else:
            print("\nBest next guess : '" + guess.upper() + "'")
