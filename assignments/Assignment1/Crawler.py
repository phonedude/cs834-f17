'''
Created on Sep 20, 2017

@author: nauman
'''
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import time
#url = raw_input("Enter a website to extract the URL's from: ")

url = "http://www.cs.odu.edu/~mln/"
list_of_url_to_parse = []
list_of_url_to_parse.append(url)
file_uri = open("URI_List.txt","w")

while True:
    parsed_uri = urlparse(list_of_url_to_parse[0])
    file_path = '{uri.netloc}{uri.path}'.format(uri = parsed_uri)
    file_name = file_path+".html"
    #print(file_name)
    file_name = file_name.replace('/','-')
    file = open(file_name,"w", encoding='utf-8')
    r  = requests.get(list_of_url_to_parse[0])
    list_of_url_to_parse.pop(0)
    data = r.text
    soup = BeautifulSoup(data)
    file.write(str(soup))
    file.close()
    for link in soup.find_all('a'):
        if type(link.get('href')) is str : 
            file_uri.write(link.get('href') + "\n")
            list_of_url_to_parse.append(link.get('href'))
    time.sleep(5)
    if not list_of_url_to_parse:
        file_uri.close()
        break