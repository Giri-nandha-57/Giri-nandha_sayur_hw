# the question is there will be an input string and we need to find if the letters in the string can be 
# used to form one of the words in the given list of words

# eg: List = ["we", "doctor","and", "nurse", "are"]
# given input string 
# input = "wearenurseandoctor"
# output = False 
# input = "wearenurseanddoctor"
# output = true

# my approach 
# -> use dictionary to assign the count of the letters in the respective lists to separate variables
# -> compare the no of occurences of letters on both the lists
# -> if the letters and the no of occurences matches then return TRUE or else FALSE

ListOfWords = ["we", "doctor","and", "nurse", "are"]

letterList = list("wearenurseandoctor")

wordList = []

for i in ListOfWords:
    for j in i:
        wordList.append(j)

letterDict = {}
wordDict = {}

def countFunc(letter, occured, lst):
    for i in lst:
        if letter == i:
            occured += 1
        else:
            continue
    return occured

for i in letterList:
    count = 0
    count = countFunc(i, count, letterList)
    letterDict[i] = count

for i in wordList:
    count=0
    count = countFunc(i, count, wordList)
    wordDict[i] = count

def match():
    for i in letterDict:
        if letterDict[i] == wordDict[i]:
            continue
        else:
            return False
    return True
        
result = match()
if result:
    print(True)
else:
    print(False)