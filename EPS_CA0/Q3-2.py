
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import math
class BagOfWords:
    def __init__(self, word):
        self.word = word
        self.spam_count = 0
        self.non_spam_count = 0

def get_word(word, BoW_dict):
    if word in BoW_dict:
        return BoW_dict[word]
    new_item = BagOfWords(word)
    BoW_dict[word] = new_item
    return new_item

def deletePunctuation(string):
    pattern = r'[^\w\s]'
    return re.sub(pattern, '', string)

def preAnalyse(listEmail):
    for i in range(len(listEmail)):
        listEmail[i][0] = listEmail[i][0].lower()
        listEmail[i][0] = deletePunctuation(listEmail[i][0])

def createBoW(train, BoW_dict):
    for email, label in train:
        words = email[0].split()
        for word in words:
            theWord = get_word(word, BoW_dict)
            if label == 1: 
                theWord.spam_count += 1
            else:  
                theWord.non_spam_count += 1

def calculateNumOfSpams(test):
    counter = 0
    for i in range(len(test)):
        if test[i][1] == 1:
            counter += 1
    return counter

def calculateNumOfReals(test):
    counter = 0
    for i in range(len(test)):
        if test[i][1] == 0:
            counter += 1
    return counter

def calculateAccuracy(finalLables,test):
    counter=0
    for i in range(len(test)):
        if(test[i][1]==finalLables[i]):
            counter+=1
    return counter/len(test)
def calculateProbilities(XI, y, test, numOfReals, numOfSpams):
    p_y = None
    p_XI = None
    alpha = 1

    if y == 0:
        p_y = math.log(numOfReals / len(test))
        p_XI = math.log((XI.non_spam_count + alpha) / (numOfReals))
    else:
        p_y = math.log(numOfSpams / len(test))
        p_XI =math.log( (XI.spam_count + alpha) / (numOfSpams))
    
    return p_XI + p_y


BoW_dict = {}
emails = pd.read_csv("emails.csv")
listEmail = emails.values.tolist()
preAnalyse(listEmail)
train, test = train_test_split(listEmail, test_size=0.4)
createBoW(train, BoW_dict)
numOfReals = calculateNumOfReals(test)
numOfSpams = calculateNumOfSpams(test)
finalLables = []
finalProb0=1
finalProb1=1
vocab_size = len(BoW_dict)
for email in test:
    finalProb0=1
    finalProb1=1
    words = email[0].split()
    for word in words:
        theWord = get_word(word, BoW_dict)
        finalProb0+=calculateProbilities(theWord, 0, test, numOfReals, numOfSpams)
        finalProb1+=calculateProbilities(theWord, 1, test, numOfReals, numOfSpams)
    if(finalProb1>finalProb0):
        finalLables.append(1)
    else:
        finalLables.append(0)
print(calculateAccuracy(finalLables,test))