
# EventPacketGenerator ver 1.1.0


- Development Environment
	* OS : centos 6.8
	* PL : Python3.5

## Install
`

git clone git@github.com:LeeMinhoe/01_project.git

`

 - How to execution : python3.5 main.py -f/m/d (Target) (-p/r/g arg) (-l)
1) single packet transport :

`
python3.5 main.py -f json.json
`

2) multi packet transport :

`
python3.5 main.py -m directory name
`

3) multi packet transport  :
(packets's destination is same)

`
python3.5 main.py -d directory name
`

 - Directory Structure
	* 01_code Directory is code 
	* 02_log Directory is log.txt directory
	* 98_server Directory is Testing server program Directory 
	* 99_JSON is Json file Directory 

 - Json file format :
'
{
	"Header":
	[
		{
			"IP":"127.0.0.1",
			"Port":50007,
			"Protocol":"TCP",
			"pps":1
		}
	],
	"Data":
	[
		{
			"Type":"int",		
			"value":1		
		},
		{
			"Type":"float",
			"value":3.14
		},
		{
			"Type":"str",
			"value":"Hi"
		},


		etc.....

	]
}
'

	1) IP is Logical address
	2) Port is port address
	3) Protocol choice TCP or UDP
	4) pps is packet per second
	5) isRandom is "Data's value is random?"
	6) Type is { short, unsigned short, int, unsigned int, float, double, str } to value
	7) except Type is { __Bool(bool), signed char(Integer), unsigned char(Integer), void*(Integer) }
	8) Hold Type is { char, long, unsigned long, long long, unsigned long long }
