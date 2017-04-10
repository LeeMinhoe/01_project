
from color import *

def veri_type_checker(DataStructure):

	for DS in DataStructure:
		for Data in DS:
			# char				1Byte
			if ( Data["Type"] == "char" ):
				if type(Data["value"]) is int:
					#print("char Ok")
					pass
				elif type(Data["value"]) is list:
					#print("list Ok")
					pass
				elif (type(Data["value"]) is str and len(Data["value"]) == 1):
					#print("char Ok")
					pass
				else :
					printe("char input is wrong")

			# INTEGER 
			# signed char		1Byte
			# unsinged char		1Byte
			# short				2Byte
			# unsinged short	2Byte
			# int				4Byte
			# unsinged int		4Byte
			# long				4Byte
			# unsigned long		4Byte
			# long long			8Byte
			# unsinged long long 8Byte
			elif (Data["Type"] == "signed char" or Data["Type"] == "unsigned char"
			or Data["Type"] == "short" or Data["Type"] == "unsigned short"
			or Data["Type"] == "int" or Data["Type"] == "unsigned int"
			or Data["Type"] == "long" or Data["Type"] == "unsigned long"
			or Data["Type"] == "long long" or Data["Type"] == "unsinged long long"):
				if type(Data["value"]) is int:
					#print("Integer Ok");
					pass
				elif type(Data["value"]) is list:
					#print("Interger List Ok")
					pass
				elif ( type(Data["value"]) is str and Data["value"] == "Random" ):
					#print("Input is Random")
					pass
				else :
					printe("Integer input is wrong")				
					
			# bool 1Byte
			elif Data["Type"] == "bool":
				if type(Data["value"]) is bool:
					#print("bool Ok");
					pass
				else :
					printe("bool input is wrong")

			# FLOAT
			# float		4Byte
			# double	8Byte
			elif Data["Type"] == "float" and Data["value"] == "double":
				if type(Data["value"]) is float :
					#print("Float Ok");
					pass
				elif type(Data["value"]) is list :
					#print("Float List Ok");
					pass
				else :
					printe("bool input is wrong")


			# STRING
			# str		NByte
			elif Data["Type"] == "str":
				if type(Data["str len"]) is int:
					pass
				else :
					printe("Declare str len")

				if type(Data["value"]) is str :
					#print("String Ok");
					pass
				elif type(Data["value"]) is list :
					#print("String List Ok");
					pass
				elif type(Data["value"]) is int :
					#print("Random String Ok");
					pass
				else :
					printe("str input is wrong")

			# struct in_addr
			# str		4Byte
			elif Data["Type"] == "struct in_addr":
				if type(Data["value"]) is str :
					#print("addr Ok");
					pass
				elif type(Data["value"]) is list :
					#print("addr List Ok");
					pass
				elif type(Data["value"]) == "Random" :
					#print("Random addr Ok");
					pass
				elif type(Data["value"]) == "random" :
					#print("random addr Ok");
					pass
				else :
					printe("addr input is wrong")


			# time 
			elif Data["Type"] == "time":
				if type(Data["value"]) is int :
					#print("time Ok");
					pass
				elif type(Data["value"]) is list :
					#print("time List Ok");
					pass
				elif Data["value"] == "now" :
					#print("time now Ok");
					pass
				elif Data["value"] == "Random" :
					#print("Random time from 1970 to now Ok");
					pass
				elif type(Data["value"]) is str :
					#print("string time Ok");
					pass
				else :
					printe("time input is wrong")
			
			# hex
			elif Data["Type"] == "hex":
				if type(Data["value"]) is str :
					#print("hex Ok");
					pass
				elif type(Data["value"]) is list :
					#print("hex List Ok");
					pass
				elif type(Data["value"]) == "Random" :
					#print("Random hex Ok");
					pass
				else :
					printe("hex input is wrong")

			# MAC addr
			elif Data["Type"] == "MAC addr":
				if type(Data["value"]) is str :
					#print("addr Ok");
					pass
				elif type(Data["value"]) is list :
					#print("addr List Ok");
					pass
				elif type(Data["value"]) == "Random" :
					#print("Random addr Ok");
					pass
				elif type(Data["value"]) == "random" :
					#print("random addr Ok");
					pass
				else :
					printe("addr input is wrong")
			
			# not define variable
			else :
				printe("Not Define Variable")


def veri_range_checker(DataStructure):

	for DS in DataStructure:
		for Data in DS:
			# char 1Byte
			if Data["Type"] == "char":
				if (ord(Data["value"]) <= 127 and ord(Data["value"]) >= -128):
					#print("char Ok")
					pass
				else :
					printe("char input is wrong")
			
			# signed char 1Byte
			elif Data["Type"] == "signed char":
				if Data["value"] <= 127 and Data["value"] >= -128:
					#print("signed char Ok");
					pass
				else :
					printe("signed char input is wrong")				
		
			# unsinged char 1Byte
			elif Data["Type"] == "unsigned char":
				if Data["value"] <= 255 and Data["value"] >= 0:
					#print("unsigned char Ok");
					pass
				else :
					printe("unsigned char input is wrong")

			# bool 1Byte
			elif Data["Type"] == "bool":
				if Data["value"] == True or Data["value"] == False :
					#print("bool Ok");
					pass
				else :
					printe("bool input is wrong")

			# short 2Byte
			elif Data["Type"] == "short":
				if Data["value"] <= 32767 and Data["value"] >= -32768:
					#print("short Ok");
					pass
				else :
					printe("short input is wrong")
			
			# unsinged short 2Byte
			elif Data["Type"] == "unsigned short":
				if Data["value"] <= 65535 and Data["value"] >= 0:
					#print("unsigned short Ok");
					pass
				else :
					printe("unsigned short input is wrong")
			
			# int 4Byte
			elif Data["Type"] == "int":
				if Data["value"] <= 2147483647 and Data["value"] >= -2147483648 :
					#print("int Ok");
					pass
				else :
					printe("int input is wrong")

			# unsinged int 4Byte
			elif Data["Type"] == "unsigned int":
				if Data["value"] <= 4294967295 and Data["value"] >= 0 :
					#print("unsigned int Ok");
					pass
				else :
					printe("unsigned int input is wrong")

			# long 4Byte
			elif Data["Type"] == "long":
				if Data["value"] <= 2147483647 and Data["value"] >= -2147483648 :
					#print("long Ok");
					pass
				else :
					printe("long input is wrong")

			# unsigned long 4Byte
			elif Data["Type"] == "unsigned long":
				if Data["value"] <= 4294967295 and Data["value"] >= 0 :
					#print("unsigned long Ok");
					pass
				else :
					printe("unsinged long input is wrong")
			
			# long long 8Byte
			elif Data["Type"] == "long long":
				if Data["value"] <= 9223372036854775807 and Data["value"] >= -9223372036854775808 :
					#print("long long Ok");
					pass

			# unsinged long long 8Byte
			elif Data["Type"] == "unsinged long long":
				if Data["value"] <= 18446744073709551615 and Data["value"] >= 0 :
					#print("unsinged long long Ok");
					pass
			
			# String NByte
			elif Data["Type"] == "str":
				if len(Data["value"]) > Data["str len"]:
					printe("too long value")
				elif len(Data["value"]) == Data["str len"]:
					#print("not null packing")
					pass
				else :
					#print("null packing")
					pass

			# except float, double
			# except struct in_addr, time, hex, Mac addr

			

			