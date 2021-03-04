import requests
import re
from bs4 import BeautifulSoup

target = 'https://www.bqkan.com/1_1094/5403177.html'

re = requests.get(url=target)
re = re.text
html = BeautifulSoup(re)

for line in html.find_all('a'):
        if '下一章' in line:
                print (line)
                print (line.get('href'))
        
