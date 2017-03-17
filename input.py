
import json


# Packet�� �ش� ���� �κ� Class
class Packet_Header:
	# �ʱ�ȭ
	def __init__(self, dst_ip, dst_port, protocol):
		self.dst_ip = dst_ip
		self.dst_port = int(dst_port)
		self.protocol = protocol
	# Packet �ش� �κ� ��¹�
	def print_Header_info(self):
		print("IP address : ", self.dst_ip)
		print("port address : ", self.dst_port)
		print("protocol : ", self.protocol)


# Packet�� ������ ���� �κ� Class
class Packet_Data:
	# �ʱ�ȭ
	def __init__(self, isRandom, pps, json_file_name):
		self.isRandom = isRandom
		self.pps = int(pps)
		self.json_file_name = json_file_name
	# Packet ������ �κ� ��¹�
	def print_Data_info(self):
		print("is Random : ", self.isRandom)
		print("pps : ", self.pps)
		print("json_file_name : ", self.json_file_name)


# Packet Class : Header + Data
class Packet:
	# �ʱ�ȭ
	def __init__(self, Header_part, Data_part):
		self.Header_part = Header_part
		self.Data_part = Data_part
	# Packet ���� ��¹�
	def print_packet_info(self):
		self.Header_part.print_Header_info()
		self.Data_part.print_Data_info()




# �Է� ���� �޴� �Լ�
# ����ó�� �ʿ� : �� �Է�(json ���� �̸� ����)�� ���� ���� ���� �Ͽ� ����ó��
def inputModule():
	dst_ip = input("Destination IP address : ")
	dst_port = input("Destination Port address : ")
	while(1):
		protocol = input("Protocol : ")
		if protocol == 'UDP' or protocol == 'TCP':
			break
	while(1):
		isRandom = input(" Is Packet Rand Data? : ") # yes or no
		if isRandom == 'yes' or isRandom == 'no':
			break
	pps = input(" N packet / sec : ")
	json_file_name = input("json file name is : ")
	
	header_p = Packet_Header(dst_ip, dst_port, protocol)
	data_p = Packet_Data(isRandom, pps, json_file_name)
	packet = Packet(header_p, data_p)

	return packet




