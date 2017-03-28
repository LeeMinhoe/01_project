
#### TCP recv server ####

import socket
import pickle
import json

data_r=''
HOST='192.168.56.129'
PORT=50007
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print()
print('Connected by', addr)


while True:
	data = conn.recv(1024)
	if not data: break
	#conn.send(data)
	data_r = data

#print(data_r)
print(pickle.loads(data_r))

conn.close()

