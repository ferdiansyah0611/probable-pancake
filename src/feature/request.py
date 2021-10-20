import requests, re

def request(success, logtime, colored):
	url = input(logtime(False) + ' url = ')
	if re.search("https://|http://", r"{}".format(url)) is not None and re.search("/$", r"{}".format(url)) is not None:
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

		success()

	else:
		print(logtime(), colored('URL MUST BE INCLUDE HTTP OR HTTPS, END WITH /', 'red'))
		request(success, logtime, colored)