import socket
import json
import struct
import sys
import binascii
from color import *
from threading import Thread
from multiprocessing import Process
import time
import datetime


#############################################################
# Json 에서 읽어들인 Data Structure를 C/C++ 포맷의 형태로 Packing
#############################################################
def Data_to_Pack(Json):

	result = b''	
	
	Size = len(Json)
	for i in range(0,Size):

		# C type
		if( Json[i]["Type"] == "char"):
			result += struct.pack('<c', (Json[i]["value"]).encode('ascii'))
		elif( Json[i]["Type"] == "signed char"):
			result += struct.pack('<b', Json[i]["value"])
		elif( Json[i]["Type"] == "unsigned char"):
			result += struct.pack('<B', Json[i]["value"])
		elif( Json[i]["Type"] == "bool"):
			result += struct.pack('<?', Json[i]["value"])
		elif( Json[i]["Type"] == "short"):
			result += struct.pack('<h', Json[i]["value"])
		elif( Json[i]["Type"] == "unsigned short"):
			result += struct.pack('<H', Json[i]["value"])
		elif( Json[i]["Type"] == "int"):
			result += struct.pack('<i', Json[i]["value"])
		elif( Json[i]["Type"] == "unsigned int"):
			result += struct.pack('<l', Json[i]["value"])
		elif( Json[i]["Type"] == "long"):
			result += struct.pack('<l', Json[i]["value"])
		elif( Json[i]["Type"] == "unsigned long"):
			result += struct.pack('<L', Json[i]["value"])
		elif( Json[i]["Type"] == "long long"):
			result += struct.pack('<q', Json[i]["value"])
		elif( Json[i]["Type"] == "unsigned long long"):
			result += struct.pack('<Q', Json[i]["value"])
		elif( Json[i]["Type"] == "float"):
			result += struct.pack('<f', Json[i]["value"])
		elif( Json[i]["Type"] == "double"):
			result += struct.pack('<d', Json[i]["value"])
		elif( Json[i]["Type"] == "str"):
			option = '<' + str(Json[i]["str len"]) + 's'
			result += struct.pack(option, (Json[i]["value"]).encode('utf-8'))

		
		# user define
		elif( Json[i]["Type"] == "struct in_addr"):
			result += socket.inet_aton(Json[i]["value"])
		
		elif( Json[i]["Type"] == "time"):
			#if type(Json[i]["value"]) is str:
			#	datett = datetime.datetime.strptime(Json[i]["value"], '%Y-%m-%d %H:%M:%S')
			#	datet = int(time.mktime(datett.timetuple()))
			#elif type(Json[i]["value"]) is int :
			#	datet = Json[i]["value"]
			#result += struct.pack('<i', datet)
			result += struct.pack('<i', Json[i]["value"])
			
		elif( Json[i]["Type"] == "hex"):
			d = int(Json[i]["value"], 16)
			result += struct.pack('<l', d)

		elif( Json[i]["Type"] == "MAC addr"):
			macbytes = binascii.unhexlify(Json[i]["value"].replace(':', ''))
			result += macbytes
		else : 
			printe(" [ " + Json[i]["Type"] + " ]")
			printe("Upper Type is undefined type")
			return False
		

		#print(result)

	return result 
#############################################################

def send_P_T(sock, data, roof):

	for i in range(int(roof)):
		sock.send(data)
		if i%50 == 0 :
			time.sleep(0.1)
		#sock.sendto(data.encode('utf-8'), (HOST, PORT))
	return	

#################################################################
#	# TCP packet Send function
#################################################################
def send_packet_TCP_pk(Pkt):

	DataStructure = Pkt.Data_part.DataField

	DS = []
	for i in range(len(DataStructure)):
		DS.append(Data_to_Pack(DataStructure[i]))
	

	# Error
	# Undefined Data Type -> packing fail
	if DS == False :
		printe("mistaken file name : " + Pkt.Data_part.json_file_name)
		exit(1)

	HOST=Pkt.Header_part.dst_ip
	PORT=Pkt.Header_part.dst_port
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		s.connect((HOST,PORT))
		
		
	except ConnectionRefusedError as e:
		print()
		printe(str(e))
		print()
		exit(1)
		#printe("non 3-handshke / only send ack")

	except TimeoutError as e:
		print()
		printe(str(e))
		print()
		exit(1)
	
	except OSError as e:
		print()
		printe(str(e))
		print()
		exit(1)
	
	for ds in DS:
		# dummy
		if Pkt.Data_part.pps >= 100:
			choose = 2
		else :
			choose = 1

		roof = Pkt.Data_part.pps
	
		# Single Thread / Single Process
		if choose == 1:
			for i in range(0, roof):
				s.send(ds)
		# Muti Thread
		elif choose == 2:
			mt1 = Thread(target=send_P_T, args=(s, ds, int(roof/4)))
			mt2 = Thread(target=send_P_T, args=(s, ds, int(roof/4)))
			mt3 = Thread(target=send_P_T, args=(s, ds, int(roof/4)))
			mt4 = Thread(target=send_P_T, args=(s, ds, int(roof/4) + roof%4))

			mt1.start()
			mt2.start()
			mt3.start()
			mt4.start()
			mt1.join()
			mt2.join()
			mt3.join()
			mt4.join()

	s.close()
#################################################################
def send_packet_TCP_pulse(Pkt, t, sendPKTCount):

	DataStructure = Pkt.Data_part.DataField

	DS = []
	for i in range(len(DataStructure)):
		DS.append(Data_to_Pack(DataStructure[i]))
	

	# Error
	# Undefined Data Type -> packing fail
	if DS == False :
		printe("mistaken file name : " + Pkt.Data_part.json_file_name)
		exit(1)

	HOST=Pkt.Header_part.dst_ip
	PORT=Pkt.Header_part.dst_port
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		s.connect((HOST,PORT))
		
		
	except ConnectionRefusedError as e:
		print()
		printe(str(e))
		print()
		exit(1)
		#printe("non 3-handshke / only send ack")

	except TimeoutError as e:
		print()
		printe(str(e))
		print()
		exit(1)
	
	except OSError as e:
		print()
		printe(str(e))
		print()
		exit(1)
	
	for ds in DS:
		roof = Pkt.Data_part.pps
	
		# Single Thread / Single Process
		for i in range(0, roof):
			sendPKTCount += 1
			temp = t[sendPKTCount]
			s.send(ds)
			time.sleep(t[sendPKTCount])
			#print(datetime.datetime.now())
			for i in range(sendPKTCount ,len(t)):
				t[i] = t[i] - temp
			sendPKTCount += 1
		

	s.close()
#################################################################


def send_P_U(sock, data, HOST, PORT, roof):

	for i in range(int(roof)):
		sock.sendto(data, (HOST, PORT))
		if i%50 == 0 :
			time.sleep(0.1)

	return	

#################################################################
#	# UDP packet Send function
#################################################################
def send_packet_UDP_pk(Pkt):

	DataStructure = Pkt.Data_part.DataField

	DS = []
	for i in range(len(DataStructure)):
		DS.append(Data_to_Pack(DataStructure[i]))

	HOST=Pkt.Header_part.dst_ip
	PORT=Pkt.Header_part.dst_port
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	if Pkt.Data_part.pps >= 100:
		choose = 2
	else :
		choose = 1
	
	roof = Pkt.Data_part.pps

	for ds in DS:
		if choose == 1:
			for i in range(0, roof):
				s.sendto(ds, (HOST, PORT))

		elif choose == 2:
			mt1 = Thread(target=send_P_U, args=(s, ds, HOST, PORT, int(roof/4)))
			mt2 = Thread(target=send_P_U, args=(s, ds, HOST, PORT, int(roof/4)))
			mt3 = Thread(target=send_P_U, args=(s, ds, HOST, PORT, int(roof/4)))
			mt4 = Thread(target=send_P_U, args=(s, ds, HOST, PORT, int(roof/4) + roof%4))

			mt1.start()
			mt2.start()
			mt3.start()
			mt4.start()
			mt1.join()
			mt2.join()
			mt3.join()
			mt4.join()

#################################################################

def send_packet_UDP_pulse(Pkt, t, sendPKTCount):

	DataStructure = Pkt.Data_part.DataField

	DS = []
	for i in range(len(DataStructure)):
		DS.append(Data_to_Pack(DataStructure[i]))

	HOST=Pkt.Header_part.dst_ip
	PORT=Pkt.Header_part.dst_port
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	
	roof = Pkt.Data_part.pps

	for ds in DS:
		for i in range(0, roof):
			temp = t[sendPKTCount]
			s.sendto(ds, (HOST, PORT))
			time.sleep(t[sendPKTCount])
			#print(datetime.datetime.now())
			for i in range(sendPKTCount ,len(t)):
				t[i] = t[i] - temp
			sendPKTCount += 1