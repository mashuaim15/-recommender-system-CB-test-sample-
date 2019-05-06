import urllib
import urllib.request
from bs4 import BeautifulSoup
import string
import pandas as pd
from rake_nltk import Rake
import numpy as np

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

        # get rid of puctuation
        s1=s.translate(str.maketrans('.', '.', string.punctuation))

       # s1=("{}{}".format(s,'.'))

        #string to list
        s2=s1.split("\n")


df = pd.DataFrame(s2,columns=['joke'])


print (s2)











