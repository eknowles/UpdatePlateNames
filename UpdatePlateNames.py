#!/usr/bin/python

import os

folder = "C:\Users\Edward\Desktop\PLATES"
os.chdir(folder)

def nicenumber(datnum):
	prefix = ''
	if datnum < 100:
		prefix = '0'
	if datnum < 10:
		prefix = '00'

	return 'image' + prefix + str(datnum) + '.jpg'

numberoffiles = len(os.walk(folder).next()[2])
nicenumberoffiles = nicenumber(numberoffiles)
os.rename('image000.jpg', nicenumberoffiles)