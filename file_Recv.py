import os
import socket
import struct
import threading

def list(conn):
        fileInfo = conn.recv(struct.calcsize('128sl'))
        if fileInfo:
                fileName, fileSize = struct.unpack('128sl',fileInfo)
                fileName = fileName.decode().strip('\00')
                print ("[*] File Name {} Size: {}".format(fileName,fileSize))
        try:
                with open(fileName,'w+') as f:
                        buffer = ""
                        size   = 0
                        while size != fileSize:
                                data    = conn.recv(1024).decode()
                                buffer += data
                                size   += len(data)
                        f.write(buffer)
                        f.close()
                        print ("[*] File Write END {}".format(data))                                

        except Exception as e:
                print (e)
        
        return
        


ip   = '127.0.0.1'
port = 7001

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.bind((ip,port))
conn.listen(1)

while True:
        c,opts = conn.accept()
        print ("[*] {}:{} Success!!!".format(opts[0],opts[1]))
        t = threading.Thread(target=l,args=(c,))
        t.start()