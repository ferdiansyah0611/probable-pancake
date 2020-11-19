import sys, os, time, socket, optparse
from colorama import init
from termcolor import colored
# init color print
init()
# start app
class App:
    # attribute
    version = 1
    full = 60
    hostname = socket.gethostname()
    # init
    def __init__(self):
        if sys.version_info[0] != 3:
            sys.exit()
        else:
            print('#' * self.full)
            print('##!!                                                    !!##')
            print(f'##!!            {colored("Hacking and Bot Application", "white", "on_red", attrs=["bold"])}             !!##')
            print('##!!                                                    !!##')
            print('##!!                   $$$$$$$$$$$$$                    !!##')
            print('##!!                 $$$$$$$$$$$$$$$$$                  !!##')
            print('##!!                   |           |                    !!##')
            print('##!!                  {| [0]   [0] |}                   !!##')
            print('##!!                   |    ___    |                    !!##')
            print('##!!                   |    !!!    |                    !!##')
            print('##!!                   |___________|                    !!##')
            print('##!!                                                    !!##')
            print(f'##!!               {colored("Dev by Ferdiansyah0611", "white", "on_red", attrs=["bold"])}               !!##')
            print('##!!                                                    !!##')
            print('#' * self.full)
            print(colored('checking python version...', 'green'))
            time.sleep(0.4)
            print(colored('checking application version...', 'green'))
            time.sleep(0.4)
            print(colored('checking url...', 'green'))
            time.sleep(0.4)
            print(colored('checking ip address...', 'green'))
            ip = socket.gethostbyname(self.hostname)
            time.sleep(0.4)
            print('-' * self.full)
            print('Enjoy Your Hacking')
            print(f"IP Address: {ip}")
            print('')
            time.sleep(0.4)

def Main(): 
    parser = optparse.OptionParser("usage: %prog [options] arg")
    parser.add_option('-e', action="store", default=False, type='string', dest='email', help='email target of bruteforce')
    parser.add_option('-c', action="store", default=False, type='float', dest='choose', help='choose type target of bruteforce')
    parser.add_option('-t', action="store", default=False, type='string', dest='type', help='choose type of bruteforce')
    parser.add_option('-v', action='store_false', default=False, dest='version', help='check version library')
    parser.add_option('-p', action='store', default=False, dest='password', help='if choose manual you must be fillable password')
    group = optparse.OptionGroup(parser, "Example", "python app.py -e admin@server.domain -c 1 -t a")
    parser.add_option_group(group)
    (options, args) = parser.parse_args()
    if options.version != False:
        print('Version ', options.version)
    if options.email != False and options.choose != False and options.type !=  False:
        os.system('cls')
        # Facebook Bruteforce
        if options.choose == 1:
            # auto bruteforce
            if options.type == 'a':
                App()
                from src.facebook import Facebook
                Facebook(options.email, 'auto').run()
            # manual bruteforce
            if options.type == 'm':
                if options.password != False:
                    App()
                    from src.facebook import Facebook
                    Facebook(options.email, 'manual', options.password).run()
        if options.choose > 1 and options.choose <= 7:
            print(colored("Message : Sorry This Feature Is Coming Soon", "white", "on_cyan", attrs=["bold"]))

if __name__ == '__main__': 
    Main() 