'''
Created on Nov 7, 2017

@author: nauman
'''
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
    
## Calculate Words in wiki small dataset
def createDictionary():
    file_write=codecs.open("word_list.txt","w","utf-8")
    exclude = set(punctuation)
    doc_count = 0
    for root, dirs, files in os.walk("F:\Fall2017\InformationRetreival\Assignment2\en"):
        for file in files:
            if file.endswith(".html"):
                with codecs.open(root+"\\" + file, "r", "utf-8") as file_open:
                    doc_count = doc_count +1
                    count = 0
                    soup = BeautifulSoup(file_open,'html.parser')
                    for words in soup.findAll(text=True):
                        if words.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
                            continue

                        s = ''.join(ch for ch in str(words) if ch not in exclude)
                        words = s.split(" ")
                        for word in words:
                            count = count+1
                            if not RepresentsInt(word.rstrip()):
                                if re.search('[a-zA-Z]', word.rstrip()):
                                    file_write.write(word.rstrip().lower())
                                    file_write.write("\n")
                                 
    file_write.close()
    print("WordsOver")
    