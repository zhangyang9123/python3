import sys
import socket

def scan(url):
        print ()
        print ("[*] 测试 %s ----------- %d " % (url,port))
        conn = socket.socket()
        conn.settimeout(1)
        try:
                conn.connect((url,port))
                print ("[*] 连接成功")
                conn.sendall(payload.encode())
                data = conn.recv(4096).decode()
                
                if data and 'redis_version' in data:
                        print ("[*] 存在漏洞")
                        conn.close()
                else:
                        print("[-] 不存在漏洞")
                        conn.close()
                
        except:
                print ("[-] 连接失败")                        
        
        return


if len(sys.argv) != 3:
        print ("python3 redis.py [ip [port]]")
        sys.exit()

txt  = sys.argv[1]
port = int(sys.argv[2])

payload = "\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a"

p = 0

with open(txt,'r') as f:
        for i in f:
                i = i.replace('\n','')
                scan(i)
f.close()
sys.exit()
