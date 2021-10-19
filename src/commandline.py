from app import logtime, colored, socket, sys

def commandline():
	feature = [
		"Exit Command",
		"Request API",
		"Facebook Bruteforce",
		"DDOS Server",
		"Check IP Server"
	]
	i = 0
	print(logtime(), colored("List Command Line Application", "blue"))

	for d in feature:
		print(logtime(), '{}. {}'.format(i, d))
		i += 1

	choose = input(logtime(False) + ' ')

	if choose == "0":
		print(logtime(), colored("Exit The Command. Bye Hacker", "red"))
		sys.exit()

	if choose == "1":
		from src.feature.request import request
		request()

	if choose == "2":
		from src.facebook import Facebook
		emailorphone = input(logtime(False) + ' email/phone=')
		execute = input(logtime(False) + ' type("auto", "manual")=').lower()
		if execute == 'manual':
			pw = input(logtime(False) + ' password=')
			Facebook(emailorphone, execute, pw)
		else:
			Facebook(emailorphone, execute)

	if choose == "3":
		from src.feature.ddos import DDOS
		DDOS()

	if choose == "4":
		host = input(logtime(False) + ' hostname=')
		ip = socket.gethostbyname(host)
		print(logtime(), ip)
		tryagain = input(logtime(False) + ' write n to stop commandline or anykey to try again: ')
		if tryagain == 'n': sys.exit()
		else:
			commandline()