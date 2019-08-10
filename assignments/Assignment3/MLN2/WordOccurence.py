'''
Created on Nov 9, 2017

@author: nauman
'''
import os
from bs4 import BeautifulSoup
import codecs
from string import punctuation
import re
import math

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
def findWordOccurence(word_list):
    ####Create a 2D matrix for word frequency
    word_frequency_matrix = []
    for i in range(0,10):
        new = []
        for j in range(0,10):
            new.append(0)
        word_frequency_matrix.append(new)

    exclude = set(punctuation)
    for root, dirs, files in os.walk("F:\Fall2017\InformationRetreival\Assignment2\en"):
        for file in files:
            if file.endswith(".html"):
                with codecs.open(root+"\\" + file, "r", "utf-8") as file_open:
                    count_range = 0
                    flag_wordFound = False
                    soup = BeautifulSoup(file_open,'html.parser')
                    for words in soup.findAll(text=True):
                        if words.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
                            continue

                        s = ''.join(ch for ch in str(words) if ch not in exclude)
                        words = s.split(" ")
                        for word in words:
                            if not RepresentsInt(word.rstrip()):
                                if re.search('[a-zA-Z]', word.rstrip()):
                                    
                                    if word.rstrip().lower() in word_list and count_range == 0:
                                        flag_wordFound = True
                                        temp_word = word.rstrip().lower()
                                    elif word.rstrip().lower() in word_list and count_range <= 5:
                                        index_temp = word_list.index(temp_word)
                                        index_next = word_list.index(word.rstrip().lower())
                                        temp_frequency = word_frequency_matrix[index_temp][index_next]
                                        word_frequency_matrix[index_temp][index_next] = temp_frequency+1
                                        count_range = 0
                                        temp_word = word.rstrip().lower()
                                    elif count_range < 5 and flag_wordFound:
                                        count_range = count_range+1
                                    else:
                                        flag_wordFound = False
                                        count_range  = 0
                         
    print("WordsOver")
    return word_frequency_matrix

def findDiceCoefficient(word_frequency_matrix, word_frequency_list):
    dice_coefficient = []
    for i in range(0,len(word_frequency_list)-1):
        for j in range (i+1,len(word_frequency_list)): 
            dice_temp = (word_frequency_matrix[i][j] +word_frequency_matrix[j][i] )/(word_frequency_list[i]+word_frequency_list[j]) 
            dice_coefficient.append(dice_temp)
    return dice_coefficient

def findMutualInforamtion(word_frequency_matrix, word_frequency_list):
    mim = []
    for i in range(0,len(word_frequency_list)-1):
        for j in range (i+1,len(word_frequency_list)): 
            mim_temp = (word_frequency_matrix[i][j] +word_frequency_matrix[j][i] )/(word_frequency_list[i]*word_frequency_list[j]) 
            mim.append(mim_temp)
    return mim

def findExpectedMutualInforamtion(word_frequency_matrix, word_frequency_list, N):
    emim = []
    for i in range(0,len(word_frequency_list)-1):
        for j in range (i+1,len(word_frequency_list)):
            nab = word_frequency_matrix[i][j] +word_frequency_matrix[j][i]
            if nab>0:
                emim_temp = nab* math.log((N*(nab/(word_frequency_list[i]*word_frequency_list[j])))) 
            else:
                emim_temp = 0
            emim.append(emim_temp)
    return emim
    
def findChiSquare(word_frequency_matrix, word_frequency_list, N):
    chi_square = []
    for i in range(0,len(word_frequency_list)-1):
        for j in range (i+1,len(word_frequency_list)):
            nab = word_frequency_matrix[i][j] +word_frequency_matrix[j][i]
            x = nab-((word_frequency_list[i]*word_frequency_list[j])/N)
            chi_square_temp =  math.pow(x,2)/ (word_frequency_list[i]*word_frequency_list[j])
            chi_square.append(chi_square_temp)
    return chi_square

def main():
    N = 3902115
    word_frequency_list = [1090,106,105,104,104,1062,108,510,100,210] 
    word_list =["canada","candidates","collections","competitive","composition","very", "couples","victoria", "weapon", "defence"]
    word_frequency_matrix = findWordOccurence(word_list)
    
    for i in range(0,10):
        for j in range(0,10):
            print(word_frequency_matrix[i][j])
    diceCoefficient = findDiceCoefficient(word_frequency_matrix, word_frequency_list)
    mim = findMutualInforamtion(word_frequency_matrix, word_frequency_list)
    emim = findExpectedMutualInforamtion(word_frequency_matrix, word_frequency_list, N)
    chiSquare = findChiSquare(word_frequency_matrix, word_frequency_list, N)
    file = open("Result.txt", "w")
    file.write("Query Term1"+ " " + "Query Term2" + " " + "Dice Coefficient" + " " +"MIM" + " " + "EMIM" + " " + "Chi-Square" + "\n")
    count  =0;
    for i in range(0,len(word_list)-1):
        for j in range (i+1,len(word_list)):
            file.write(word_list[i] + " " + word_list[j] + " " + str(diceCoefficient[count]) + " " + str(mim[count]) + " " + str(emim[count]) + " " + str(chiSquare[count]) + "\n")
            count = count+1
    file.close()
    print("End")

main()