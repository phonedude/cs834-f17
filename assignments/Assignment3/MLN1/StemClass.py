'''
Created on Nov 9, 2017

@author: nauman
'''
from nltk.stem.porter import *
import codecs
import pickle
import os
from bs4 import BeautifulSoup
import codecs
from string import punctuation
import re

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def checkDigits(word):
	return word.isalpha()


def createPorterStemmerClass(wordlist,stem_words):
    word_frequency_matrix = []
    for i in range(0,10):
        new = [stem_words[i]]
        word_frequency_matrix.append(new)
    stemmer = PorterStemmer()
    for plural in wordlist:
	containsDigits = checkDigits(plural)
	if containsDigits:
        	stem = stemmer.stem(str(plural))
        	if stem in stem_words:
            		index = stem_words.index(stem)
            		word_frequency_matrix[index].append(plural)
    return word_frequency_matrix
 
def countCooccurence(word_frequency_matrix):
    stem_cooccurence_matrix = []
    for i in range(0,10):
        new = []
        for j in range(0,len(word_frequency_matrix[i])):
            new.append(0)
        stem_cooccurence_matrix.append(new)

    exclude = set(punctuation)
    for root, dirs, files in os.walk("F:\Fall2017\InformationRetreival\Assignment2\en"):
        for file in files:
            if file.endswith(".html"):
                with codecs.open(root+"\\" + file, "r", "utf-8") as file_open:
                    count_range = [0,0,0,0,0,0,0,0,0,0]
                    flag_wordFound = [False,False,False,False,False,False,False,False,False,False]
                    temp_word = ["","","","","","","","","",""]
                    soup = BeautifulSoup(file_open,'html.parser')
                    for words in soup.findAll(text=True):
                        if words.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
                            continue

                        s = ''.join(ch for ch in str(words) if ch not in exclude)
                        words = s.split(" ")
                        for word in words:
                            if not RepresentsInt(word.rstrip()):
                                if re.search('[a-zA-Z]', word.rstrip()):
                                    
                                    for i in range(0,10):
                                        if word.rstrip().lower() in word_frequency_matrix[i]:
                                            if count_range[i] == 0:
                                                temp_word[i] = word.rstrip().lower()
                                                flag_wordFound[i] = True
                                            elif count_range[i] < 200 and flag_wordFound[i]:
                                                index_prev = word_frequency_matrix[i].index(temp_word[i])
                                                index_next = word_frequency_matrix[i].index(word.rstrip().lower())
                                                temp = stem_cooccurence_matrix[i][index_next] 
                                                stem_cooccurence_matrix[index_prev][index_next] = temp +1
                                                temp = stem_cooccurence_matrix[i][index_prev] 
                                                stem_cooccurence_matrix[index_prev][index_prev] = temp +1
                                                temp_word[i] = word.rstrip().lower()
                                                count_range[i] = 0
                                        elif count_range < 200:
                                            count_range[i] = count_range[i] + 1
                                        else:
                                            count_range[i] = 0
					    flag_wordFound[i] = False
                        
    print("WordsOver") 
    return stem_cooccurence_matrix
      
def main():
    word_list =["canada","candidates","collections","competitive","composition","very", "couples","victoria", "weapon", "defence"]
    stemmer = PorterStemmer()
    stem_words = [stemmer.stem(plural) for plural in word_list]
    with open("word_unique.pkl", 'rb') as f:
        wordlist = pickle.load(f)
    word_frequency_matrix = createPorterStemmerClass(wordlist,stem_words) 
    file = open ("StemClass.txt", "w")
    file.write("Intital Stem Class without Co-occurence" + "\n")
    for i in range(0,10):
	file.write("Stem Class: ")
        for j in range(0,len(word_frequency_matrix[i])):
            file.write(word_frequency_matrix[i][j] + "  ")
   	file.write("\n")
    file.write("\nFinal Stem classes after considering co-occurence\n\n")
                
    stem_cooccurence_matrix = countCooccurence(word_frequency_matrix)
    for i in range(0,10):
        file.write("Stem Class \n" )
        for j in range(0,len(stem_cooccurence_matrix[i])):
            if stem_cooccurence_matrix[i][j]> 0:
                file.write(word_frequency_matrix[i][j] + "  ")
        file.write("\n")
    file.close()
                
    
     
main()
