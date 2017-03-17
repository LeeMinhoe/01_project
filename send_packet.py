import socket
import json
import pickle
import input


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
	data=s.recv(1024)

	s.close()

	data2 = pickle.loads(data)
	#print(data2)


def run():
	packet = input.inputModule()

	print()

	packet.print_packet_info()

	print()

	send_packet_TCP_pk(packet)

if __name__ == "__main__":
	run()
