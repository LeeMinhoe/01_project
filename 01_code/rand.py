import random
import string
import time
import binascii
import socket

#############################################################
# string random 생성기 : 원하는 size 만큼의 string을 생성한다.
#############################################################
def str_generator(size, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
#############################################################


#삭제 예정
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


def RandToValue(DataStructure):

	# DataStructure is Json format data list
	# DataStructure's type is short, unsigned short, int, unsigned int, long long
		# value is just value -> Random value in this value's type range
		# value type is list -> Random value in this list
		# value is "Random" -> Random value from Random Min to Random Max
	
		
	# DataStructure tour
	# Integer Random value
	for DS in DataStructure:
		for Data in DS:

			## List input (list random)
			if type(Data["value"]) is list:
				Data["value"] = random.sample(Data["value"], 1)[0]
			## is Integer
			if (Data["Type"] == "short" or Data["Type"] == "unsigned short"
			or Data["Type"] == "int" or Data["Type"] == "unsigned int"
			or Data["Type"] == "long long") :
				if Data["value"] == "Random":
					Data["value"] = random.randint(Data["Random Min"], Data["Random Max"])

				elif type(Data["value"]) is int:
					pass

			## is str
			elif (Data["Type"] == "str"):
				print("check")
				if Data["value"] == 0 :
					Data["value"] = str_generator(Data["str len"])
				
				elif type(Data["value"]) is str:
					pass

			## is time
			elif (Data["Type"] == "time"):
				if Data["value"] == "Random" :
					Data["value"] = random.randint(0, int(time.time()))
				elif Data["value"] == "now" :
					Data["value"] = int(time.time())

			
			## is str
			elif (Data["Type"] == "struct in_addr"):
				if Data["value"] == "Random" :
					Data["value"] = '.'.join('%s'%random.randint(0, 255) for i in range(4))

				elif Data["value"] == "random" :
					min = int((binascii.hexlify(socket.inet_aton(Data["addr min"]))).decode(), 16)
					max = int((binascii.hexlify(socket.inet_aton(Data["addr max"]))).decode(), 16)
					randip = random.randint(min, max)
					randip_hex_str = str(hex(randip)).split('0x')[1]
					if len(randip_hex_str) != 8: 
						for i in range(8-len(randip_hex_str)):
							randip_hex_str = '0'+ randip_hex_str
					randip_list = []
					for i in range(4):
						randip_list.append(str(int('0x' + randip_hex_str[i*2:i*2+2], 16)))
					Data["value"] = '.'.join(randip_list)

			## is hex
			elif (Data["Type"] == "hex"):
				if Data["value"] == "Random":
					Data["value"] = hex(random.randint(int(Data["Random Min"], 16), int(Data["Random Max"], 16)))

			## is MAC addr
			elif (Data["Type"] == "MAC addr"):
				if Data["value"] == "Random" :
					Data["value"] = ':'.join('%s' % hex(random.randint(0,255)).split('0x')[1] for i in range(6))
				if Data["value"] == "random" :
					min = int(Data["addr min"].replace(':', ''), 16)
					max = int(Data["addr max"].replace(':', ''), 16)

					r = hex(random.randint(min, max)).split('0x')[1]

					if len(r) != 12:
						print("check")
						for i in range(12-len(r)):
							r = '0' + r
					
					f = []
					for i in range(6):
						f.append(r[i*2:i*2+2])
					Data["value"] = ':'.join(f)