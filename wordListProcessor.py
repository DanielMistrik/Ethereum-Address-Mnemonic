# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os
import random
import time

wordList = []
indexDict = {}
def loadWordList():
    if not os.path.exists('processedWordList.txt'):
        return
    with open('processedWordList.txt','r') as txtfile:
        words = txtfile.readlines()
        i = 0
        for word in words:
            wordList.append(word.strip('\n'))
            indexDict[word.strip('\n')]=i
            i+=1

def convertWordListToJSON():
    jsonLists = []
    for i,word in enumerate(wordList):
        tempJson = {"model": "MnemGen.wordlistentry","pk":i}
        tempJson['fields']={"word":word}
        jsonLists.append(tempJson)
    with open('processedWordList.json','w') as jsonfile:
        json.dump(jsonLists,jsonfile)

def filterWordList():
    if os.path.exists('processedWordList.txt'):
        return
    rootPath = os.getcwd()+'/RawWordList.txt'
    wordDict={}
    with open(rootPath,'r') as txtfile:
        words = txtfile.readlines()
        for word in words:
            word = word.strip('\n')
            if len(word) < 3 or len(word)>14:
                continue
            if True in [word[:i] in wordDict for i in range(5,len(word))]:
                continue
            if ' ' in word or "'" in word or "-" in word:
                continue
            wordDict[word]=1
    wordList = list(wordDict.keys())
    numerizedWords = []
    indexesToChooseFrom = list(range(len(wordList)))
    for i in range(4096):
        j = random.choice(indexesToChooseFrom)
        indexesToChooseFrom.remove(j)
        numerizedWords.append(wordList[j])

    with open('processedWordList.txt','w') as txtfile:
        for word in numerizedWords:
            txtfile.write(word.lower()+'\n')

def printOutWordList():
    if not os.path.exists('processedWordList.txt'):
        return
    with open('processedWordList.txt','r') as txtfile:
        words = txtfile.readlines()
        for word in words:
            print(word)
            time.sleep(0.3)

if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
