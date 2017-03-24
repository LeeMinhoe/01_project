
How to execution : python3.5 main.py (Target Json file name)



Json file format :



{
	"Header":				# Header 관련 정보 기입
	[
		{
			"IP":"127.0.0.1",	# Destination IP 기입
			"Port":50007,		# Destination Port 기입
			"Protocol":"TCP",	# 전송할 패킷의 Protocol 기입
			"pps":1,		# 한번에 전송할 패킷의 수 기입
			"isRandom":"yes"	# 정의된 데이터 구조에서 랜덤한 값을 보낼지 기입
		}
	],
	"Data":
	[
		{
			"Type":"int",		# 데이터의 자료형 기입 (int, float, str)
			"value":1		# 데이터의 값 기입 
		},
		{
			"Type":"float",
			"value":3.14
		},
		{
			"Type":"str",
			"value":"Hi"
		}
	]
}