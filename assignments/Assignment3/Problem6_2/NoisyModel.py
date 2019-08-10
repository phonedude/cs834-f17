'''
Created on Nov 7, 2017

@author: nauman
'''

from EditDistance import editDistDP
from WordList import createDictionary
from WordFrequency import countWordFrequency
import pickle
from decimal import *

## Check for words that start with same capital letter
def getCorrectWord(word):
    getcontext().prec = 28
    suggestionList = []
    probability_list = []
    with open('word_unique.pkl', 'rb') as f:
        wordlist = pickle.load(f)
    with open('word_frequency.pkl', 'rb') as f:
        frequency = pickle.load(f)
    for i in range(0, len(wordlist)):
        if checkLength(wordlist[i], word) and wordlist[i][:1] == word[:1]:
            editDistance = editDistanceCalculator(wordlist[i],word)
            if editDistance == 1:
                probability = Decimal(int(frequency[i]))/Decimal(3902115* 0.6)
		suggestionList.append(wordlist[i])
		probability_list.append(probability)
            elif editDistance == 2:
		probability = Decimal(int(frequency[i]))/Decimal(3902115* 0.2)
                suggestionList.append(wordlist[i])
		probability_list.append(probability)
	    elif editDistance == 0:
		print(wordlist[i])
		exit(1)
    
    maximum_probability = max(probability_list)
    index = probability_list.index(maximum_probability)
    print(suggestionList[index]) 
            
## Check for words than that are in length of +1 and -1
 
def editDistanceCalculator(str1,str2):
    editDistance = editDistDP(str1, str2,len(str1) , len(str2))
    return editDistance
 
def checkLength(word1,word2):
    len1 = len(word1)
    len2 = len(word2)
    if len1 == len2 or (len1 - len2) ==1 or (len2 - len1) == 1:
        return True
    else:       
        return False

def main():
    createDictionary()
    countWordFrequency()
    getCorrectWord("collectionz")
    
    
main()
    
