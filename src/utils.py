import sqlite3
from datetime import datetime

class Database:
	def __init__(self):
		self.connect = sqlite3.connect('db.sqlite3')
		self.execute = self.connect.execute
		self.init()
	def init(self):
		self.execute('''CREATE TABLE IF NOT EXISTS FACEBOOK
		(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			email TEXT NOT NULL,
			last_action TEXT NOT NULL,
			password TEXT NULL
		)
		''')
		self.execute('''CREATE TABLE IF NOT EXISTS DDOS
		(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			ip TEXT NOT NULL,
			last_action TEXT NOT NULL,
			total_payload TEXT NULL
		)
		''')
		self.execute('''CREATE TABLE IF NOT EXISTS REQUEST
		(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			url TEXT NOT NULL,
			last_action TEXT NOT NULL,
			response TEXT NULL
		)
		''')
		self.execute('''CREATE TABLE IF NOT EXISTS ZIP
		(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL,
			last_action TEXT NOT NULL,
			password TEXT NULL
		)
		''')
	def add_facebook(self, data):
		email = data['email']
		last_action = datetime.now()
		password = data['password']
		self.execute(f"INSERT INTO FACEBOOK (email, last_action, password) VALUES ('{email}', '{last_action}', '{password}')")
		self.connect.commit()

	def add_ddos(self, data):
		ip = data['ip']
		last_action = datetime.now()
		total_payload = data['total_payload']
		self.execute(f"INSERT INTO DDOS (ip, last_action, total_payload) VALUES ('{ip}', '{last_action}', '{total_payload}')")
		self.connect.commit()
		data = self.execute(f'SELECT * FROM ddos ORDER BY id DESC LIMIT 1')
		response = data.fetchall()
		if len(response):
			return response[0]

	def add_request(self, data):
		url = data['url']
		last_action = datetime.now()
		response = data['response']
		self.execute(f"INSERT INTO REQUEST (url, last_action, response) VALUES ('{url}', '{last_action}', '{response}')")
		self.connect.commit()

	def add_zip(self, data):
		name = data['name']
		last_action = datetime.now()
		password = data['password']
		self.execute(f"INSERT INTO ZIP (name, last_action, password) VALUES ('{name}', '{last_action}', '{password}')")
		self.connect.commit()

	def update_ddos(self, data):
		last_action = datetime.now()
		total_payload = data['total_payload']
		self.execute(f"UPDATE DDOS SET `total_payload`='{total_payload}' WHERE `id`={data['id']}")
		self.connect.commit()
		
	def get(self, name, page, total):
		name = name.upper()
		offset = total
		if page == 0:
			offset = total * page + total

		data = self.execute(f'SELECT * FROM {name} LIMIT {page * total}, {offset}')
		return data.fetchall()

	def delete(self, name, _id):
		name = name.upper()
		self.execute(f"DELETE FROM {name} WHERE `id`={_id}")
		self.connect.commit()