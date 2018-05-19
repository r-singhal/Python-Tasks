#!/usr/bin/python

import time
import webbrowser
import urllib

from bs4 import BeautifulSoup
#from google import search
import commands
import requests


print ("enter a choice no")
ch=raw_input()


if ch=='1':
	search_data=raw_input('Enter data :' )
	final_data=search_data.strip()
	done_data=final_data.split()
	for i in done_data:
		webbrowser.open_new_tab('https://www.google.com/search?q='+i)
	
elif ch=='2':
	search_data=raw_input('Enter data :' )
	final_data=search_data.strip()
	done_data=final_data.split()
	for i in done_data:	
		webbrowser.open_new_tab('https://www.google.com/search?tbm=isch&q='+i)
elif ch=='3':
	c=raw_input('Enter data :' )
	url = ("http://www.google.com/search?q=%s"%c)
	response = requests.get(url)
	# parse html
	page = str(BeautifulSoup(response.content))


	def getURL(page):
    		"""

    		:param page: html of web page (here: Python home pa 
    		:return: urls in that page 
    		"""
    		start_link = page.find("a href")
    		if start_link == -1:
        		return None, 0
    		start_quote = page.find('"', start_link)
    		end_quote = page.find('"', start_quote + 1)
		url = page[start_quote + 1: end_quote]
    		return url, end_quote

	while True:
    		url, n = getURL(page)
    		page = page[n:]
    		if url:
        		print (url)
    		else:
       			break
	
elif ch=='4':
	x=time.ctime()
	print x
elif ch=='5':
	webbrowser.open_new_tab('http://www.google.com')
elif ch=='6':
	print commands.getstatusoutput('nmap -sP 192.168.1.0/24')
	print commands.getstatusoutput('arp -a')
elif ch=='7':
	search_data=raw_input('Enter domain name :' )
	webbrowser.open_new_tab('https://who.is/whois/'+search_data)
else:
	print "Enter a choice between 1 to 7 only."


