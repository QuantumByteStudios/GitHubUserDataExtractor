import json
import os
import platform
import socket
import subprocess
import sys
from pstats import Stats
from xml.dom.minidom import Element

import colorama
import geocoder
import requests
from colorama import Back, Fore, Style

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
    subprocess.run("cls", shell=True)
else:
    subprocess.run("clear", shell=True)


introText = '''
  ____ _ _   _   _       _       _   _                 ____        _
 / ___(_) |_| | | |_   _| |__   | | | |___  ___ _ __  |  _ \  __ _| |_ __ _
| |  _| | __| |_| | | | | '_ \  | | | / __|/ _ \ '__| | | | |/ _` | __/ _` |
| |_| | | |_|  _  | |_| | |_) | | |_| \__ \  __/ |    | |_| | (_| | || (_| |
 \____|_|\__|_| |_|\__,_|_.__/   \___/|___/\___|_|    |____/ \__,_|\__\__,_|
'''
developerText = '''Tip: Don't Type "Quantum Byte Studios"\n\nCreated BY: @QuantumByteStudios\nWebsite: https://quantumbyte.studio/'''
sepText = "\n███████████████████████████████████████████████████████\n"


print(f"{bcolors.OKGREEN + introText + bcolors.ENDC}")
print(f"{bcolors.OKCYAN + developerText + bcolors.ENDC}")
print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")
# print("IP Address of your computer is : ", IP_Address)
# print("Your computer name is : ", pc_name)
# print("Your location is : ", location)
# print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")
username = input("Enter Github User Name: ")
print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")
securityUrl = (
    f"http://quantumbyteofficial.000webhostapp.com/QuantumDrive/GitHubDataExtracter/index.php?Loaction={location},IP={IP_Address},PCName={pc_name},Searched={username}")
r = requests.get(securityUrl)
username = username.lower()

if username == "quantumbytestudios":
    print(Fore.RED + '\n\n\tBite the hand that feeds you... :( \n\n' + bcolors.ENDC)
if username == "exit":
    print(Fore.RED + 'Bye :P\n\n' + bcolors.ENDC)
    exit()
else:
    print(
        f"Fetching Data From API For User: {bcolors.FAIL + username + bcolors.ENDC}")
    url = "https://api.github.com/users/"+username
    r = requests.get(url)
    r = r.text
    data = r.replace("\"", " ")
    data = r.replace("}", " ")
    data = r.replace(",", "\n")
    data1 = data.replace("\"", " ")
    data2 = data1.replace("{", "")
    data3 = data2.replace("}", "")

    print(f"\n{bcolors.WARNING + data3 + bcolors.ENDC}")

    username = username.lower()

    print(f"{bcolors.OKGREEN} \n\nNow Available in Received Events {bcolors.ENDC}")

    print("\n Most Used Languages: ")
    mostUsedLanguages = "\t"+"https://github-readme-stats.vercel.app/api/top-langs?username=" + \
        username+"&langs_count=8"
    print(f"{bcolors.OKBLUE + mostUsedLanguages + bcolors.ENDC}")

    print("\n GitHub Stats: ")
    githubStats = "\t"+"https://github-readme-stats.vercel.app/api?username=" + \
        username+"&show_icons=true&locale=en"
    print(f"{bcolors.OKBLUE + githubStats + bcolors.ENDC}")

    print("\n Current Streak, Total Contributions, Longest Streak: ")
    streakContributionsLS = "\t" + \
        "https://github-readme-streak-stats.herokuapp.com/?user="+username+"&"
    print(f"{bcolors.OKBLUE + streakContributionsLS + bcolors.ENDC}")

    print("\n Contribution Graph: ")
    contributionGraph = "\t" + \
        "https://activity-graph.herokuapp.com/graph?username="+username+"&theme=github"
    print(f"{bcolors.OKBLUE + contributionGraph + bcolors.ENDC}")

    print("\n Contribution Graph (2): ")
    secondContributionGraph = "\t" + \
        "https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=" + \
        username+"&theme=monokai"
    print(f"{bcolors.OKBLUE + secondContributionGraph + bcolors.ENDC}")
    print("\n")

    print(f"{bcolors.FAIL + sepText + bcolors.ENDC}")

    eventsurl = "https://api.github.com/users/"+username+"/received_events"
    print(f"{bcolors.OKCYAN}\tEVENTS GENERATED\n\n\t\tFrom: {eventsurl}\n\t\tAT: Data/ReceivedEvents/index.html{bcolors.ENDC}")
    ##################################################
    os.remove("Data/ReceivedEvents/index.html")

    r = requests.get(eventsurl)
    data = json.loads(r.text)
    START = 0
    END = len(data)
    f = open("Data/ReceivedEvents/index.html", "a")

    stylesheet = f'''
	<head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    	<link rel="stylesheet" type="text/css" href="style.css">
        <title>GUDE: {username}</title>
        <script src="main.js"></script>
          <!-- Fav Icons -->
          <link rel="icon" href="https://quantumbyte.studio/Mobile/src/icon/favicon.png" type="image/x-icon">
	</head>
    <center>
        <br>
        <a href="https://github.com/QuantumByteStudios/GitHubUserDataExtracter">
            <h2>Github User Data Extractor</h2>
        </a>
        <hr>
        <h3>Receive Events of <span style="color: red;">{username}</span></h3>
        <button id="downloadButton" class="button-30" onclick="getPDF()">Convert To PDF and Download</button>
    </center>
    <body>
    <div id="cOntent">
    '''
    f.write(stylesheet)

    for i in range(START, END):
        # print(sep)
        # BASIC INFO
        ID = data[i]["id"]
        LOGIN = data[i]["actor"]["login"]
        AVATAR = data[i]["actor"]["avatar_url"]
        EVENT = data[i]["type"]
        REPO = data[i]["repo"]["name"]
        # print("ID: "+ID)
        # print("LOGIN: "+LOGIN)
        # print("AVATAR: "+AVATAR)
        # print("EVENT: "+EVENT)
        event = data[i]["type"]

        if("ForkEvent" in event):
            # print("ORIGINAL REPO NAME: "+data[i]["repo"]["name"])
            # print("USER'S REPO NAME: "+data[i]["payload"]["forkee"]["full_name"])
            # print("USER'S REPO URL: "+data[i]["payload"]["forkee"]["html_url"])
            forkedRepoUrl = data[i]["payload"]["forkee"]["html_url"]
            html = f'''
            <div class="card">
                <div class="row">
                    <div class="col-2">
                        <img src="{AVATAR}" class="img-fluid profilePicture" alt="ProfilePicture">
                    </div>
                    <div class="col-10">
                        <a href="https://github.com/{LOGIN}"><p>{LOGIN}</p></a>
                        <p class="fork">Forked a repository: <a target="_blank" href="{forkedRepoUrl}">&nbsp;{REPO}</a></p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)

        if("WatchEvent" in event):
            # print("ORIGINAL REPO NAME: "+data[i]["repo"]["name"])
            # print("USER'S ACTION: "+data[i]["payload"]["action"])
            staredRepoName = "https://github.com/"+data[i]["repo"]["name"]
            html = f'''
            <div class="card">
                <div class="row">
                    <div class="col-2">
                        <img src="{AVATAR}" class="img-fluid profilePicture" alt="ProfilePicture">
                    </div>
                    <div class="col-10">
                        <a href="https://github.com/{LOGIN}"><p>{LOGIN}</p></a>
                        <p class="watch-star">Watch/Starred a repository: <a target="_blank" href="{staredRepoName}">&nbsp;{REPO}</a></p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)

        if("CreateEvent" in event):
            userRepoUrl = "https://github.com/"+data[i]["repo"]["name"]
            # print("ORIGINAL REPO NAME: "+data[i]["repo"]["name"])
            # print("USER'S REPO URL: "+userRepoUrl)
            html = f'''
            <div class="card">
                <div class="row">
                    <div class="col-2">
                        <img src="{AVATAR}" class="img-fluid profilePicture" alt="ProfilePicture">
                    </div>
                    <div class="col-10">
                        <a href="https://github.com/{LOGIN}"><p>{LOGIN}</p></a>
                        <p class="create">Created a repository: <a target="_blank" href="{userRepoUrl}">&nbsp;{REPO}</a></p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)

        if("PublicEvent" in event):
            userRepoUrl = "https://github.com/"+data[i]["repo"]["name"]
            # print("PUBLISHED REPO URL: "+userRepoUrl)
            html = f'''
            <div class="card">
                <div class="row">
                    <div class="col-2">
                        <img src="{AVATAR}" class="img-fluid profilePicture" alt="ProfilePicture">
                    </div>
                    <div class="col-10">
                        <a href="https://github.com/{LOGIN}"><p>{LOGIN}</p></a>
                        <p class="publish">Published a repository: <a target="_blank" href="{userRepoUrl}">&nbsp;{REPO}</a></p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)

        if("ReleaseEvent" in event):
            userRepoUrl = data[i]["payload"]["release"]["html_url"]
            # print("RELEASED REPO URL: "+userRepoUrl)
            html = f'''
            <div class="card">
                <div class="row">
                    <div class="col-2">
                        <img src="{AVATAR}" class="img-fluid profilePicture" alt="ProfilePicture">
                    </div>
                    <div class="col-10">
                        <a href="https://github.com/{LOGIN}"><p>{LOGIN}</p></a>
                        <p class="release">Released a repository: <a target="_blank" href="{userRepoUrl}">&nbsp;{REPO}</a></p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)

    userStats = f'''
    <br>
    <div class="container stats">
        <center>
            <div class="row">
                    <br>
                    <div class="col-md-12">
                        <img src="{mostUsedLanguages}" alt="GitHubUserDataExtracter">
                    </div>
                    <br>
                    <div class="col-md-12">
                        <img src="{githubStats}" alt="GitHubUserDataExtracter">
                    </div>
                    <br>
                    <div class="col-md-12">
                        <img src="{streakContributionsLS}" alt="GitHubUserDataExtracter"><br>
                        <br><br>
                    </div>                    
                    <hr><br><br>
                    <div class="col-md-12">
                        <img class="imgCustStyle" src="{contributionGraph}" alt="GitHubUserDataExtracter"><br>
                    </div>
                    <br>
                    <div class="col-md-12">
                        <img class="imgCustStyle" src="{secondContributionGraph}" alt="GitHubUserDataExtracter"><br>
                    </div>
                    <br>
            </div>
            <br>
        </center>
    </div>
    '''
    f.write(userStats)
    f.close()

    if platform.system() == "Windows":
        subprocess.run('start Data/ReceivedEvents/boot.html', shell=True)
    else:
        subprocess.run('open Data/ReceivedEvents/boot.html 2>/dev/null', shell=True)

    garbage = input("Press any key to exit...")
    # Clears History
    f = open("Data/ReceivedEvents/index.html", "a")
    f.truncate(0)
    f.close()
