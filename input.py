import json



class Packet_Header:
	def __init__(self, dst_ip, dst_port, protocol):
		self.dst_ip = dst_ip
		self.dst_port = dst_port
		self.protocol = protocol

	def print_Header_info(self):
		print("IP address : ", self.dst_ip)
		print("port address : ", self.dst_port)
		print("protocol : ", self.protocol)



class Packet_Data:
	def __init__(self, isRandom, pps, json_file_name):
		self.isRandom = isRandom
		self.pps = pps
		self.json_file_name = json_file_name
	
	def print_Data_info(self):
		print("is Random : ", self.isRandom)
		print("pps : ", self.pps)
		print("json_file_name : ", self.json_file_name)



class Packet:
	def __init__(self, Header_part, Data_part):
		self.Header_part = Header_part
		self.Data_part = Data_part

	def print_packet_info(self):
		self.Header_part.print_Header_info()
		self.Data_part.print_Data_info()





def inputModule():
	dst_ip = input("Destination IP address : ")
	dst_port = input("Destination Port address : ")
	protocol = input("Protocol : ")
	isRandom = input(" Is Packet Rand Data? : ") # yes or no
	pps = input(" N packet / sec : ")
	json_file_name = input("json file name is : ")
	
	header_p = Packet_Header(dst_ip, dst_port, protocol)
	data_p = Packet_Data(isRandom, pps, json_file_name)
	packet = Packet(header_p, data_p)

	return packet


def ReadJson(json_file_name):
	#print(json_file_name)
	jsonFile = json_file_name
	with open(jsonFile) as data_file:
		DataStructure = json.load(data_file)

	print(DataStructure)

	return DataStructure



	
def run():
	packet = inputModule()

	print()

	packet.print_packet_info()

	print()

	DS = ReadJson(packet.Data_part.json_file_name)#

if __name__ == "__main__":
	run()
