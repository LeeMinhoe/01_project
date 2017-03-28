import socket
import json
import string
import random
import struct
import sys
from color import *


#############################################################
# Json 에서 읽어들인 Data Structure를 C/C++ 포맷의 형태로 Packing
#############################################################
def Data_to_Pack(Json):

	result = b''	
	
	Size = len(Json)
	for i in range(0,Size):
		if( Json[i]["Type"] == "short"):
			result += struct.pack('<h',Json[i]["value"])
		elif( Json[i]["Type"] == "unsigned short"):
			result += struct.pack('<H',Json[i]["value"])
		elif( Json[i]["Type"] == "int"):
			result += struct.pack('<i',Json[i]["value"])
		elif( Json[i]["Type"] == "unsigned int"):
			result += struct.pack('<I',Json[i]["value"])
		elif( Json[i]["Type"] == "float"):
			result += struct.pack('<f',Json[i]["value"])
		elif( Json[i]["Type"] == "double"):
			result += struct.pack('<d',Json[i]["value"])
		elif( Json[i]["Type"] == "str"):
			option = '<' + str(len(Json[i]["value"])+1) + 's'
			result += struct.pack(option, (Json[i]["value"]).encode('ascii'))
		
		else : # 현 프로그램에서 정의되지 않은 전송 데이터 형 , 형변환을 못함
			printe(" [ " + Json[i]["Type"] + " ]")
			printe("Upper Type is undefined type")
			return False
	return result 
#############################################################


#**********************Random Part****************************
#############################################################
# string random 생성기 : 원하는 size 만큼의 string을 생성한다.
#############################################################
def str_generator(size, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
#############################################################
#############################################################
# Data struture 를 Rand 하게 만드는 function
# 추후에 업데이트 해야함
# Error 처리도 업데이트 이후
#############################################################
def rand_json(JS):
	
	JSon = JS
	t1 = 1073741823
	t2 = 1073741823 * (-1)
	Size = len(JSon)
	for i in range(0,Size):
		if( JSon[i]["Type"] == "int"):
			JSon[i]["value"] = random.randint(t2,t1)
		elif( JSon[i]["Type"] == "float"):
			JSon[i]["value"] = random.uniform(t2,t1)
		elif( JSon[i]["Type"] == "str"):
			JSon[i]["value"] = str_generator(len(JSon[i]["value"]))

	return JSon
#############################################################
#*************************************************************



#################################################################
#	# TCP packet Send function
#################################################################
def send_packet_TCP_pk(Pkt):

	DataStructure = Pkt.Data_part.DataField

	if Pkt.Data_part.isRandom == 'yes':
		DataStructure = rand_json(Pkt.Data_part.DataField)
	
	DS = Data_to_Pack(DataStructure)
	
	# Error
	# Undefined Data Type -> packing fail
	if DS == False :
		printe("mistaken file name : " + Pkt.Data_part.json_file_name)
		exit(1)

	#print(DS)

		
	HOST=Pkt.Header_part.dst_ip
	PORT=Pkt.Header_part.dst_port
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	try:
		s.connect((HOST,PORT))
		
		s.send(DS)
		#data=s.recv(1024)

		s.close()
	except:
		printe("non 3-handshke / only send ack")
#################################################################

#################################################################
#	# UDP packet Send function
#################################################################
def send_packet_UDP_pk(Pkt):

	DataStructure = Pkt.Data_part.DataField

	if Pkt.Data_part.isRandom == 'yes':
		DataStructure = rand_json(Pkt.Data_part.DataField)
	
	DS = Data_to_Pack(DataStructure)

	HOST=Pkt.Header_part.dst_ip
	PORT=Pkt.Header_part.dst_port
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	for i in range(0, Pkt.Data_part.pps+1):
		s.sendto(DS, (HOST, PORT))
	#data, addr=s.recvfrom(1024)  
	#print(data)
#################################################################