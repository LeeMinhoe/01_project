
#### UDP recv server ####

from socket import *
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

print(data)