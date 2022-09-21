import requests, re

def request(url, methods, db, data = dict(), header = dict(), minimize = False):
	if re.search("https://|http://", r"{}".format(url)) is not None and re.search("/$", r"{}".format(url)) is not None:
		method = methods.lower()
		try:
			if method == 'post':
				commit = requests.post(url, data = data, headers=header)
				if minimize == False:
					print(commit.text)
				db.add_request(data = {'url': url, 'response': commit.text})
			else:
				commit = requests.get(url, headers=header)
				if minimize == False:
					print(commit.text)
				check = db.add_request(data = {'url': url, 'response': commit.text})
		except (RuntimeError, TypeError, NameError) as E:
			print(E)
			pass
	else:
		print('Error: URL must be include http or https, end with /')