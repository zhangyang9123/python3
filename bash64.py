import base64

b = 'a'
bs = base64.b64encode(b)
print (bs.decode())

bss = 'emhlYXNnYWZhZGZzYWRmYXNkZmRzZGFmYWRmYXNhZnJ0eQ=='
bs = base64.b64decode(bss)
print (bs.decode())
