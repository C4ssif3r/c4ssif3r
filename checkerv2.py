from sys import argv
import urllib3
from os import system as terminal
import requests
from colorama import Fore, Style
import threading
from random import choice as select


w = Fore.WHITE
r = Fore.RED
g = Fore.GREEN


URL = ["https://google.com","https://github.com","https://stackoverflow.com"]

CMD_CLEAR_TERM = "clear"

TIMEOUT = (3.05,10) # or set 27 for default ! dont change it


#try:
#    MAX_THREADS = int(input("Max Threads [Default->50] ?:"))
#except:
#    MAX_THREADS = 50



#if MAX_THREADS > 500:
#    MAX_THREADS = 500

#else:
#    pass
MAX_THREADS = 70 #can set to 2000 or more 
#good_file_name = input(" Enter The Good File Name For Save Good Proxies :")

trd = str(MAX_THREADS)

print (f"THREADS -> {r}{trd}{w}")

class ProxyChecker:
    def __init__(self):
        self.goods = 0
        self.proxies = []
        self.file_with_goods = open('good_proxies.txt', 'a')

    def check_proxy(self, proxy):
        try:
            session = requests.Session()
            session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131'
            session.max_redirects = 30
            proxy = proxy.split('\n',1)[0]
            print(Fore.LIGHTYELLOW_EX + 'Checking ' + proxy)
            session.get(select(URL), proxies={'http':'http://' + proxy}, timeout=TIMEOUT, allow_redirects=True)
        except:
            pass
        else:
            self.file_with_goods.write(proxy + "\n")
#            self.file_with_goods.write("\n")
            self.goods += 1
            print(Fore.LIGHTGREEN_EX + 'Good proxy ' + proxy + " "+ str(self.goods))

    def check_proxies(self, proxies):
        threads = []
        for proxy in proxies:
            t = threading.Thread(target=self.check_proxy, args=(proxy,))
            threads.append(t)
            t.start()
            if len(threads) >= MAX_THREADS:
                for thread in threads:
                    thread.join()
                threads = []
        # Join remaining threads
        for thread in threads:
            thread.join()

        self.file_with_goods.close()
        print(Fore.LIGHTGREEN_EX + 'Total ' + str(self.goods) + ' good proxies found')
        print(Fore.LIGHTRED_EX + 'And ' + str(len(proxies) - self.goods) + ' is bad')
        print(Fore.LIGHTYELLOW_EX + 'Have a nice day! :)')


def print_help():
    terminal(CMD_CLEAR_TERM)
    print(Fore.LIGHTGREEN_EX + 'PROXY CHCKER ZER0 M.J.I')


if len(argv) > 1:
    commands = ['--help','-h','-f','/?','--file','-file','--proxy']
    if argv[1] in commands:
        if argv[1] in ('--help','-help','/?','--?'):
            print_help()
        elif argv[1] in ('-f','--file','-file'):
            try:
                file = open(argv[2])
                proxies = list(file)
                checker = ProxyChecker()
                terminal(CMD_CLEAR_TERM)
                print(Fore.LIGHTCYAN_EX + '===========================================')
                checker.check_proxies(proxies)
            except FileNotFoundError:
                print(Fore.LIGHTRED_EX + 'Error!\nFile Not found!')
            except IndexError:
                print(Fore.LIGHTRED_EX + 'Error!\nMissing filename!')
        else:
            print(Fore.LIGHTRED_EX + 'Unknown option \"' + argv[1] + '\"')
    else:
        print_help()
else:
    print_help()
