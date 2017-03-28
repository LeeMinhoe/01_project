
from header import *

def run():

	Pkt = []
	optionNum = len(sys.argv) - 1
	
	# input is '*.json files in ./99_JSON Directory
	if optionNum == 1 and argv[1] == '*.json' :
		optionNum = 0
		fileList = []
		for file in os.listdir(os.getcwd() + '/../99_JSON'):
			if file.endswith(".json"):
				fileList.append(file)
				optionNum = optionNum + 1

		#print(fileList)
		for i in range(0, optionNum):
			Pkt.append(inputModule(fileList[i]))

	
	# input is Directory name 
	elif optionNum == 1 and os.path.isdir(os.getcwd() + '/../99_JSON/' + argv[1]):
		optionNum = 0
		fileList = []
		for file in os.listdir(os.getcwd() + '/../99_JSON/' + argv[1]):
			if file.endswith(".json"):
				fileList.append(file)
				optionNum = optionNum + 1
		for i in range(0, optionNum):
			Pkt.append(inputModule(fileList[i]))


	# input is single transport / multi transport
	else : 	
		for i in range(1, optionNum + 1):
			Pkt.append(inputModule(argv[i]))

	print(Pkt)
	
	print()
	
	# print Info / Send Packet
	for i in range(0, optionNum):
		Pkt[i].print_packet_info()
		
		print()

		if Pkt[i].Header_part.protocol == 'TCP':
			send_packet_TCP_pk(Pkt[i])
		elif Pkt[i].Header_part.protocol == 'UDP':
			send_packet_UDP_pk(Pkt[i])


if __name__ == "__main__":
	run()
