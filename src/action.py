import os

class Action():
	def request(self, url, method, data = None, header = None):
		text = f'start cmd /k py app.py request {url} {method}'
		if data:
			text += f' --data {data}'
		if header:
			text += f' --header {header}'
		os.system(text)
	def ip_port(self, ip):
		os.system(f'start cmd /k py app.py ip:port {ip}')
	def ip_check(self, ip):
		os.system(f'start cmd /k py app.py ip:check {ip}')
	def ddos(self, ip, port):
		if port:
			os.system(f'start cmd /k py app.py ddos {ip} {port}')
		else:
			os.system(f'start cmd /k py app.py ddos {ip}')
	def bruteforce_fb(self, email, manual=None, password=None):
		if manual:
			return os.system(f'start cmd /k py app.py bruteforce:fb {email} --manual {manual}')
		if password:
			return os.system(f'start cmd /k py app.py bruteforce:fb {email} --password {password}')
		else:
			return os.system(f'start cmd /k py app.py bruteforce:fb {email}')
	def bruteforce_zip(self, zips, password_list):
		if password_list:
			os.system(f'start cmd /k py app.py bruteforce:zip {zips} {password_list}')
		else:
			os.system(f'start cmd /k py app.py bruteforce:zip {zips}')
	def bruteforce_ftp(self, host, user, password_list, port):
		text = f'start cmd /k py app.py bruteforce:ftp {host} {user}'
		if password_list:
			text += f' --password_list {password_list}'
		if port:
			text += f' --port {port}'
		print(text)
		os.system(text)