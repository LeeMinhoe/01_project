
How to execution : python3.5 main.py (Target Json file name)



Json file format :



{
	"Header":				# Header ���� ���� ����
	[
		{
			"IP":"127.0.0.1",	# Destination IP ����
			"Port":50007,		# Destination Port ����
			"Protocol":"TCP",	# ������ ��Ŷ�� Protocol ����
			"pps":1,		# �ѹ��� ������ ��Ŷ�� �� ����
			"isRandom":"yes"	# ���ǵ� ������ �������� ������ ���� ������ ����
		}
	],
	"Data":
	[
		{
			"Type":"int",		# �������� �ڷ��� ���� (int, float, str)
			"value":1		# �������� �� ���� 
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