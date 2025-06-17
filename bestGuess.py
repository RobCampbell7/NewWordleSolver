import random

def bestGuess(wordlist):
    """
    PLACEHOLDER - TODO
    """
    return random.choice(wordlist)
    
def maxFromDict(d):
    maxItem = None
    for item in d.keys():
        if maxItem == None or d[item] > d[maxItem]:
            maxItem = item
    return maxItem

def makeGuess(answer, guess):
    green = ""
    yellow = ""
    grey = ""
    for i in range(5):
        if answer[i] == guess[i]:
            green += answer[i]
        else:
            green += "."
        if guess[i] not in answer:
            grey += guess[i]
    lettersToFind = [answer[i] for i in range(5) if green[i] == "."]
    for i in range(5):
        if green[i] == "." and guess[i] in lettersToFind:
            yellow += guess[i]
            lettersToFind.remove(guess[i])
        else:
            yellow += "."
    return green, yellow, grey

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