import json
import os
from color import *

#############################################################
# Packet의 해더 관련 부분 Class
class Packet_Header:
	# 초기화 함수
	def __init__(self, dst_ip, dst_port, protocol):
		self.dst_ip = dst_ip
		self.dst_port = int(dst_port)
		self.protocol = protocol
	# Packet Header info 출력문
	def print_Header_info(self):
		print("* IP address : ", self.dst_ip)
		print("* port address : ", self.dst_port)
		print("* protocol : ", self.protocol)
#############################################################


#############################################################
# Packet의 데이터 관련 부분 Class
class Packet_Data:
	# 초기화
	def __init__(self, pps, json_file_name, DataField):
		self.pps = int(pps)
		self.json_file_name = json_file_name
		self.DataField = DataField
	# Packet Data info 출력문
	def print_Data_info(self):
		print("* pps : ", self.pps)
		print("* json_file_name : ", self.json_file_name)
		print("* Data Field in Json")	
		for DS in self.DataField:
			print("#")
			for data in DS:
				print("    " + str(data))
		#print(self.DataField)
		print("##########################")
#############################################################


#############################################################
# Packet Class : Header + Data
# 해더와 데이터 부분을 더한 클래스
class Packet:
	# 초기화
	def __init__(self, Header_part, Data_part):
		self.Header_part = Header_part
		self.Data_part = Data_part
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
def inputModule(jsonf, d):
	json_file_name = jsonf

	di = ''

	Jsonpwd = os.getcwd() + '/../99_JSON/' + d
	print("# Target Path : " + Jsonpwd + '/' + jsonf)
	os.chdir(Jsonpwd)
	
	try :

		with open(json_file_name) as data_file:	
			DataStructure = json.load(data_file)

		dst_ip = DataStructure["Header"][0]["IP"]
		dst_port = DataStructure["Header"][0]["Port"]
		protocol = DataStructure["Header"][0]["Protocol"]
		pps = DataStructure["Header"][0]["pps"]
		

		Data = []
		if jsonf == "header.json":
			dataList = []
			for data in os.listdir(os.getcwd()):
				if data.endswith(".json") and data != "header.json":
					dataList.append(data)
			for data in dataList:
				di = data
				with open(data) as data_file:
					DS = json.load(data_file)
				Data.append(DS["Data"])
		else :
			Data.append(DataStructure["Data"])
	
		header_p = Packet_Header(dst_ip, dst_port, protocol)
		data_p = Packet_Data(pps, json_file_name, Data)
		packet = Packet(header_p, data_p)
		
		return packet

	########### 예외처리 List ############
	# 파일을 찾을 수 없을 때 일어남 / no file
	except FileNotFoundError as e:
		printe("error #1")
		print()
		printe(str(e))
		print()
		exit(1)
	# 변수 초기화할때 일어남
	except KeyError as e:
		printe("error #2")
		print()
		printe("KeyError : " + str(e))
		printe("modify " + jsonf)
		print()
		exit(1)
	# 존재하지 않는 변수에 접근 시 일어나는 에러
	except UnboundLocalError as e:
		printe("error #3")
		print()
		printe(e)
		print()
		exit(1)	
	# Json file 안의 value가 없을 때
	# Json format이 잘못되었을때
	# json file의 잘못된 위치도 error string으로 알려줌
	except json.decoder.JSONDecodeError as e:
		print("error #4")
		print("who : " + di)
		print()
		printe(str(e))
		print()
		exit(1)