import requests
from  bs4 import BeautifulSoup

target = "http://www.biqukan.com/1_1094/5403177.html"

def get_next(html):
        
        for line in html.find_all('a'):
                if '下一章' in line:
                        nx = line.get('href')
                        return nx
                        
                
                
        return None

i = 0

if __name__ == "__main__":
        
        print ("[*] 开始爬取.....")
        with open('txt', 'ab+') as f:
                while True:
                        
        
                        re   = requests.get(target)
                        re   = re.text
                        html = BeautifulSoup(re)
                        text = html.find_all('div',class_ = 'showtxt')
                        text = text[0].text.replace('\xa0'*8 ,'\n\n')
                        
                        
                        f.write(text.encode())
                        d = '\n\n'
                        f.write(d.encode())
        
                        i += 1
                                
                        n = get_next(html)
                        
                        
                        if i % 100 == 0:
                                print ("[*] 已爬取 %s 章...." % i)
                        
                        if n == None:
                                print ("[-] 没有内容 应该是结束了！！！")
                                print ()
                                print ("[*] 共爬取了 %s 章" % (i))
                                break
                        
                        target = "http://www.biqukan.com" + n
                f.close()
        
                
               