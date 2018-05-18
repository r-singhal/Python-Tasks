#!/usr/bin/python
import commands
import socket
rec_ip="127.0.0.1"
myport=9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((rec_ip,myport))
while(4>2):
	data=s.recvfrom(1000)
	print 'data from client: '+data[0]
	print 'ip of client: '+data[1][0]
	
	rply=raw_input('plz type your reply: ')
	s.sendto(rply,data[1])
