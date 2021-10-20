from app import logtime, colored, socket, sys

def exited():
	print(logtime(), colored("Exit The Command. Bye Hacker", "red"))
	sys.exit()

def success():
	tryagain = input(logtime(False) + ' write n to stop commandline or anykey to try again: ')
	if tryagain == 'n': sys.exit()
	else:
		commandline()

def commandline():
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
	print(logtime(), colored("List Command Line Application", "blue"))

	for d in feature:
		print(logtime(), '[{}] {}'.format(i, d))
		i += 1

	choose = input(logtime(False) + ' ')

	if choose == "0":
		exited()

	if choose == "1":
		from src.feature.request import request
		request(success = success, logtime = logtime, colored = colored)

	if choose == "2":
		from src.feature.ddos import DDOS
		DDOS()

	if choose == "3":
		host = input(logtime(False) + ' hostname = ')
		ip = socket.gethostbyname(host)
		print(logtime(), ip)
		success()

	if choose == "4":
		from src.facebook import Facebook
		emailorphone = str(input(logtime(False) + ' email = ')).lower()
		execute = str(input(logtime(False) + ' type(auto/manual) = ')).lower()
		if execute == 'manual':
			pw = input(logtime(False) + ' password=')
			Facebook(emailorphone, execute, colored = colored, password=pw)
		else:
			customfile = str(input(logtime(False) + ' custom wordlist *default(passwords.txt) = '))
			Facebook(emailorphone, execute, customfile = customfile, colored = colored)

	if choose == "5":
		from src.feature.zipper import ZIP
		ZIP(success = success, colored = colored, logtime = logtime)

	if choose == "6":
		from src.feature.checkport import Checkport
		Checkport(colored = colored, logtime = logtime, success = success)

	else:
		exited()