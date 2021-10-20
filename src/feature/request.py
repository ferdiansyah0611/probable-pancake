import requests, re
from app import Application

class request(Application):
	def __init__(self):
		url = input(super().logtime(False) + ' url = ')
		if re.search("https://|http://", r"{}".format(url)) is not None and re.search("/$", r"{}".format(url)) is not None:
			method = str(input(super().logtime(False) + ' method("get", "post") = ')).lower()
			try:
				if method == 'post':
					data = input(super().logtime(False) + ' data=')
					commit = requests.post(url, data = data)
					print(super().logtime(), commit)
					print(commit.text)
					self.add_request(data = {'url': url, 'last_action': 'yyy', 'response': commit.text})
				else:
					commit = requests.get(url)
					print(super().logtime(), commit)
					print(commit.text)
					self.add_request(data = {'url': url, 'last_action': 'yyy', 'response': commit.text})
			except:
				pass

			super().success()

		else:
			print(super().logtime(), super().colored('URL MUST BE INCLUDE HTTP OR HTTPS, END WITH /', 'red'))
			request(Application)