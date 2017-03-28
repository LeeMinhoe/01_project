- Development Environment
	* OS : centos 6.8
	* PL : Python3.5


 - How to execution : python3.5 main.py $(Target)
	* $(Target) : 
	1) single packet transport :		ex) python3.5 main.py json.json
	  json.json is json file name
	2) multi packet transport :		ex) python3.5 main.py json1.json json2.json json3.json
	  json1, json2, json3 packet transport
	3) *.json transport :			ex) python3.5 main.py *.json
	  all json file in 99_JSON Directory
	4) Target Directory transport :		ex) python3.5 main.py TCP
	  TCP is Directory

 - Directory Structure
	* 01_code Directory is code 
	* 98_server Directory is Testing server program Directory 
	* 99_JSON is Json file Directory 

 - Json file format :

{
	"Header":
	[
		{
			"IP":"127.0.0.1",
			"Port":50007,
			"Protocol":"TCP",
			"pps":1,
			"isRandom":"yes"
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
	* IP is Logical address
	* Port is port address
	* Protocol choice TCP or UDP
	* pps is packet per second
	* isRandom is "Data's value is random?"
	* Type is { short, unsigned short, int, unsigned int, float, double, str } to value
	* except Type is { __Bool(bool), signed char(Integer), unsigned char(Integer), void*(Integer) }
	* Hold Type is { char, long, unsigned long, long long, unsigned long long }
