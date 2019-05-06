#-*- coding:utf-8 -*-
import requests
from lxml import etree
import time
import urllib
import urllib.request
from bs4 import BeautifulSoup
import string
import pandas as pd


with open(r'/Users/Brian/Desktop/joke.csv','w') as F:
    for i in range(100):
        url1 = 'file:///Users/Brian/Desktop/jokes/init{}.html'.format(i+1)
        with urllib.request.urlopen(url1) as url:
         s = url.read()

         soup = BeautifulSoup(s,'html.parser')

         for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
         text = soup.get_text()

        # break into lines and remove leading and trailing space on each
         lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
         chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
         text11 = '\n'.join(chunk for chunk in chunks if chunk)
        #从第二行开始读取
         text2 = text11.splitlines()[1:]

        #transfer list to string
        s = "".join(text2)

        #去掉各种标点符号
        s1=s.translate(str.maketrans('.', '.', string.punctuation))
        s2=s1.split("\n")

        F.write("{}\n".format(s1))
        print (s1)