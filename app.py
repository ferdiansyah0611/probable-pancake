import time
from src.core import Core

class Application(Core):

	version = 1
	full = 60

	def initial(self):
		self.beforerun()
		self.clear()
		print(self.logtime(), '#' * self.full)
		print(self.logtime(), '##!!                                                    !!##')
		print(self.logtime(), '##!!             Hacking Tools Application              !!##')
		print(self.logtime(), '##!!                                                    !!##')
		print(self.logtime(), '##!!                   $$$$$$$$$$$$$                    !!##')
		print(self.logtime(), '##!!                 $$$$$$$$$$$$$$$$$                  !!##')
		print(self.logtime(), '##!!                   |           |                    !!##')
		print(self.logtime(), '##!!                  {| [0]   [0] |}                   !!##')
		print(self.logtime(), '##!!                   |    ___    |                    !!##')
		print(self.logtime(), '##!!                   |    !!!    |                    !!##')
		print(self.logtime(), '##!!                   |___________|                    !!##')
		print(self.logtime(), '##!!                                                    !!##')
		print(self.logtime(), '##!!               Dev by Ferdiansyah0611               !!##')
		print(self.logtime(), '##!!                                                    !!##')
		print(self.logtime(), '#' * self.full)
		print(self.logtime(), 'checking python version...')
		self.check()
		time.sleep(0.2)
		print(self.logtime(), 'checking application version...')
		time.sleep(0.2)
		print(self.logtime(), 'checking ip address...')
		ip = self.ip()
		time.sleep(0.2)
		print(self.logtime(),f"IP Address: {ip}")
		print(self.logtime(), 'Enjoy Your Hacking')
		time.sleep(0.2)
		self.run()

if __name__ == '__main__': 
	Application().initial()