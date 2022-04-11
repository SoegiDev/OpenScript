#! /usr/bin/python3

import sys
import shutil
import glob
import json
import os
import argparse
from pathlib  import Path

def tojson(source : str, dest : str =None):
	f = open(source,'r')
	content = f.read()
	splitcontent = content.splitlines()
	d=[]
	for v in splitcontent:
		l = v.split(' | ')
		d.append(dict(s.split(':',1) for s in l))

	if dest is None:
		with open(source.split(".")[0]+'.json','w') as fileout:
			fileout.write((json.dumps(d,indent=4,sort_keys=False)))
	else:
		with open(dest,'w') as fileout:
			fileout.write((json.dumps(d,indent=4,sort_keys=False)))

def fungsiOne():
	datafile = str(sys.argv[1])
	split = datafile.split(".")
	shutil.copy(datafile.split[0]+".txt")


if  sys.argv[1] != '-h':
	if sys.argv[2] == '-t':
		datafile = str(sys.argv[1])
		if sys.argv[3] == 'text':
			split = datafile.split(".")
			shutil.copy(datafile,split[0]+'.txt')
		elif sys.argv[3] == 'json':
			#print(f"sadas",len(sys.argv))
			if len(sys.argv) <= 4:
				tojson(datafile)
			else :
				destination = str(sys.argv[5])
				tojson(datafile,destination)
		elif sys.argv[3] != 'text' or sys.argv[3] != 'json':
			print("Type data tidak dikenali")

	elif sys.argv[2] == "-o" :
		datafile = str(sys.argv[1])
		destination = str(sys.argv[3])
		try:
			shutil.copy(datafile,destination)
		except IOError as e:
			print("Directory Tidak ada")
			
	elif str(sys.argv[2]) != 't' or str(sys.argv[2]) != '-o':
		print("Format fungsi tidak dikenali")

elif sys.argv[1] == '-h':
	parser = argparse.ArgumentParser()
	parser.add_argument("[source] -t typedata(text/json)",help="Copy data di folder yang sama")
	parser.add_argument("[source] -o [destination]",help="Copy data di folder yang berbeda hanya text")
	parser.add_argument("[source] -t json -o [destination]", help="Copy data di folder yang berbeda json")
	args = parser.parse_args()


#print("THIS IS THE NAME OF THE PROGRAM :",sys.argv[1])

