from tkinter import *
from tkinter import ttk, filedialog
import os

color = {
	'primary': '#464646',
	'secondary': '#6F6F6F',
	'danger': '#C62828',
	'primary.btn': '#1565C0'
}

style_btn_primary = {
	'bg': color['primary.btn'],
	'activebackground': color['primary.btn'],
	'foreground': 'white',
	'activeforeground': 'white'
}

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
	def bruteforce_fb(self, email, manual, password):
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

class Gui():
	widget = []
	def __init__(self):
		self.action = Action()
		self.root = Tk()
		self.style = ttk.Style()
		self.style.configure('W.TButton', font=('Arial', 8 ))
		self.style.configure('Run.TButton', bg='#1565C0', font=('Arial', 10 ))
		self.style.configure('A.TFrame', background=color['secondary'])
		self.style.configure('TLabel', background=color['secondary'], foreground='white')
		self.style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
		self.style.configure("Treeview.Heading", font=('Calibri', 13,'bold'))
		self.root.configure(bg=color['primary'])
		self.root.title("HackTools By ferdiansyah0611")
		self.root.geometry('430x250-5+40')
		# state
		self.active = StringVar()
		self.active.trace('w', self.trace_active)
		# template
		self.mainframe = Frame(self.root, bg=color['primary'], padx=12, pady=5, relief="groove", borderwidth=2)
		self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		# start
		self.action_btn()
		self.bruteforce_fb()
		self.root.mainloop()
	def make_frame2(self):
		self.mainframe2 = ttk.Frame(self.root, padding="12 12 12 12", style='A.TFrame')
		self.mainframe2.grid(column=2, row=0, sticky=(N, W, E, S))
	def trace_active(self, a, b, c):
		active = self.active.get()
		self.mainframe2.destroy()
		if active == 'Request':
			self.request()
		if active == 'IP Port':
			self.ip_port()
		if active == 'IP Check':
			self.ip_port(True)
		if active == 'DDOS':
			self.ddos()
		if active == 'Bruteforce Facebook':
			self.bruteforce_fb()
		if active == 'Bruteforce ZIP':
			self.bruteforce_zip()
	def make_empty_row(self, column, row):
		ttk.Label(self.mainframe2, text='').grid(column=column, row=row)

	def action_btn(self):
		def maker(arg):
			text = arg[0]
			column = arg[1]
			row = arg[2]
			event = lambda x: True

			if len(arg) == 4:
				event = arg[3]

			def action_event():
				self.active.set(text)

			styled = {
				'bg': '#464646',
				'foreground': 'white',
				'activebackground': '#616060',
				'activeforeground': 'white',
				'font': ('Arial', 8),
				'relief': 'ridge'
			}
			btn = Button(self.mainframe, text=text, command=action_event, **styled)
			btn.grid(column=column, row=row, sticky=[N, E, S, W], padx=2, pady=2)

		listing = [
			("Bruteforce Facebook", 0, 1),
			("Bruteforce ZIP", 0, 2),
			("DDOS", 0, 3),
			("IP Check", 0, 4),
			("IP Port", 0, 5),
			("Request", 0, 6),
		]

		label = Label(self.mainframe, text='Action', bg='#464646', foreground='white')
		label.grid(column=0, row=0)
		for btn in listing:
			maker(btn)

	def bruteforce_zip(self):
		self.make_frame2()
		# state
		filename_zip = StringVar()
		filename_list = StringVar()
		# action
		def run():
			self.action.bruteforce_zip(filename_zip.get(), filename_list.get())
		def password_list():
			filename_list.set(filedialog.askopenfilename())
		def zip_action():
			filename_zip.set(filedialog.askopenfilename())
		# element
		Button(self.mainframe2, text='Select ZIP', command=zip_action, background=color['danger'], activebackground=color['danger'], foreground='white', activeforeground='white').grid(column=0, row=1, sticky=[N, E, S, W], padx=5, pady=5)
		Button(self.mainframe2, text='Select Password List', command=password_list, background=color['danger'], activebackground=color['danger'], foreground='white', activeforeground='white').grid(column=0, row=2, sticky=[N, E, S, W], padx=5, pady=5)

		self.make_empty_row(column=1, row=4)
		self.make_empty_row(column=1, row=5)
		self.make_empty_row(column=1, row=6)
		self.make_empty_row(column=1, row=7)

		Button(self.mainframe2, text='Run', command=run, **style_btn_primary).grid(column=0, row=8, sticky=[N, E, S, W], padx=5, pady=5)

	def bruteforce_fb(self):
		self.make_frame2()
		# state
		email = StringVar()
		manual = StringVar()
		filename = None
		# action
		def run():
			self.action.bruteforce_fb(email.get(), manual.get(), filename)
		def password_list():
			filename = filedialog.askopenfilename()
		# element
		ttk.Label(self.mainframe2, text='Email').grid(column=1, row=0, sticky=[N, E, S, W], padx=5)
		ttk.Entry(self.mainframe2, textvariable=email).grid(column=1, row=1, padx=5)
		ttk.Label(self.mainframe2, text='Customize Password').grid(column=1, row=2, sticky=[N, E, S, W], padx=5)
		ttk.Entry(self.mainframe2, textvariable=manual).grid(column=1, row=3, padx=5)

		ttk.Label(self.mainframe2, text='').grid(column=1, row=4, rowspan=1)
		ttk.Label(self.mainframe2, text='').grid(column=1, row=5, rowspan=1)
		ttk.Label(self.mainframe2, text='').grid(column=1, row=6, rowspan=1)
		ttk.Label(self.mainframe2, text='').grid(column=1, row=7, rowspan=1)

		Button(self.mainframe2, text='Run', command=run, **style_btn_primary).grid(column=1, row=8, sticky=[N, E, S, W], padx=5, pady=5)
		btn_select = Button(self.mainframe2, text='Select Password List', command=password_list, background=color['danger'], activebackground=color['danger'], foreground='white', activeforeground='white')
		btn_select.grid(column=3, row=8, sticky=N, padx=5, pady=5)

	def ddos(self):
		self.make_frame2()
		# state
		ip = StringVar()
		port = IntVar()
		# action
		def run():
			self.action.ddos(ip.get(), port.get())
		# element
		ttk.Label(self.mainframe2, text='IP Address').grid(column=1, row=0, sticky=[N, E, S, W], columnspan=2, padx=5)
		ttk.Entry(self.mainframe2, textvariable=ip).grid(column=1, row=1, columnspan=2, padx=5)
		ttk.Label(self.mainframe2, text='Port (Optional)').grid(column=1, row=2, sticky=[N, E, S, W], columnspan=2, padx=5)
		ttk.Entry(self.mainframe2, textvariable=port).grid(column=1, row=3, columnspan=2, padx=5)

		self.make_empty_row(column=1, row=4)
		self.make_empty_row(column=1, row=5)
		self.make_empty_row(column=1, row=6)
		self.make_empty_row(column=1, row=7)

		Button(self.mainframe2, text='Run', command=run, **style_btn_primary).grid(column=1, row=8, columnspan=2, sticky=[N, E, S, W], padx=5, pady=5)

	def ip_port(self, is_ip_check = False):
		self.make_frame2()
		# state
		ip = StringVar()
		# action
		def run():
			if is_ip_check:
				self.action.ip_check(ip.get())
			else:
				self.action.ip_port(ip.get())
		# element
		text = 'IP Address'
		if is_ip_check:
			text = 'Hostname'
		ttk.Label(self.mainframe2, text=text).grid(column=1, row=0, sticky=[N, E, S, W], columnspan=2, padx=5)
		ttk.Entry(self.mainframe2, textvariable=ip).grid(column=1, row=1, columnspan=2, padx=5)

		self.make_empty_row(column=1, row=2)
		self.make_empty_row(column=1, row=3)
		self.make_empty_row(column=1, row=4)
		self.make_empty_row(column=1, row=5)
		self.make_empty_row(column=1, row=6)
		self.make_empty_row(column=1, row=7)

		Button(self.mainframe2, text='Run', command=run, **style_btn_primary).grid(column=1, row=8, columnspan=2, sticky=[N, E, S, W], padx=5, pady=5)

	def request(self):
		self.make_frame2()
		# state
		url = StringVar()
		data = StringVar()
		method = StringVar()
		header = StringVar()
		# action
		def run():
			self.action.request(url.get(), method.get(), data.get(), header.get())
		# element
		ttk.Label(self.mainframe2, text='URL').grid(column=1, row=0, sticky=[N, E, S, W], columnspan=2, padx=5)
		ttk.Entry(self.mainframe2, textvariable=url).grid(column=1, row=1, columnspan=2, padx=5)
		ttk.Label(self.mainframe2, text='Methods').grid(column=1, row=2, sticky=[N, E, S, W], columnspan=2, padx=5)
		
		first_position = 3
		for methods in ['Get', 'Post', 'Put', 'Delete']:
			ttk.Radiobutton(self.mainframe2, text=methods, variable=method, value=methods.lower()).grid(column=1, row=first_position, sticky=[N, E, S, W], columnspan=2, padx=5)
			first_position += 1

		ttk.Label(self.mainframe2, text='Data').grid(column=3, row=0, sticky=[N, E, S, W], padx=5)
		ttk.Entry(self.mainframe2, textvariable=data).grid(column=3, row=1, padx=5)
		ttk.Label(self.mainframe2, text='Header').grid(column=3, row=2, sticky=[N, E, S, W], padx=5)
		ttk.Entry(self.mainframe2, textvariable=data).grid(column=3, row=3, padx=5)
		ttk.Label(self.mainframe2, text='').grid(column=1, row=7, rowspan=1, columnspan=2)
		Button(self.mainframe2, text='Run', command=run, **style_btn_primary).grid(column=1, row=8, columnspan=2, sticky=[N, E, S, W], padx=5, pady=5)

if __name__ == '__main__':
	Gui()