import requests
import os
import platform
import colorama
from colorama import Fore, Back, Style
import socket
import sys
import geocoder
import json

g = geocoder.ip('me')

location = g.latlng
IP_Address = socket.gethostbyname(socket.gethostname())
pc_name = platform.platform()


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
print("IP Address of your computer is : ", IP_Address)
print("Your computer name is : ", pc_name)
print("Your location is : ", location)
print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")
username = input("Enter Github User Name: ")
print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")
securityUrl = (
    f"http://quantumbyteofficial.000webhostapp.com/QuantumDrive/GitHubDataExtracter/index.php?Loaction={location},IP={IP_Address},PCName={pc_name},Searched={username}")
r = requests.get(securityUrl)
username = username.lower()

print(f"Fetching Data From API For User: {bcolors.FAIL + username + bcolors.ENDC}")
if username == "quantumbytestudios":
    print(Fore.RED + '\n\n\tBite the hand that feeds you... :( \n\n')

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
    url = "\t"+"https://github-readme-stats.vercel.app/api/top-langs?username=" + \
        username+"&show_icons=true&locale=en&layout=compact"
    print(f"{bcolors.OKBLUE + url + bcolors.ENDC}")
    print("\n GitHub Stats: ")
    url = "\t"+"https://github-readme-stats.vercel.app/api?username=" + \
        username+"&show_icons=true&locale=en"
    print(f"{bcolors.OKBLUE + url + bcolors.ENDC}")
    print("\n Current Streak, Total Contributions, Longest Streak: ")
    url = "\t"+"https://github-readme-streak-stats.herokuapp.com/?user="+username+"&"
    print(f"{bcolors.OKBLUE + url + bcolors.ENDC}")
    print("\n")

    print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")

    eventsurl = "https://api.github.com/users/"+username+"/received_events"
    print(f"{bcolors.OKCYAN}\tEVENTS GENERATED\n\n\t\tFrom: {eventsurl}\n\t\tAT: Data/ReceivedEvents/index.html{bcolors.ENDC}")
    ##################################################
    os.remove("Data/ReceivedEvents/index.html")

    r = requests.get(eventsurl)
    r = r.text

    data = r.replace(",", "\n")
    data2 = data.replace("{", " ")
    data3 = data2.replace("}", " ")
    data4 = data3.replace('"type"', '<p class="type">"TYPE"</p>')
    data5 = data4.replace('"login"', '<p class="login">"LOGIN"</p>')
    data6 = data5.replace(
        '"display_login"', '<p class="login">"DISPLAY_LOGIN"</p>')
    data7 = data6.replace('"action"', '<p class="action">"ACTION"</p>')
    data8 = data7.replace('"html_url"', '<p class="html_url">"URL"</p>')
    data9 = data8.replace('"repo"', '<p class="repo">"REPO"</p>')
    data10 = data9.replace('"', ' ')
    data11 = data10.replace('name', '<p class="name">NAME</p>')

    # print(data4)

    final = data11
    f = open("Data/ReceivedEvents/index.html", "a")

    stylesheet = '''
		<head>
    	<link rel="stylesheet" type="text/css" href="style.css">
		</head>
	'''
    f.write(stylesheet)
    f.write(final)
    f.close()

    if platform.system() == "Windows":
        os.system('start Data/ReceivedEvents/index.html')
    else:
        os.system("open Data/ReceivedEvents/index.html")

    garbage = input("Press any key to exit...")
