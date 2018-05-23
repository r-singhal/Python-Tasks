#!/usr/bin/python2

import cgi

print "content-type:text/html"
print ""

web_data=cgi.FieldStorage()
print web_data.getvalue('x')
