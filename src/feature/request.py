import requests
from app import logtime
from src.commandline import commandline

def request():
	url = input(logtime(False) + ' url=')
	method = str(input(logtime(False) + ' method("get", "post")=')).lower()
	if method == 'post':
		data = input(logtime(False) + ' data=')
		commit = requests.post(url, data = data)
		print(logtime(), commit)
		print(commit.text)
	else:
		commit = requests.get(url)
		print(logtime(), commit)
		print(commit.text)

	commandline()