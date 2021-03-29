import socket
from sys import exit
import colorama
from colorama import Back, Fore, Style, deinit, init
init()

print(Fore.MAGENTA)
ip = input("\nTarget IP : ")
print(Fore.WHITE + "\n-------")
print(Fore.MAGENTA)
ports = input("Enter ports to scan : ")
print(Fore.WHITE + "\n-------")
ports = ports.replace(' ', '')

for port in ports.split(','):
	try:
		port = int(port)
	except:
		print(Fore.YELLOW)
		print("[*]Incorrect.")
		exit(1)

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	code = sock.connect_ex((ip, port))

	if code==0 :
		print(Fore.GREEN)
		print("[*]Port {} is open !".format(str(port)))
	else:
		print(Fore.RED)
		print("[*]Port {} is closed !".format(str(port)))

	sock.close()
	

