import socket
from app import Application

class Checkport(Application):
	def __init__(self):
		ip = str(input(super().logtime(False) + ' ip = '))
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		portlist = [
			{'name': 'ftp', 'port': 20},
			{'name': 'ftp', 'port': 21},
			{'name': 'http', 'port': 80},
			{'name': 'https', 'port': 443},
			{'name': 'ssh', 'port': 22},
			{'name': 'telnet', 'port': 23},
			{'name': 'smtp', 'port': 25},
			{'name': 'dns', 'port': 53},
			{'name': 'dhcp', 'port': 67},
			{'name': 'dhcp', 'port': 68},
			{'name': 'pop3', 'port': 110},
			{'name': 'nntp', 'port': 119},
			{'name': 'ntp', 'port': 123},
			{'name': 'remote dekstop protocol', 'port': 3389},
		]
		for port in portlist:
			locate = (ip, port['port'])
			result = sock.connect_ex(locate)
			if result == 0:
				print(super().logtime(), port['name'], '->', super().colored('open', 'green'))
			else:
				print(super().logtime(), port['name'], '->', super().colored('closed', 'red'))

		super().success()