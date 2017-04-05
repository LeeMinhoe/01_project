import os
import datetime

def makelog(Pkt):

	now = datetime.datetime.now()
	nowDate = now.strftime('%Y%m%d')
	nowTime = now.strftime('%H:%M:%S')
	logDirPWD = os.getcwd() + '/../02_log/'
	filename = 'log'+ nowDate + '.txt'
	filepath = logDirPWD + filename
	nowDate = now.strftime('%Y-%m-%d')
	
	os.chdir(logDirPWD)	
	
	f = open(filename, 'a')
	
	f.write("[ Send Time is " + nowDate + " " + nowTime + " ]\n(DST IP : PORT / PROTOCOL)\n")
	f.write(str(Pkt.Header_part.dst_ip) + " : " + str(Pkt.Header_part.dst_port) + " / " + str(Pkt.Header_part.protocol))
	f.write("\n===== Detail Data =====\n")
	for i in range(len(Pkt.Data_part.DataField)):
		for j in range(len(Pkt.Data_part.DataField[i])):
			f.write(str(Pkt.Data_part.DataField[i][j]["value"]) + "( " + str(Pkt.Data_part.DataField[i][j]["Type"]) + " )\n")
	f.write("=======================\n")
	f.write('\n\n')


	f.close()
	