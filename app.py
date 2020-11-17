import sys
import time
import socket
import mechanize
from colorama import Fore, init
from termcolor import colored
# init color print
init()
# start app
class App:
    # attribute
    version = 1
    socialmedia = [
        'Facebook',
        'Twitter (Coming Soon)',
        'Instagram (Coming Soon)',
        'Google (Coming Soon)',
        'Yahoo (Coming Soon)',
        'Spam Chat Whatsapp (Coming Soon)',
        'Bot Whatsapp (Coming Soon)',
        'Custom Bruteforce (Coming Soon)'
    ]
    full = 54
    hostname = socket.gethostname()
    # init
    def __init__(self):
        if sys.version_info[0] != 3:
            sys.exit()
        else:
            print('#' * self.full)
            print('##!!                                              !!##')
            print(f'##!!         {colored("Hacking and Bot Application", "white", "on_red", attrs=["bold"])}          !!##')
            print('##!!                                              !!##')
            print('##!!                $$$$$$$$$$$$$                 !!##')
            print('##!!              $$$$$$$$$$$$$$$$$               !!##')
            print('##!!                |           |                 !!##')
            print('##!!               {| [0]   [0] |}                !!##')
            print('##!!                |    ___    |                 !!##')
            print('##!!                |    !!!    |                 !!##')
            print('##!!                |___________|                 !!##')
            print('##!!                                              !!##')
            print(f'##!!            {colored("Dev by Ferdiansyah0611", "white", "on_red", attrs=["bold"])}            !!##')
            print('##!!                                              !!##')
            print('#' * self.full)
            print(colored('checking python version...', 'green'))
            time.sleep(1)
            print(colored('checking application version...', 'green'))
            time.sleep(1)
            print(colored('checking url...', 'green'))
            time.sleep(1)
            print(colored('checking ip address...', 'green'))
            ip = socket.gethostbyname(self.hostname)
            time.sleep(1)
            print('-' * self.full)
            print('Enjoy Your Hacking')
            print(f"IP Address: {ip}")
            print('')
            time.sleep(1)
    # start app
    def start(self):
        try:
            print('|List Of Vulnerability Hacking & Bot: ')
            i = 0
            for listsocial in self.socialmedia:
                i += 1
                print(f"| {str(i)}. {listsocial}")
            print('')
            print('|For Helping: ')
            print('| -h : Helping')
            print('| -d : Debug Report')
            print('')
            choosebrute = str(input(f'{self.hostname}> ')).split(' ')
            if choosebrute:
                if(len(choosebrute) == 2):
                    # for helping
                    if choosebrute[0] == '1' and choosebrute[1] == '-h':
                        print('-' * self.full)
                        print('|Help For Facebook')
                        print('| email    : Email Target For Bruteforce. In email must be have @/./@gmail.com/@yahoo.com')
                        print('| type     : Type Bruteforce. -a is auto password or -m after -m is manual adding password')
                        print('| password : Must be fillable if you choose type -m.')
                        print('-' * self.full)
                        print('CommandExample> 1 {email} {type} {password}')
                    if choosebrute[0] and choosebrute[1] == '-d':
                        try:
                            import webbrowser as browser
                            openbrowser = input('Dou You Want Open Browser Now ? (Y/N) ')
                            if openbrowser == 'Y' or openbrowser == 'y':
                                browser.open('https://github.com')
                            pass
                        except Exception as e:
                            print('Please Instal Webbrowser. Do You Want Install Now ?')
                if(len(choosebrute) == 3):
                    from src.facebook import Facebook
                    if choosebrute[0] == '1' and choosebrute[2] == '-a': Facebook(choosebrute[1], 'auto').run()
                    if choosebrute[0] == '1' and choosebrute[2] == '-m': Facebook(choosebrute[1], 'manual', choosebrute[3]).run()
                if choosebrute[0] == '2': print(colored("Message : Sorry This Feature Is Coming Soon", "white", "on_cyan", attrs=["bold"]))
                if choosebrute[0] == '3': print(colored("Message : Sorry This Feature Is Coming Soon", "white", "on_cyan", attrs=["bold"]))
                if choosebrute[0] == '4': print(colored("Message : Sorry This Feature Is Coming Soon", "white", "on_cyan", attrs=["bold"]))
                if choosebrute[0] == '5': print(colored("Message : Sorry This Feature Is Coming Soon", "white", "on_cyan", attrs=["bold"]))
                if choosebrute[0] == '6': print(colored("Message : Sorry This Feature Is Coming Soon", "white", "on_cyan", attrs=["bold"]))
                if choosebrute[0] == '7': print(colored("Message : Sorry This Feature Is Coming Soon", "white", "on_cyan", attrs=["bold"]))
            else:
                sys.exit()
            pass
        except Exception as e:
            print(f"Erorr : {e}")
# call app
App().start()