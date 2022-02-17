"""第三章"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import time


url = "http://python.org"
html = urlopen(url)
time.sleep(5)
bsobj = BeautifulSoup(html, 'html.parser')
for link in bsobj.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
