
import json


# Packet의 해더 관련 부분 Class
class Packet_Header:
	# 초기화
	def __init__(self, dst_ip, dst_port, protocol):
		self.dst_ip = dst_ip
		self.dst_port = int(dst_port)
		self.protocol = protocol
	# Packet 해더 부분 출력문
	def print_Header_info(self):
		print("IP address : ", self.dst_ip)
		print("port address : ", self.dst_port)
		print("protocol : ", self.protocol)


# Packet의 데이터 관련 부분 Class
class Packet_Data:
	# 초기화
	def __init__(self, isRandom, pps, json_file_name):
		self.isRandom = isRandom
		self.pps = int(pps)
		self.json_file_name = json_file_name
	# Packet 데이터 부분 출력문
	def print_Data_info(self):
		print("is Random : ", self.isRandom)
		print("pps : ", self.pps)
		print("json_file_name : ", self.json_file_name)


# Packet Class : Header + Data
class Packet:
	# 초기화
	def __init__(self, Header_part, Data_part):
		self.Header_part = Header_part
		self.Data_part = Data_part
	# Packet 정보 출력문
	def print_packet_info(self):
		self.Header_part.print_Header_info()
		self.Data_part.print_Data_info()




# 입력 인자 받는 함수
# 예외처리 필요 : 각 입력(json 파일 이름 제외)에 대한 범위 설정 하여 예외처리
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




