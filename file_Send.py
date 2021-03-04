import os
import socket
import struct

ip   = '127.0.0.1'
port = 7001 

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
        conn.connect((ip,port))
        print ("[*] Lian jie Sucess!!!")
except Exception as e:
        print (e)

file = input("[+] Input File dir: ")

try:
        f = open(file,'r')
        f.close()
except:
        print ("[-] Open file Falied!!!")

fileInfo = struct.pack('128sl',bytes(os.path.basename(file).encode('utf-8')),os.stat(file).st_size)
print ("[*] File Name: {} ------ Size: {}".format(os.path.basename(file),os.stat(file).st_size))

conn.sendall(fileInfo)

try:
        with open(file) as f:
                while True:
                        buffer = f.read(1024).encode()
                        print (buffer)
                        conn.sendall(buffer)
                        if not buffer:
                                break
                f.close()
except Exception as e:
        print (e)