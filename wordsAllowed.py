from random import sample
from functions import makeGuess, knownFilter

def translateToFeedback(digits):
    string = ""
    for d in digits:
        if d == 0:
            string += "."
        elif d == 1:
            string += "Y"
        else:
            string += "G"
    return string

def incrementDigits(digits):
    if len(digits) == 0:
        return digits
    if digits[-1] < 2:
        return digits[:-1] + [1 + digits[-1]]
    else:
        return incrementDigits(digits[:-1]) + [0]

def possibleFeedback():
    i = 0
    digits = [2, 2, 2, 2, 2]
    while i < 243:
        i += 1
        digits = incrementDigits(digits)
        yield translateToFeedback(digits)

WORDS = []
with open("possibleAnswers.txt", "r") as guessesFile:
    for li in guessesFile.readlines():
        WORDS.append(li.replace("\n", "").lower())
        
WORDS = sample(WORDS, 500)
WORDS.sort()

if __name__=="__main__":
    lookup = {}
    lookupFile = open("lookupData.csv", "w")
    for feedback in possibleFeedback():
        # print("w1 = " + w1)
        for prevGuess in WORDS:
            for nextGuess in WORDS:
                # lookup[(feedback, prevGuess, nextGuess)] = knownFilter(nextGuess, prevGuess, feedback)
                # li = "({0}, {1}, {2}) = {3}".format(feedback, prevGuess, nextGuess, lookup[(feedback, prevGuess, nextGuess)])
                li = "{0}, {1}, {2}, {3}".format(feedback, prevGuess, nextGuess, knownFilter(nextGuess, prevGuess, feedback))
                # print(li)
                lookupFile.write(li + "\n")
    
    