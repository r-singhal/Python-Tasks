#!/usr/bin/python3
import os   #file management module
import sys


inn=sys.argv

file_name= (inn[1]) #input as an argument)


f=open(file_name, 'r')  #opening file in read mode


print(f.read())


