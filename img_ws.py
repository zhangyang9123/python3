import requests
from bs4 import BeautifulSoup

headers = {
        'Host': 'hdqwalls.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Cookie': '__cfduid=dad63bc6758ac038914d3a5856c51369f1614068671; _ga=GA1.2.1168125514.1614068674; _gid=GA1.2.1429686340.1614068674; __gads=ID=7cab7054f6be45d5-2249862521c6005b:T=1614068674:RT=1614068674:S=ALNI_MbUq8pLLK20nPm7x7kGJZHgCpPJHA; PHPSESSID=e2abc0be3f1d715dbcc9ec6e2ef2d71c',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'        
          }

data = requests.get('https://hdqwalls.com/popular-wallpapers/page/16',headers=headers)
data = data.text
html = BeautifulSoup(data)

print (html)






#url  = "https://images.hdqwalls.com/wallpapers/anime-landscape-waterfall-cloud-5k-mq.jpg"

#name = url.split('/')[4]

#img  = requests.get(url,headers=headers).content


#with open("%s" % name, "wb") as f:
        #f.write(img)
        



