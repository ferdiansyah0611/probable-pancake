import sqlite3
# from app import Application

class Database:

	def __init__(self):
		self.connect = sqlite3.connect('db.sqlite3')
		self.execute = self.connect.execute
		self.init()

	def init(self):
		self.execute('''CREATE TABLE IF NOT EXISTS FACEBOOK
		(
			id INT PRIMARY KEY NOT NULL,
			email TEXT NOT NULL,
			last_action TEXT NOT NULL,
			password TEXT NULL
		)
		''')
		self.execute('''CREATE TABLE IF NOT EXISTS DDOS
		(
			id INT PRIMARY KEY NOT NULL,
			ip TEXT NOT NULL,
			last_action TEXT NOT NULL,
			total_payload TEXT NULL
		)
		''')
		self.execute('''CREATE TABLE IF NOT EXISTS REQUEST
		(
			id INT PRIMARY KEY NOT NULL,
			url TEXT NOT NULL,
			last_action TEXT NOT NULL,
			response TEXT NULL
		)
		''')
	def add_facebook(self, data):
		# _id = data['id']
		email = data['email']
		last_action = data['last_action']
		password = data['password']
		self.execute(f"INSERT INTO FACEBOOK (email, last_action, password) VALUES ('{email}', '{last_action}', '{password}')")
		self.connect.commit()

	def add_ddos(self, data):
		# _id = data['id']
		ip = data['ip']
		last_action = data['last_action']
		total_payload = data['total_payload']
		self.execute(f"INSERT INTO DDOS (email, last_action, password) VALUES ('{ip}', '{last_action}', '{total_payload}')")
		self.connect.commit()

	def add_request(self, data):
		# _id = data['id']
		url = data['url']
		last_action = data['last_action']
		response = data['response']
		self.execute(f"INSERT INTO REQUEST (email, last_action, password) VALUES ('{url}', '{last_action}', '{response}')")
		self.connect.commit()


	def get_request(self):
		data = self.execute('SELECT * FROM REQUEST')
		return data