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
	
	parser = optparse.OptionParser('main.py -f/m/d <target> (-p/r/g <option>)')
	parser.add_option("-f", dest="target_file_name", help="target is json file name", metavar="TARGET file name")
	parser.add_option("-m", dest="target_mdirectory_name", help="target is name of directory / N session", metavar="TARGET dir name")
	parser.add_option("-d", dest="target_directory_name", help="target is name of directory that has \"header.json\"", metavar="TARGET dir name")


	parser.add_option("-p", dest="steady", metavar="sec", type='float', help="input : float - steady pulse time (sec)")
	parser.add_option("-r", dest="random", metavar="from to", type='int', nargs=2, help="input : int ,int - random pulse time range from (int) to (int)")
	parser.add_option("-g", dest="gauss", metavar="avg sd", type='int', nargs = 2, help="input : int, int - Average, Standard Deviation / According to gaussian distributions")
	parser.add_option("-l", dest="loof", action='store_true', help="if you using this option, Packet Scenario repeat")

	(options, args) = parser.parse_args()
	if len(sys.argv)-1 == 0:
		print(parser.usage)
		exit(1)

	while True :
		Pkt = []
	
		#1 -f : single
		if options.target_file_name != None:
			Pkt.append(inputModule(options.target_file_name, "."))
			print("#1")

		#2 -m : multi
		elif options.target_mdirectory_name != None:
			fileList = []
			for file in os.listdir(os.getcwd() + '/../99_JSON/' + options.target_mdirectory_name):
				if file.endswith(".json"):
					fileList.append(file)
			for f in fileList:
				if f != 'header.json':
					Pkt.append(inputModule(f, options.target_mdirectory_name))
					os.chdir(os.getcwd() + '/..')
			print("#2")

		#3 -d : direcotory
		elif options.target_directory_name != None:
			Pkt.append(inputModule("header.json", options.target_directory_name))
			os.chdir(os.getcwd() + '/..')
			print("#3")
	
		# Pkt List is empty	
		if len(Pkt) == 0:
			printe("There is no Json file!")
			printe("Check 99_JSON directory")
			exit(1)

		# numbering pkt
		totalPN = 0

		# Rand to value module
		for p in Pkt:
			veri_type_checker(p.Data_part.DataField)
			RandToValue(p.Data_part.DataField)
			Converter(p.Data_part.DataField)
			veri_range_checker(p.Data_part.DataField)
		
			if len(p.Data_part.DataField) != 0:
				totalPN += p.Data_part.pps * len(p.Data_part.DataField)
		#
		sendPKTCount = 0
		t = []
		alladder = 0
	

		if options.gauss != None:
			m = options.gauss[0]
			sd = options.gauss[1]
			for i in range(totalPN) :
				z = random.gauss(m, sd)
				if z < 0 : z = (-1) * z
				t.append(z)
				alladder += z
			t.sort()
		elif options.steady != None:
			for i in range(totalPN):
				t.append(options.steady * (i+1))
				alladder += t[i]
		elif options.random != None:
			t.append(random.uniform(options.random[0], options.random[1]))
			alladder += t[0]
			for i in range(totalPN-1):
				t.append(t[i] + random.uniform(options.random[0], options.random[1]))
				alladder += t[i]

		print(t)
		print(alladder / totalPN)


		# Transmission Packet
		# print Info / Send Packet
		th_p = []
		print("start : " + str(datetime.now()))
		for i in range(0, len(Pkt)):
			Pkt[i].print_packet_info()
	
			print()

			if options.steady is None and options.random is None and options.gauss is None:
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
			
			else :
				if Pkt[i].Header_part.protocol == 'TCP':
					send_packet_TCP_pulse(Pkt[i], t, sendPKTCount)
				elif Pkt[i].Header_part.protocol == 'UDP':
					send_packet_UDP_pulse(Pkt[i], t, sendPKTCount)

		if options.steady is None and options.random is None and options.gauss is None:
			for th in th_p:
				th.join()
		
		for pkt in Pkt:
			makelog(pkt)

		print("end   : " + str(datetime.now()))
		if options.loof != True:
			break;
if __name__ == "__main__":
	run()

