from hashlib import md5

a = 'c2f7ab46df3db842040a86a0897a5377'

m = md5()

m.update(a.encode())

print (m.hexdigest())