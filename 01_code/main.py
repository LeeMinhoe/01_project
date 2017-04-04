
from header import *
from threading import Thread
def run():
	
	Pkt = []
	optionNum = len(sys.argv) - 1

	##################################### ERROR #1 ######################################
	# No input parameter																#
	if len(sys.argv) - 1 == 0:															#
		printe("Usage : python3.5 " + sys.argv[0] + " "  + "< json files or direcoty >")#
		#print("Check 99_JSON directory")												#
		exit(1)																			#
	#####################################################################################

############################ Create Packet class List ###################################
	#1 input is '*.json files in ./99_JSON Directory
	if optionNum == 1 and argv[1] == '*.json' :
		optionNum = 0
		fileList = []
		for file in os.listdir(os.getcwd() + '/../99_JSON'):
			if file.endswith(".json"):
				fileList.append(file)
				optionNum = optionNum + 1
		for i in range(0, optionNum):
			Pkt.append(inputModule(fileList[i]))

	#2 input is Directory name 
	elif optionNum == 1 and os.path.isdir(os.getcwd() + '/../99_JSON/' + argv[1]):
		optionNum = 0
		fileList = []
		for file in os.listdir(os.getcwd() + '/../99_JSON/' + argv[1]):
			if file.endswith(".json"):
				fileList.append(file)
				optionNum = optionNum + 1
		for i in range(0, optionNum):
			Pkt.append(inputModule(fileList[i]))

	#3,4 input is single transport / multi transport
	else : 	
		for i in range(1, optionNum + 1):
			Pkt.append(inputModule(argv[i]))
#########################################################################################

	#print(Pkt)
	#print()

	############### ERROR #2 ################
	# Pkt List is empty						#
	if len(Pkt) == 0:						#
		printe("There is no Json file!")	#
		printe("Check 99_JSON directory")	#
		exit(1)								#
	#########################################


###################### Transmission Packet ########################################
	# print Info / Send Packet
	th_p = []
	if len(Pkt) == 1:
		for i in range(0, len(Pkt)):
			Pkt[i].print_packet_info()
		
			print()

			if Pkt[i].Header_part.protocol == 'TCP':
				send_packet_TCP_pk(Pkt[i])
			elif Pkt[i].Header_part.protocol == 'UDP':
				send_packet_UDP_pk(Pkt[i])
	
	else :
		
		for i in range(0, len(Pkt)):
			Pkt[i].print_packet_info()

			print()

			if Pkt[i].Header_part.protocol == 'TCP':
				th = Thread(target=th_f, args=(Pkt[i], ))
				th.start()
				th_p.append(th)

			elif Pkt[i].Header_part.protocol == 'UDP':
				th = Thread(target=th_f, args=(Pkt[i], ))
				th.start()
				th_p.append(th)

		for th in th_p:
			th.join()
	
	for pkt in Pkt:
		makelog(pkt)

############################################3######################################
def th_f(pkt):
	if pkt.Header_part.protocol == 'TCP':
		send_packet_TCP_pk(pkt)
	elif pkt.Header_part.protocol == 'UDP':
		send_packet_UDP_pk(pkt)

	return


if __name__ == "__main__":
	run()
