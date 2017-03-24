
import json
import os

#############################################################
# Packet의 해더 관련 부분 Class
#############################################################
class Packet_Header:
	# 초기화 함수
	def __init__(self, dst_ip, dst_port, protocol):
		self.dst_ip = dst_ip										##str Type
		self.dst_port = int(dst_port)								##int Type
		self.protocol = protocol									##str Type
	# Packet Header info 출력문
	def print_Header_info(self):
		print("* IP address : ", self.dst_ip)
		print("* port address : ", self.dst_port)
		print("* protocol : ", self.protocol)
#############################################################

#############################################################
# Packet의 데이터 관련 부분 Class
#############################################################
class Packet_Data:
	# 초기화
	def __init__(self, isRandom, pps, json_file_name, DataField):
		self.isRandom = isRandom									##str Type
		self.pps = int(pps)											##int Type
		self.json_file_name = json_file_name						##str Type
		self.DataField = DataField									##List Type
	# Packet Data info 출력문
	def print_Data_info(self):
		print("* is Random : ", self.isRandom)
		print("* pps : ", self.pps)
		print("* json_file_name : ", self.json_file_name)
		print("* Data Field in Json")
		print(self.DataField)
		print("##########################")
#############################################################


#############################################################
# Packet Class : Header + Data
# 해더와 데이터 부분을 더한 클래스
#############################################################
class Packet:
	# 초기화
	def __init__(self, Header_part, Data_part):
		self.Header_part = Header_part								##Class Type
		self.Data_part = Data_part									##Class Type
	# Packet Info 출력문
	def print_packet_info(self):
		print("######################")
		print("####Packet Info.######")
		print("######################")
		self.Header_part.print_Header_info()
		self.Data_part.print_Data_info()
#############################################################

#############################################################
# Json file 에서 패킷 정보를 읽어오는 함수
#############################################################
def inputModule(jsonf):
	json_file_name = jsonf

	print()
	print("######################")
	print("#### Program Start####")
	print("######################")
	os.chdir("..")
	Jsonpwd = os.getcwd() + '/99_JSON'
	print("Target Path : " + Jsonpwd + '/' + jsonf)
	os.chdir(Jsonpwd)

	with open(json_file_name) as data_file:							# 입력한 json file 을 읽어서 
		DataStructure = json.load(data_file)						# Pakcet의 Header 데이터,
	dst_ip = DataStructure["Header"][0]["IP"]						# 전송에 필요한 option,
	dst_port = DataStructure["Header"][0]["Port"]					# 데이터 부를 변수에 저장한다
	protocol = DataStructure["Header"][0]["Protocol"]				#
	isRandom = DataStructure["Header"][0]["isRandom"]				#
	pps = DataStructure["Header"][0]["pps"]							#
	Data = DataStructure["Data"]									#
	
	################################################
	## Input Data Header / Data Option 범위 예외처리  ##					# 추가하기
	################################################


	header_p = Packet_Header(dst_ip, dst_port, protocol)			#
	data_p = Packet_Data(isRandom, pps, json_file_name, Data)		# Class 초기화
	packet = Packet(header_p, data_p)								#

	return packet	
#############################################################
