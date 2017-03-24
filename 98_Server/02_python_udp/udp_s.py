
#### UDP recv server ####

from socket import *
import json
import struct

HOST=''
PORT=50007
data3=''
s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))

data, addr = s.recvfrom(1024)
print(data)
print()
#s.sendto(data, addr)


value = list(struct.unpack('if3s', data))
value[2] = value[2].decode("ascii")

print(value)
print()
