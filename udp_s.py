
#### UDP recv server ####

from socket import *
import pickle
import json

HOST=''
PORT=50007
data3=''
s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))

data, addr = s.recvfrom(1024)
#print(data)
s.sendto(data, addr)

data2 = pickle.loads(data)
print(data2)




