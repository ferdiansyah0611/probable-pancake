import sys, os, time, socket
from colorama import init
from termcolor import colored
# init color print
init()

def logtime(withcolor = True):
	now = time.localtime(time.time())
	if withcolor:
		return colored("[{hours}:{minutes}]".format(hours = now.tm_hour, minutes = now.tm_min), 'green') + ':'
	else:
		return "[{hours}:{minutes}]".format(hours = now.tm_hour, minutes = now.tm_min) + ':'

class Application:

	version = 1
	full = 60
	hostname = socket.gethostname()

	def __init__(self):
		self.beforerun()
		self.clear()
		print(logtime(), '#' * self.full)
		print(logtime(), '##!!                                                    !!##')
		print(logtime(),f'##!!             {colored("Hacking Tools Application", "white", "on_red", attrs=["bold"])}              !!##')
		print(logtime(), '##!!                                                    !!##')
		print(logtime(), '##!!                   $$$$$$$$$$$$$                    !!##')
		print(logtime(), '##!!                 $$$$$$$$$$$$$$$$$                  !!##')
		print(logtime(), '##!!                   |           |                    !!##')
		print(logtime(), '##!!                  {| [0]   [0] |}                   !!##')
		print(logtime(), '##!!                   |    ___    |                    !!##')
		print(logtime(), '##!!                   |    !!!    |                    !!##')
		print(logtime(), '##!!                   |___________|                    !!##')
		print(logtime(), '##!!                                                    !!##')
		print(logtime(),f'##!!               {colored("Dev by Ferdiansyah0611", "white", "on_red", attrs=["bold"])}               !!##')
		print(logtime(), '##!!                                                    !!##')
		print(logtime(), '#' * self.full)
		print(logtime(), 'checking python version...')
		self.check()
		time.sleep(0.2)
		print(logtime(), 'checking application version...')
		time.sleep(0.2)
		print(logtime(), 'checking ip address...')
		ip = self.ip()
		time.sleep(0.2)
		print(logtime(),f"IP Address: {ip}")
		print(logtime(), 'Enjoy Your Hacking')
		time.sleep(0.2)
		self.run()

	def beforerun(self):
		if len(sys.argv) >= 2:
			def version():
				print(logtime(), 'version',self.version)
				self.end()
			def update():
				os.system('git pull')
				self.end()
			def helpdef():
				usage = [
					{'name': 'version', 'msg': 'Check The Version'},
					{'name': 'update', 'msg': 'Update Latest Version'},
				]
				print(logtime(), 'Usage Hacktools, python manage.py [command]')
				print(logtime(), colored('COMMAND', 'blue'))
				for data in usage:
					print(logtime(), data['name'], '\t:', data['msg'])
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
			print(logtime(), colored('python must be v3', 'red'))
			sys.exit()

	def ip(self):
		return socket.gethostbyname(self.hostname)

if __name__ == '__main__': 
	Application()