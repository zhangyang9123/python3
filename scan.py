
##ICMP SCAN
#from scapy.all import *
#import threading
#import time

#buffer = ""

#def scan(a,b):
        
        #buffer = ""
        #for i in range(a,b):
                #ip = "192.168.0." + str(i)
                
                #re = sr1(IP(dst=ip)/ICMP(),timeout=1,verbose=0)
                
                #if re:
                        #buffer += str(ip)
                #else:
                        #pass
        
        #print (buffer)
        #return
                
#global buffer 

#buffer = ""

#def scan(ip):
        
        #re = sr1(IP(dst=ip)/TCP(flags = 'A',dport = 12345),timeout=0.5,verbose=0)
        #time.sleep(0.5)
        #if not re:
                #pass
        #else:
                #if int(re[TCP].flags) == 4:
                        #print (ip)
                #else:
                        #pass
        

#for i in range(1,150):
        #ip = "192.168.0." + str(i)

        #star = threading.Thread(target=scan,args=(ip,))
        #star.start()


#time.sleep(10)   

#for i in range(150,256):
        #ip = "192.168.0." + str(i)
        
        #star = threading.Thread(target=scan,args=(ip,))
        #star.start()



#ARP SCAN

#from scapy.all import *
#try:
        #re = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1,hwdst='00:00:00:00:00:00',pdst="192.168.0.0/24"),timeout=1)
        #print (re[0].show())
#except KeyboardInterrupt:
        #print (re.display())



# Banner
#import socket

#conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.0.6'
#port = 80
#try:
        #conn.connect((host,port))
#except Exception as err:
        #print (err)

#data = 'GET / HTTP/1.0\r\n\r\n'

#conn.sendall(data.encode())

#re = conn.recv(4096)

#print (re)





        
