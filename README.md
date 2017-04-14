
# EventPacketGenerator ver 1.1.0


- Development Environment
	* OS : centos 6.8
	* PL : Python3.5

## Install
```
git clone git@github.com:LeeMinhoe/01_project.git
```

 - How to execution : python3.5 main.py -f/m/d (Target) (-p/r/g arg) (-l)
1) single packet transport :

```
python3.5 main.py -f json.json
```

2) multi packet transport :

```
python3.5 main.py -m directory name
```

3) multi packet transport (packets's destination is same) :


```
python3.5 main.py -d directory name
```

 - Directory Structure
	* 01_code Directory is code 
	* 02_log Directory is log.txt directory
	* 98_server Directory is Testing server program Directory 
	* 99_JSON is Json file Directory 

 - Json file format
```
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
     # bool type
     1) really value : 1(True)
    { 
      "comment": "real value",
      "Type": "bool",
      "value": 1
    },
     2) really value : 0(False)
    { 
      "comment": "real value",
      "Type": "bool",
      "value": 0
    },
     3) One value of the list 
    { 
      "comment": "list",
      "Type": "bool",
      "value": [1, 0]
    }
     
     # char type
     1) really value : ASCii
    {
      "Type": "char",
      "value": "a"
    },
     2) One value of the list
    { 
      "comment": "list",
      "Type": "char",
      "value": [88, 89, 90]
    }

     # signed char type
     1) real value
    {
      "comment": "real value",
      "Type": "signed char",
      "value": 88
    },
     2) One value of the list
    {
      "comment": "list",
      "Type": "signed char",
      "value": [88, 89, 90]
    }

     # unsigned char type
     1) really value
    {
      "comment": "real value",
      "Type": "signed char",
      "value": 88
    },
     2) One value of the list
    {
      "comment": "list",
      "Type": "signed char",
      "value": [88, 89, 90]
    }

     # short type
     1) really value
    { 
      "comment": "real value",
      "Type": "short",
      "value": 15
    },
     2) One value of the list
    { 
      "comment": "list",
      "Type": "short",
      "value": [15, 115, 1115]
    }

     # unsigned short
     1) really value
    { 
      "comment": "real value",
      "Type": "unsigned short",
      "value": 99
    },
     2) One value of the list
    { 
      "comment": "list",
      "Type": "unsigned short",
      "value": [9, 99, 999]
    }

     # int
     1) really value
    { 
      "comment": "real value",
      "Type": "int",
      "value": 4
    },
     2) One value of the list
    { 
      "comment": "list",
      "Type": "int",
      "value": [4, 44, 444]
    }

     # unsigend int
     1) really value
    { 
      "comment": "real value",
      "Type": "unsigned int",
      "value": 13
    },
     2) One value of the list
    { 
      "comment": "list",
      "Type": "unsigned int",
      "value": [13, 113, 1113]
    }

     # long
     1) really value
    { 
      "comment": "real value",
      "Type": "long",
      "value": 14
    },
     2) One value of the list
    { 
      "comment": "list",
      "Type": "long",
      "value": [14, 114, 1114]
    }

     # unsigned long
     1) really value
    { 
      "comment": "real value",
      "Type": "unsigned long",
      "value": 12
    },
     2) One value of the list
    { 
      "comment": "list",
      "Type": "unsigned long",
      "value": [12, 112, 1112]
    }

     # long long
     1) really value
    { 
      "comment": "real value",
      "Type": "long long",
      "value": 11
    },
     2) One value of the list
    { 
      "comment": "list",
      "Type": "long long",
      "value": [11, 111, 1111]
    }

     # unsigned long long
     1) really value
    { 
      "comment": "real value",
      "Type": "unsigned long long",
      "value": 10
    },
     2) One value of the list
    { 
      "comment": "list",
      "Type": "unsigned long long",
      "value": [10, 100, 1000]
    }

     # float
     1) really value
    {
      "comment": "float",
      "Type": "float",
      "value": 3.14
    },
     2) One value of the list
    {
      "comment": "list",
      "Type": "float",
      "value": [3.14, 3.1415, 3.141592]
    }

     # double
     1) really value
    {
      "comment": "double",
      "Type": "double",
      "value": 3.141592
    },
     2) One value of the list
    {
      "comment": "list",
      "Type": "double",
      "value": [3.14, 3.1415, 3.141592]
    }

     # str
     1) str len == len(value)
    {
      "comment": "1-2 v == l",
      "Type": "str",
      "value": "ipplus",
      "str len": 6
    },
     2) str len > len(value) (NULL)
    {
      "comment": "1-3 v < l",
      "Type": "str",
      "value": "ip",
      "str len": 6
    },
     3) One value of the list
    {
      "comment": "2. list",
      "Type": "str",
      "value": ["ipplus", "js", "JS"],
      "str len": 6
    },
     4) len < value size random string (NULL)
    {
      "comment": "3. random",
      "Type": "str",
      "value": 5,
      "str len": 6
    },
     5) len == value size random string (NULL)
    {
      "comment": "3. random",
      "Type": "str",
      "value": 6,
      "str len": 6
    }

     # hex
     1) really value
    {
      "comment": "1. real value",
      "Type": "hex",
      "value": "0x04"
    },
     2) One value of the list
    {
      "comment": "2. list",
      "Type": "hex",
      "value": ["0x03", "0x04", "0x05"]
    },
     3) Random hex value from min to max
    {
      "comment": "3. Random",
      "Type": "hex",
      "value": "Random",
      "random min": "0x04",
      "random max": "0x07"
    }

     # time
     1) really value(Integer)
    {
      "comment": "1. 1970.01.01 00:00:00",
      "Type": "time",
      "value": 0
    },
     2) really value(String)
    {
      "comment": "2. 2017.11.04 00:00:00",
      "Type": "time",
      "value": "2017-11-04 00:00:00"
    },
     3) Random time from 1970 to now
    {
      "comment": "3. Random time from 1970 to now",
      "Type": "time",
      "value": "Random"
    },
     4) One value of the list 
    {
      "comment": "4. list",
      "Type": "time",
      "value": ["1995-11-04 00:00:00", "1993-11-22 00:00:00"]
    },
     5) time is now
    {
      "comment": "5. now",
      "Type": "time",
      "value": "now"
    }

     # struct in_addr
     1) really value
    {
      "commment": "1. real value : local",
      "Type": "struct in_addr",
      "value": "127.0.0.1"
    },
     2) One value of the list
    {
      "commment": "2. list",
      "Type": "struct in_addr",
      "value": ["127.0.0.1", "163.152.219.191", "10.0.2.161"]
    },
     3) Random addr
    {
      "commment": "3. Random",
      "Type": "struct in_addr",
      "value": "Random"
    },
     4) random addr from min to max
    {
      "commment": "4. random",
      "Type": "struct in_addr",
      "value": "random",
      "addr min": "10.0.1.18",
      "addr max": "10.0.1.20"
    }

     # MAC_addr
     1) really value
    {
      "comment": "1. real value",
      "Type": "MAC addr",
      "value": "00:01:02:03:04:05"
    },
     2) One value of the list
    {
      "comment": "2. list",
      "Type": "MAC addr",
      "value": ["00:01:02:03:04:05", "10:21:32:43:54:65", "FF:FF:FF:FF:FF:FF"]
    }


  ]
}
```

	1) IP is Logical address
	2) Port is port address
	3) Protocol choice TCP or UDP
	4) pps is packet per second
	5) isRandom is "Data's value is random?"
	6) Type is { short, unsigned short, int, unsigned int, float, double, str } to value
	7) except Type is { __Bool(bool), signed char(Integer), unsigned char(Integer), void*(Integer) }
	8) Hold Type is { char, long, unsigned long, long long, unsigned long long }
