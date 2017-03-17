import socket
import json
import pickle


def ReadJson(json_file_name):
	#print(json_file_name)
	jsonFile = json_file_name
	with open(jsonFile) as data_file:
		DataStructure = json.load(data_file)

	
	#print(DataStructure)
	#print()

	return DataStructure


	# case 1 pickle _ in TCP
def send_packet_TCP_pk(Pkt):
	#DataStructure
	#DS is json format
	DS = ReadJson(Pkt.Data_part.json_file_name)

	#message is pickle format
	message = pickle.dumps(DS)

	#print(message)

	#print(message)
	HOST=Pkt.Header_part.dst_ip
	#print(HOST)
	PORT=Pkt.Header_part.dst_port
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST,PORT))

	s.send(message)
	#data=s.recv(1024)

	s.close()

	#data2 = pickle.loads(data)
	#print(data2)


	# case 1 pickle _ in UDP
def send_packet_UDP_pk(Pkt):
	DS = ReadJson(Pkt.Data_part.json_file_name)

	message = pickle.dumps(DS)

	HOST=Pkt.Header_part.dst_ip
	PORT=Pkt.Header_part.dst_port
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	s.sendto(message, (HOST, PORT))
	#data, addr=s.recvfrom(1024)  
	#print(data)

	#data2 = pickle.loads(data)
	#print(data2)


