from header import *

def run():
	packet = inputModule()

	print()

	#packet.print_packet_info()

	print()
	
	if packet.Header_part.protocol == 'TCP':
		send_packet_TCP_pk(packet)
	elif packet.Header_part.protocol == 'UDP':
		send_packet_UDP_pk(packet)

if __name__ == "__main__":
	run()
