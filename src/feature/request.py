import requests, re
from app import logtime, colored
from src.commandline import commandline

def request():
	url = input(logtime(False) + ' url = ') + "\r"
	if re.search("https://|http://", r"{}".format(url)) is not None:
		method = str(input(logtime(False) + ' method("get", "post") = ')).lower()
		try:
			if method == 'post':
				data = input(logtime(False) + ' data=')
				commit = requests.post(url, data = data)
				print(logtime(), commit)
				print(commit.text)
			else:
				commit = requests.get(url)
				print(logtime(), commit)
				print(commit.text)
		except:
			print(logtime(), colored("Could Not Resolve", "red"))

		commandline()

	else:
		print(logtime(), colored('URL MUST BE INCLUDE HTTP OR HTTPS', 'red'))
		request()