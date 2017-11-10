'''
Created on Nov 7, 2017

@author: nauman
'''
import pickle
import codecs

def countWordFrequency():
    file = codecs.open("word_list.txt","r","utf-8")
    file_unique = open("word_unique.pkl", "w")
    file_frequency = open("word_frequency.pkl","w")
    word = []
    frequency_word = []
    for line in file:
        if line in word:
            index = word.index(line)
            temp = frequency_word[index] 
            frequency_word[index] = (temp+1)
        else:
            word.append(line.rsplit())
            frequency_word.append(1)
	    print(line)
    file.close()
    file_unique.write(pickle.dumps(word))
    file_frequency.write(pickle.dumps(frequency_word))
    file_unique.close()
    file_frequency.close()        

#countWordFrequency()

def writeToList():
    file_unique = open("word_unique.pkl", "w")
    file_frequency = open("word_frequency.pkl","w")
    file_word = open("word_list_unique_.txt","r")
    file_frequency1 = open("word_list_unique_frequency.txt", "r")
    word = []
    frequency = []
    for line in file_word:
       	word.append(line.rstrip())
    for line in file_frequency1:
	frequency.append(line)
    file_unique.write(pickle.dumps(word))
    file_frequency.write(pickle.dumps(frequency))
    file_unique.close()
    file_frequency.close()     
	
writeToList()
