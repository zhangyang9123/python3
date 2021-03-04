import requests

headers = {
        "User-Agent": "mozilla/5.0"
        }

url = input("[*] URL: ")
txt = input("[*] TXT: ")

url_list = []
if txt == "":
        txt = "php.txt"
try:
        with open(txt,'r') as f:
                for a in f:
                        a = a.replace('\n','')
                        url_list.append(a)
                f.close()
except:
        print ("\033[5;1;1m[-]打开文件错误\033[0m")

for li in url_list :
        conn = "https://" + url + "/" + li
        
        try:
                res = requests.get(conn,headers = headers)
                print ("[*] %s-------%s" % (conn,res))
        except e:
                print ("[-] %s-------%s" % (conn,e.code))
        url_list
