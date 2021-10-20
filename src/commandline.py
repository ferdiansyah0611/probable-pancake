from app import Application
import socket

class Action(Application):
	def actionrequest(self):
		from src.feature.request import request
		request()
	def actionddos(self):
		from src.feature.ddos import DDOS
		DDOS()
	def actioncheckip(self):
		host = input(super().logtime(False) + ' hostname = ')
		ip = socket.gethostbyname(host)
		print(super().logtime(), ip)
		super().success()
	def actionfacebook(self):
		from src.feature.facebook import Facebook
		emailorphone = str(input(super().logtime(False) + ' email = ')).lower()
		execute = str(input(super().logtime(False) + ' type(auto/manual) = ')).lower()
		if execute == 'manual':
			pw = input(super().logtime(False) + ' password=')
			Facebook(emailorphone, execute, password=pw)
		else:
			customfile = str(input(super().logtime(False) + ' custom wordlist *default(passwords.txt) = '))
			Facebook(emailorphone, execute, customfile = customfile)
	def actionzip(self):
		from src.feature.zipper import ZIP
		ZIP()
	def actioncheckport(self):
		from src.feature.checkport import Checkport
		Checkport()
	def showrequest(self):
		data = super().get_request()
		for row in data:
			print(row[0])

class commandline(Application):
	def __init__(self):
		feature = [
			"Exit Command",
			"Request API",
			"DDOS Server",
			"Check IP Server",
			"Facebook Bruteforce",
			"Zip Bruteforce",
			"Check Port Server"
		]
		i = 0
		print(self.logtime(), super().colored("List Command Line Application", "blue"))

		for d in feature:
			print(super().logtime(), '[{}] {}'.format(i, d))
			i += 1

		choose = input(super().logtime(False) + ' ')

		action = Action()
		chooselist = [
			{'name': '0', 'action': self.exited},
			{'name': '1', 'action': action.actionrequest},
			{'name': '2', 'action': action.actionddos},
			{'name': '3', 'action': action.actioncheckip},
			{'name': '4', 'action': action.actionfacebook},
			{'name': '5', 'action': action.actionzip},
			{'name': '6', 'action': action.actioncheckport},
			{'name': 'show request', 'action': action.showrequest}
		]
		selected = False
		for _ in chooselist:
			if choose == _['name']:
				_['action']()
				selected = True
				break

		if selected == False:
			self.exited()