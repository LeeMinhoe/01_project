from header import *

def run():

	packet = inputModule(argv[1])

	#header_p = Packet_Header("127.0.0.1", 50007, "TCP")
	#data_p = Packet_Data("no", 1, "json.json")
	#packet = Packet(header_p, data_p)

	print()

	packet.print_packet_info()

	print()
	
	if packet.Header_part.protocol == 'TCP':
		send_packet_TCP_pk(packet)
	elif packet.Header_part.protocol == 'UDP':
		send_packet_UDP_pk(packet)

if __name__ == "__main__":
	run()
