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
	# attribute
	version = 1
	full = 60
	hostname = socket.gethostname()
	# init
	def __init__(self):
		if os.system('cls') == 0:
			os.system('cls')
		if os.system('clear') == 0:
			os.system('clear')
		print(logtime(), '#' * self.full)
		print(logtime(), '##!!                                                    !!##')
		print(logtime(), f'##!!             {colored("Hacking Tools Application", "white", "on_red", attrs=["bold"])}              !!##')
		print(logtime(), '##!!                                                    !!##')
		print(logtime(), '##!!                   $$$$$$$$$$$$$                    !!##')
		print(logtime(), '##!!                 $$$$$$$$$$$$$$$$$                  !!##')
		print(logtime(), '##!!                   |           |                    !!##')
		print(logtime(), '##!!                  {| [0]   [0] |}                   !!##')
		print(logtime(), '##!!                   |    ___    |                    !!##')
		print(logtime(), '##!!                   |    !!!    |                    !!##')
		print(logtime(), '##!!                   |___________|                    !!##')
		print(logtime(), '##!!                                                    !!##')
		print(logtime(), f'##!!               {colored("Dev by Ferdiansyah0611", "white", "on_red", attrs=["bold"])}               !!##')
		print(logtime(), '##!!                                                    !!##')
		print(logtime(), '#' * self.full)
		print(logtime(), 'checking python version...')
		if sys.version_info[0] < 3:
			print(logtime(), colored('python must be v3', 'red'))
			sys.exit()
		time.sleep(0.2)
		print(logtime(), 'checking application version...')
		time.sleep(0.2)
		print(logtime(), 'checking ip address...')
		ip = socket.gethostbyname(self.hostname)
		time.sleep(0.2)
		print(logtime(), f"IP Address: {ip}")
		print(logtime(), 'Enjoy Your Hacking')
		time.sleep(0.2)
		self.run()

	def run(self):
		from src.commandline import commandline
		commandline()

if __name__ == '__main__': 
	Application() 
