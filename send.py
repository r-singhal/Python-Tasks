#!/usr/bin/python

import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 4>2:
	msg=raw_input('Enter msg to send: ')
	s.sendto(msg,("127.0.0.1",9999))



	print s.recvfrom(1000)
