import urllib
import urllib.request
from bs4 import BeautifulSoup
import string

with urllib.request.urlopen("file:///Users/Brian/Desktop/jokes/init1.html") as url:
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
text1 = '\n'.join(chunk for chunk in chunks if chunk)



print(text1)
