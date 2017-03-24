
import json
import os

#############################################################
# Packet�� �ش� ���� �κ� Class
#############################################################
class Packet_Header:
	# �ʱ�ȭ �Լ�
	def __init__(self, dst_ip, dst_port, protocol):
		self.dst_ip = dst_ip										##str Type
		self.dst_port = int(dst_port)								##int Type
		self.protocol = protocol									##str Type
	# Packet Header info ��¹�
	def print_Header_info(self):
		print("* IP address : ", self.dst_ip)
		print("* port address : ", self.dst_port)
		print("* protocol : ", self.protocol)
#############################################################

#############################################################
# Packet�� ������ ���� �κ� Class
#############################################################
class Packet_Data:
	# �ʱ�ȭ
	def __init__(self, isRandom, pps, json_file_name, DataField):
		self.isRandom = isRandom									##str Type
		self.pps = int(pps)											##int Type
		self.json_file_name = json_file_name						##str Type
		self.DataField = DataField									##List Type
	# Packet Data info ��¹�
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
# �ش��� ������ �κ��� ���� Ŭ����
#############################################################
class Packet:
	# �ʱ�ȭ
	def __init__(self, Header_part, Data_part):
		self.Header_part = Header_part								##Class Type
		self.Data_part = Data_part									##Class Type
	# Packet Info ��¹�
	def print_packet_info(self):
		print("######################")
		print("####Packet Info.######")
		print("######################")
		self.Header_part.print_Header_info()
		self.Data_part.print_Data_info()
#############################################################

#############################################################
# Json file ���� ��Ŷ ������ �о���� �Լ�
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

	with open(json_file_name) as data_file:							# �Է��� json file �� �о 
		DataStructure = json.load(data_file)						# Pakcet�� Header ������,
	dst_ip = DataStructure["Header"][0]["IP"]						# ���ۿ� �ʿ��� option,
	dst_port = DataStructure["Header"][0]["Port"]					# ������ �θ� ������ �����Ѵ�
	protocol = DataStructure["Header"][0]["Protocol"]				#
	isRandom = DataStructure["Header"][0]["isRandom"]				#
	pps = DataStructure["Header"][0]["pps"]							#
	Data = DataStructure["Data"]									#
	
	################################################
	## Input Data Header / Data Option ���� ����ó��  ##					# �߰��ϱ�
	################################################


	header_p = Packet_Header(dst_ip, dst_port, protocol)			#
	data_p = Packet_Data(isRandom, pps, json_file_name, Data)		# Class �ʱ�ȭ
	packet = Packet(header_p, data_p)								#

	return packet	
#############################################################
