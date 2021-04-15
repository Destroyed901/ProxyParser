import requests
from colorama import init, Fore, Back, Style

import pyfiglet

ascii_banner = pyfiglet.figlet_format("ProxyParser by Dififu")
print(Fore.LIGHTGREEN_EX + ascii_banner + Fore.RESET)

init(convert=True)
print("ProxyParser by" + Fore.LIGHTGREEN_EX + " dififu")

a = int(input(Fore.RED + " 1 - http\n 2 - Socks4\n 3 - Socks5\n Введи тип прокси:"))

if a == 1:
	http = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=5000&country=All&anonymity=All&ssl=yes')
	proxy = http.text.split()
	with open('http_proxy.txt', 'w') as http_proxy:
		for i in range(len(proxy)):
			http_proxy.write(proxy[i] + '\n')
	print(Fore.CYAN + 'Готово,прокси сохрaнены в файл')

elif a == 2:
	http = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=5000&country=All&anonymity=All&ssl=yes')
	proxy = http.text.split()
	with open('socks4_proxy.txt', 'w') as socks4_proxy:
		for i in range(len(proxy)):
			socks4_proxy.write(proxy[i] + '\n')
	print(Fore.CYAN + 'Готово,прокси сохрaнены в файл')

elif a == 3:
	http = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=5000&country=All&anonymity=All&ssl=yes')
	proxy = http.text.split()
	with open('socks5_proxy.txt', 'w') as socks5_proxy:
		for i in range(len(proxy)):
			socks5_proxy.write(proxy[i] + '\n')
	print(Fore.CYAN + 'Готово,прокси сохрaнены в файл')

else:
	print(Fore.RED + 'Ты что написал?')
