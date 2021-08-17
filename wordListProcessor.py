# This script was what processed the raw oxford 5000 word dictionary into a processed word list of 4096 words

import os
import json
import random
import time

wordList = []
indexDict = {}
def loadWordList():
    """
    Function that loads the processed word list into the script variable wordList
    Source of the processed word list is processedWordList.txt
    :return: None
    """
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
    """
    Converts the word list in the wordList array into a json that can be loaded into Django models and saves it into
    the file processedWordList.json
    :return: None
    """
    jsonLists = []
    for i,word in enumerate(wordList):
        tempJson = {"model": "MnemGen.wordlistentry","pk":i}
        tempJson['fields']={"word":word}
        jsonLists.append(tempJson)
    with open('processedWordList.json','w') as jsonfile:
        json.dump(jsonLists,jsonfile)

def filterWordList():
    """
    Filters the raw word list into a processed word list and saves the contents into processedWordList.txt
    Source of raw word list is RawWordList.txt
    :return: None
    """
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
    """
    Function that slowly prints out the entire processed word list, from processedWordList.txt, in terminal
    :return: None
    """
    if not os.path.exists('processedWordList.txt'):
        return
    with open('processedWordList.txt','r') as txtfile:
        words = txtfile.readlines()
        for word in words:
            print(word)
            time.sleep(0.3)

if __name__ == '__main__':
    pass

