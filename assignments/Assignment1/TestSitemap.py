'''
Created on Sep 20, 2017

@author: nauman
'''
# Python code to create an XML sitemap.
# See http://www.sitemaps.org/protocol.php
# Place in same directory as your content and pipe output to a file.
# Assumes all content to index is in one directory.
# Written by John D. Cook, http://www.johndcook.com

import os, time
from sys import platform
def changeFrequencyValue(diff):
	change_val = ["always","hourly","daily","weekly","monthly","yearly","never"]
	diff_hour = int(diff/(1000*60*60))%24
	if diff_hour == 0:
		return change_val[0]
	elif diff_hour == 1:
		return change_val[1]
	elif diff_hour < 24:
		return change_val[2]
	elif diff_hour < (24*7):
		return change_val[3]
	elif diff_hour < (24*7*30):
		return change_val[4]
	elif diff_hour < (24*7*30*365):
		return change_val[5]
	else:
		return change_val[6]

def changeFreq(file_path):
	modified_time = os.path.getmtime(file_path)
        current_time = time.time() * 1000
	diff_time = current_time - int(modified_time) 
	return changeFrequencyValue(diff_time)
		      
# your base URL
url = "http://www.cs.odu.edu/~msiddique/"
path = "/home/msiddique/public_html/cs725/VI1/"
# file types to include in sitemap
extensions_to_keep = ['.css', '.html', '.pdf','.png'] 

print ('<?xml version="1.0" encoding="UTF-8"?>')
print ('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for file in os.listdir(path):
    # exclude proof-of-ownership files
    if file.startswith( ("google", "y_key_") ):
        continue
    file_extension = os.path.splitext(file)[1]
    if file_extension in extensions_to_keep:
	absolute_file_path = path+file
        file_mod_time = time.gmtime(os.path.getmtime(absolute_file_path))
        utc = time.strftime("%Y-%m-%dT%H:%M:%SZ", file_mod_time)
	changeFreq(absolute_file_path)
        print ("    <url>")
        print ("        <loc>%s%s</loc>" % (url, file))
        print ("        <lastmod>%s</lastmod>" % utc)
	print ("        <changefreq>%s</changefreq>"% changeFreq(absolute_file_path))
        print ("    </url>")
        
print ("</urlset>")

