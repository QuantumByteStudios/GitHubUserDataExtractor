import requests
import os
import platform
import colorama
from colorama import Fore, Back, Style
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'

if platform.system() == "Windows":
	os.system("cls")
else:
	os.system("clear")


introText = '''
  ____ _ _   _   _       _       _   _                 ____        _
 / ___(_) |_| | | |_   _| |__   | | | |___  ___ _ __  |  _ \  __ _| |_ __ _
| |  _| | __| |_| | | | | '_ \  | | | / __|/ _ \ '__| | | | |/ _` | __/ _` |
| |_| | | |_|  _  | |_| | |_) | | |_| \__ \  __/ |    | |_| | (_| | || (_| |
 \____|_|\__|_| |_|\__,_|_.__/   \___/|___/\___|_|    |____/ \__,_|\__\__,_|

	'''
developerText = '''
Tip: Don't Type "Quantum Byte Sudios"\n\nCreated BY: @QuantumByteStudios\nWebsite: https://quantumbyteofficial.tech/
'''
sepText = "\n**************************************\n"


print(f"{bcolors.OKGREEN + introText + bcolors.ENDC}")
print(f"{bcolors.OKCYAN + developerText + bcolors.ENDC}")
print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")
username = input("Enter Github User Name: ")
print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")
if username == "QuantumByteStudios":
	print(Fore.RED + '\n\nBite the hand that feeds you... :( \n\n')

else:
	url = "https://api.github.com/users/"+username
	r = requests.get(url)
	r = r.text 
	data = r.replace("\"", " ")
	data = r.replace("}", " ")
	data = r.replace(",", "\n")
	data1 = data.replace("\"", " ")
	data2 = data1.replace("{", "")
	data3 = data2.replace("}", "")

	print(f"{bcolors.WARNING + data3 + bcolors.ENDC}")

	username = username.lower()
	print("\n Most Used Languages: ")
	url = "\t"+"https://github-readme-stats.vercel.app/api/top-langs?username="+username+"&show_icons=true&locale=en&layout=compact"
	print(f"{bcolors.OKBLUE + url + bcolors.ENDC}")
	print("\n GitHub Stats: ")
	url = "\t"+"https://github-readme-stats.vercel.app/api?username="+username+"&show_icons=true&locale=en"
	print(f"{bcolors.OKBLUE + url + bcolors.ENDC}")
	print("\n Current Streak, Total Contributions, Longest Streak: ")
	url = "\t"+"https://github-readme-streak-stats.herokuapp.com/?user="+username+"&"
	print(f"{bcolors.OKBLUE + url + bcolors.ENDC}")
	print("\n")
	garbage = input("Press any key to exit...")