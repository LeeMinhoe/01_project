import socket
import json
import pickle
import string
import random

def str_generator(size, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def rand_json(JS):
	
	JSon = JS
	t1 = 1073741823
	t2 = 1073741823 * (-1)
	Size = len(JSon["Data"])

	for i in range(0,Size):
		if( JSon["Data"][i]["Type"] == "int"):
			JSon["Data"][i]["value"] = random.randint(t2,t1)
		elif( JSon["Data"][i]["Type"] == "float"):
			JSon["Data"][i]["value"] = random.uniform(t2,t1)
		elif( JSon["Data"][i]["Type"] == "str"):
			JSon["Data"][i]["value"] = str_generator(len(JSon["Data"][i]["value"]))

	return JSon

def ReadJson(Pkt):
	#print(Pkt.Data_part.json_file_name)
	jsonFile = Pkt.Data_part.json_file_name
	with open(jsonFile) as data_file:
		DataStructure = json.load(data_file)

	if Pkt.Data_part.isRandom == 'yes':
		DataStructure = rand_json(DataStructure)
	
	#print(DataStructure)
	#print()

	return DataStructure


	# case 1 pickle _ in TCP
def send_packet_TCP_pk(Pkt):
	#DataStructure
	#DS is json format
	DS = ReadJson(Pkt)

	#message is pickle format
	message = pickle.dumps(DS)

	#print(message)

	#print(message)
	HOST=Pkt.Header_part.dst_ip
	#print(HOST)
	PORT=Pkt.Header_part.dst_port
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		s.connect((HOST,PORT))
	
		for i in range(0, Pkt.Data_part.pps):
			s.send(message)
		#data=s.recv(1024)

		s.close()
	except:
		print("non 3-handshke / only send ack")

	#data2 = pickle.loads(data)
	#print(data2)


	# case 1 pickle _ in UDP
def send_packet_UDP_pk(Pkt):
	#DataStructure
	#DS is json format
	DS = ReadJson(Pkt)

	message = pickle.dumps(DS)

	HOST=Pkt.Header_part.dst_ip
	PORT=Pkt.Header_part.dst_port
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	for i in range(0, Pkt.Data_part.pps+1):
		s.sendto(message, (HOST, PORT))
	#data, addr=s.recvfrom(1024)  
	#print(data)

	#data2 = pickle.loads(data)
	#print(data2)


