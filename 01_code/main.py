from header import *
from threading import Thread
import optparse

def th_f(pkt):
	if pkt.Header_part.protocol == 'TCP':
		send_packet_TCP_pk(pkt)
	elif pkt.Header_part.protocol == 'UDP':
		send_packet_UDP_pk(pkt)
	return

def run():
	
	parser = optparse.OptionParser('main.py -f/m/d <target>')
	parser.add_option("-f", "--file", dest="target_file_name", help="target is json file name", metavar="TARGET")
	parser.add_option("-m", "--multi", dest="target_mdirectory_name", help="target is name of directory / N session", metavar="TARGET")
	parser.add_option("-d", "--directory", dest="target_directory_name", help="target is name of directory that has \"header.json\"", metavar="TARGET")

	(options, args) = parser.parse_args()
	if len(sys.argv)-1 == 0:
		print(parser.usage)
		exit(1)

	Pkt = []
	
	#1 -f : single
	if options.target_file_name != None:
		Pkt.append(inputModule(options.target_file_name, "."))

	#2 -m : multi
	elif options.target_mdirectory_name != None:
		fileList = []
		for file in os.listdir(os.getcwd() + '/../99_JSON/' + options.target_mdirectory_name):
			if file.endswith(".json"):
				fileList.append(file)
		for f in fileList:		
			Pkt.append(inputModule(f, options.target_mdirectory_name))
			os.chdir(os.getcwd() + '/..')

	#3 -d : direcotory
	elif options.target_directory_name != None:
		Pkt.append(inputModule("header.json", options.target_directory_name))
		os.chdir(os.getcwd() + '/..')
	
	# Pkt List is empty	
	if len(Pkt) == 0:
		printe("There is no Json file!")
		printe("Check 99_JSON directory")
		exit(1)

	# Rand to value module
	for p in Pkt:
		RandToValue(p.Data_part.DataField)


	# Transmission Packet
	# print Info / Send Packet
	th_p = []
	
	for i in range(0, len(Pkt)):
		Pkt[i].print_packet_info()

		print()

		if Pkt[i].Header_part.protocol == 'TCP':
			#send_packet_TCP_pk(Pkt[i])
			th = Thread(target=th_f, args=(Pkt[i], ))
			th.start()
			th_p.append(th)

		elif Pkt[i].Header_part.protocol == 'UDP':
			#send_packet_UDP_pk(Pkt[i])
			th = Thread(target=th_f, args=(Pkt[i], ))
			th.start()
			th_p.append(th)

	for th in th_p:
		th.join()
	
	for pkt in Pkt:
		makelog(pkt)

if __name__ == "__main__":
	run()

