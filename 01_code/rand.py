import random
import string
import time
import datetime
import binascii
import socket

#############################################################
# string random 생성기 : 원하는 size 만큼의 string을 생성한다.
#############################################################
def str_generator(size, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
#############################################################

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
				if type(Data["value"]) is int :
					Data["value"] = str_generator(Data["value"])
				
				elif type(Data["value"]) is str:
					pass

			## is time
			elif (Data["Type"] == "time"):
				if Data["value"] == "Random" :
					Data["value"] = random.randint(0, int(time.time()))
			
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
					print(Data["value"])
					print(Data["Type"])
					Data["value"] = hex(random.randint(int(Data["random min"], 16), int(Data["random max"], 16)))
					
					
			## is MAC addr
			elif (Data["Type"] == "MAC addr"):
				if Data["value"] == "Random" :
					x = []
					for i in range(6):
						k = hex(random.randint(0,255)).split('0x')[1]
						if len(k) == 2:
							pass
						else : 
							for j in range(2-len(k)):
								k = '0' + k
						x.append(k)
					Data["value"] = ':'.join(x)
				elif Data["value"] == "random" :
					min = int(Data["addr min"].replace(':', ''), 16)
					max = int(Data["addr max"].replace(':', ''), 16)

					r = hex(random.randint(min, max)).split('0x')[1]

					if len(r) != 12:
						for i in range(12-len(r)):
							r = '0' + r
			
					Data["value"] = ':'.join([r[i:i+2] for i in range(0, len(r), 2)])
					



def Converter(DataStructure):

	for DS in DataStructure:
		for Data in DS:

			if (Data["Type"] == "char" and type(Data["value"]) is int):
				Data["value"] = chr(Data["value"])

			elif Data["Type"] == "time" :
				if Data["value"] == "now":
					Data["value"] = int(time.time())
				elif type(Data["value"]) is str:
					d = datetime.datetime.strptime(Data["value"], '%Y-%m-%d %H:%M:%S')
					Data["value"] = int(time.mktime(d.timetuple()))

			elif Data["Type"] == "bool" :
				if Data["value"] == 1:
					Data["value"] = True
				elif Data["value"] == 0:
					Data["value"] = False