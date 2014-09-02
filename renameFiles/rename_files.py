#!/usr/bin/env python

import os

def rename_files():
	file_list = os.listdir(r"/home/usuario/Desktop/workspacepython")
	print (file_list)
	saved_path = os.getcwd()
	os.chdir(r"/home/usuario/Desktop/workspacepython")

	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,"0123456789"))
	
	os.chdir(save_path)

rename_files()
