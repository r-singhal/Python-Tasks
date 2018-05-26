#!/usr/bin/python2

import os
import sys
inn=sys.argv
file_name = inn[1]
path = inn[2]

for root, dirs, files in os.walk(path):  #traversing to the path where file is to be created
    if file_name in files:
        f=open(file_name, 'r+')
        print(f.read())
        break
    else:
        f=open(file_name, 'w+')


