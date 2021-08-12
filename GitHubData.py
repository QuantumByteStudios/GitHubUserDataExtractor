import requests
import os
os.system("cls")
print('''

  ____ _ _   _   _       _       _   _                 ____        _
 / ___(_) |_| | | |_   _| |__   | | | |___  ___ _ __  |  _ \  __ _| |_ __ _
| |  _| | __| |_| | | | | '_ \  | | | / __|/ _ \ '__| | | | |/ _` | __/ _` |
| |_| | | |_|  _  | |_| | |_) | | |_| \__ \  __/ |    | |_| | (_| | || (_| |
 \____|_|\__|_| |_|\__,_|_.__/   \___/|___/\___|_|    |____/ \__,_|\__\__,_|

Tip: Don't Type "Quantum Byte Sudios" 

Created BY: @QuantumByteStudios
Website: https://quantumbyteofficial.tech/

	''')
username = input("Enter Github User Name: ")
if username == "QuantumByteStudios":
	print("\n\nBite the hand that feeds you... :( \n\n")

else:

	url = "https://api.github.com/users/"+username
	print("\n**************************************\n")
	r = requests.get(url)
	r = r.text 
	data = r.replace("\"", " ")
	data = r.replace("}", " ")
	data = r.replace(",", "\n")
	data1 = data.replace("\"", " ")
	data2 = data1.replace("{", "")
	data3 = data2.replace("}", "")
	print(data3)
	username = username.lower()
	print("\n Most Used Languages: ")
	url = "\t"+"https://github-readme-stats.vercel.app/api/top-langs?username="+username+"&show_icons=true&locale=en&layout=compact"
	print(url)
	print("\n GitHub Stats: ")
	url = "\t"+"https://github-readme-stats.vercel.app/api?username="+username+"&show_icons=true&locale=en"
	print(url)
	print("\n Current Streak, Total Contributions, Longest Streak: ")
	url = "\t"+"https://github-readme-streak-stats.herokuapp.com/?user="+username+"&"
	print(url)
	print("\n\n")
	garbage = input("Press any key to exit...")