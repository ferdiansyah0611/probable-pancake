import sys, os, time, socket
from colorama import init
from termcolor import colored

init()

class Core:
	hostname = socket.gethostname()

	def colored(self, msg, color, bg = None, attrs = None):
		return colored(msg, color, bg, attrs)

	def beforerun(self):
		if len(sys.argv) >= 2:
			def version():
				print(self.logtime(), 'version',self.version)
				self.end()
			def update():
				os.system('git pull')
				self.end()
			def helpdef():
				usage = [
					{'name': 'version', 'msg': 'Check The Version'},
					{'name': 'update', 'msg': 'Update Latest Version'},
				]
				print(self.logtime(), 'Usage Hacktools, python manage.py [command]')
				print(self.logtime(), self.colored('COMMAND', 'blue'))
				for data in usage:
					print(self.logtime(), data['name'], '\t:', data['msg'])
				self.end()

			cmd = [
				{'name': 'version', 'action': version},
				{'name': 'update', 'action': update},
				{'name': 'help', 'action': helpdef}
			]
			for i in range(0, len(cmd)):
				if sys.argv[1] == cmd[i]['name']:
					cmd[i]['action']()
					break

	def run(self):
		from src.commandline import commandline
		commandline()

	def end(self):
		sys.exit()

	def clear(self):
		if os.system('cls') == 0:
			os.system('cls')
		if os.system('clear') == 0:
			os.system('clear')

	def check(self):
		if sys.version_info[0] < 3:
			print(self.logtime(), self.colored('python must be v3', 'red'))
			sys.exit()

	def ip(self):
		return socket.gethostbyname(self.hostname)

	def logtime(self, withcolor = True):
		now = time.localtime(time.time())
		if withcolor:
			return self.colored("[{hours}:{minutes}]".format(hours = now.tm_hour, minutes = now.tm_min), 'green') + ':'
		else:
			return "[{hours}:{minutes}]".format(hours = now.tm_hour, minutes = now.tm_min) + ':'

	def exited(self):
		print(self.logtime(), self.colored("Exit The Command. Bye Hacker", "red"))
		sys.exit()

	def success(self):
		tryagain = input(self.logtime(False) + ' write n to stop commandline or anykey to try again: ')
		if tryagain == 'n': sys.exit()
		else:
			from src.commandline import commandline
			commandline()