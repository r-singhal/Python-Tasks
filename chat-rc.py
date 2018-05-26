#!/usr/bin/env python

import socket 
import thread

i=1

rec_ip="192.168.10.137"
myport=8888
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((rec_ip, myport))

x=raw_input("Enter your name: ")
s.sendto(x,("127.0.0.1",8888))
d=s.recvfrom(100)

def rc():
	while True:
		y=s.recvfrom(1000)
		print (d[0]+":"+y[0])

def sc():
	while True:
		a=raw_input()
		s.sendto(a,("127.0.0.1",8888))

thread.start_new_thread(rc,())

thread.start_new_thread(sc,())

while True:
	pass
