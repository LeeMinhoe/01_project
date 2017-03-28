
import json
import os
from color import *

#############################################################
# Packet�� �ش� ���� �κ� Class
#############################################################
class Packet_Header:
	# �ʱ�ȭ �Լ�
	def __init__(self, dst_ip, dst_port, protocol):
		self.dst_ip = dst_ip
		self.dst_port = int(dst_port)
		self.protocol = protocol
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
		self.isRandom = isRandom
		self.pps = int(pps)
		self.json_file_name = json_file_name
		self.DataField = DataField
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
		self.Header_part = Header_part
		self.Data_part = Data_part
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
	Jsonpwd = os.getcwd() + '/../99_JSON'
	print("Target Path : " + Jsonpwd + '/' + jsonf)
	os.chdir(Jsonpwd)
	
	try :
			
		with open(json_file_name) as data_file:							# �Է��� json file �� �о 
			DataStructure = json.load(data_file)						# Pakcet�� Header ������,

		dst_ip = DataStructure["Header"][0]["IP"]						# ���ۿ� �ʿ��� option,
		dst_port = DataStructure["Header"][0]["Port"]					# ������ �θ� ������ �����Ѵ�
		protocol = DataStructure["Header"][0]["Protocol"]				#
		isRandom = DataStructure["Header"][0]["isRandom"]				#
		pps = DataStructure["Header"][0]["pps"]							#
		Data = DataStructure["Data"]									#
	
		header_p = Packet_Header(dst_ip, dst_port, protocol)			#
		data_p = Packet_Data(isRandom, pps, json_file_name, Data)		# Class �ʱ�ȭ
		packet = Packet(header_p, data_p)								#

		return packet

	###################################
	########### ����ó�� List ############
	###################################
	# ������ ã�� �� ���� �� �Ͼ / no file
	except FileNotFoundError as e:
		printe("error #1")
		print()
		printe(str(e))
		print()
		exit(1)
	###################################
	# ���� �ʱ�ȭ�Ҷ� �Ͼ
	except KeyError as e:
		printe("error #2")
		print()
		printe("KeyError : " + str(e))
		printe("modify " + jsonf)
		print()
		exit(1)
	###################################
	# �������� �ʴ� ������ ���� �� �Ͼ�� ����
	except UnboundLocalError as e:
		printe("error #3")
		print()
		printe(e)
		print()
		exit(1)	
	###################################
	# Json file ���� value�� ���� ��
	# Json format�� �߸��Ǿ�����
	# json file�� �߸��� ��ġ�� error string���� �˷���
	except json.decoder.JSONDecodeError as e:
		print()
		printe(str(e))
		print()
		exit(1)
	###################################

#############################################################
