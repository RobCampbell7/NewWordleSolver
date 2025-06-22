from functools import cache
import random

def maxIndex(lst, ignoreIndexes=[]):
    """
    Returns the index of the maximum value in the list
    """
    indexLst = [i for i in range(len(lst)) if i not in ignoreIndexes]
    return max(indexLst, key=lst.__getitem__)

def minIndex(lst, ignoreIndexes=[]):
    """
    Returns the index of the maximum value in the list
    """
    indexLst = [i for i in range(len(lst)) if i not in ignoreIndexes]
    return min(indexLst, key=lst.__getitem__)

def maxFromDict(d):
    maxItem = None
    for item in d.keys():
        if maxItem == None or d[item] > d[maxItem]:
            maxItem = item
    return maxItem

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

@cache
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

def filterWordList(wordlist, guess, result):
    return [w for w in wordlist if knownFilter(w, guess, result)]

def findWorstCase(w1, wordlist):
    worst = 0
    for w2 in wordlist:
        result = makeGuess(w1, w2)
        worst = max(worst, len(filterWordList(wordlist, w2, result)))
    
    return worst

