import socket
import json
import pickle




HOST='127.0.0.1' 
PORT=50007
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 


s.sendto("i am client".encode('ascii'), (HOST, PORT))
#s.sendto(message, (HOST, PORT))

data, addr=s.recvfrom(1024)  

