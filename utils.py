import json
import os
import platform
import requests
import subprocess
import tkinter as tk
from tkinter import ttk
from colorama import Fore
from tkinter import messagebox


# Colors
class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


# Clear Screen
def clear():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)  # nosec B602, B607
    else:
        subprocess.run("clear", shell=True)  # nosec B602, B607


# Fetch and Print Data form API
def fetchAndPrintData(username):
    print(f"Fetching data from API for user: {colors.FAIL + username + colors.ENDC}")
    url = "https://api.github.com/users/"+username
    r = requests.get(url).text
    data = r.replace("\"", " ").replace("}", " ").replace(",", "\n").replace("\"", " ").replace("{", "").replace("}", "")
    print(f"\n{colors.WARNING + data + colors.ENDC}")


# Show Events and Graphs
def showEventsAndGraphs(urls):
    # Start
    print(f"\n\nGraphs are now available in Received Events [ {colors.GREEN}✓{colors.ENDC} ]")

    # Most Used Languages
    # print("\n Most Used Languages: ")
    # print(f"{colors.BLUE + urls['mostUsedLanguages'] + colors.ENDC}")

    # GitHub Stats
    # print("\n GitHub Stats: ")
    # print(f"{colors.BLUE + urls['githubStats'] + colors.ENDC}")

    # Current Streak, Total Contributions, Longest Streak
    # print("\n Current Streak, Total Contributions, Longest Streak: ")
    # print(f"{colors.BLUE + urls['streakContributionsLS'] + colors.ENDC}")

    # Contribution Graphs One & Two
    # print("\n Contribution Graph: (One)")
    # print(f"{colors.BLUE + urls['contributorGraphOne'] + colors.ENDC}")
    # print("\n Contribution Graph: (Two)")
    # print(f"{colors.BLUE + urls['contributorGraphTwo'] + colors.ENDC}")
    
    # End
    # print("\n\n")


# HTML Received Events File
def createAndDisplayHTMLUserEvents(username, urls):
    eventsurl = "https://api.github.com/users/"+username+"/received_events"
    # print(f"{colors.CYAN}\tEVENTS GENERATED\n\n\t\tFrom: {eventsurl}\n\t\tAT: Data/ReceivedEvents/index.html{colors.ENDC}")
    print(f"HTML received events generated successfully [ {colors.GREEN}✓{colors.ENDC} ]\n\n")
        
    # Delete Old File
    if os.path.exists("Data/ReceivedEvents/index.html"):
        os.remove("Data/ReceivedEvents/index.html")
    r = requests.get(eventsurl).text
    data = json.loads(r)
    START = 0
    END = len(data)
    f = open("Data/ReceivedEvents/index.html", "a", encoding="utf_8")
    stylesheet = f'''
    <head>
        <title>GitHubUserDataExtractor - Output</title>
        <link rel="icon" href="https://quantumbytestudios.in/src/images/ClassicWhiteVeryBig.png" type="image/x-icon">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="style.css">
        <script src="main.js"></script>
    </head>
    <br>
    <div class="d-flex align-items-center m-2">
        <a class="badge program-title" href="https://github.com/QuantumByteStudios/GitHubUserDataExtracter">
            <h2 class="m-0 p-2">GithubUserDataExtractor</h2>
        </a>
        <h5 class="m-0 p-2">Target <span class="badge bg-danger">{username}</span></h5>
    </div>
    <hr>

    <body class="container-lg p-lg-5">
    <div class="w-100">
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
        if ("ForkEvent" in event):
            # print("ORIGINAL REPO NAME: "+data[i]["repo"]["name"])
            # print("USER'S REPO NAME: "+data[i]["payload"]["forkee"]["full_name"])
            # print("USER'S REPO URL: "+data[i]["payload"]["forkee"]["html_url"])
            forkedRepoUrl = data[i]["payload"]["forkee"]["html_url"]
            html = f'''
            <div class="row m-3 p-0 bg-normal">
                <div class="col-12 d-flex justify-content-left align-items-center">
                    <img src="{AVATAR}" class="img-fluid profile-picture">
                    <a href="https://github.com/{LOGIN}">
                        <p class="badge bg-primary">{LOGIN}</p>
                    </a>
                    <div class="badge bg-danger text-white bg-content">
                        <p>
                            Forked a repository
                            <a class="repo-link" target="_blank" href="{forkedRepoUrl}">
                                {REPO}
                            </a>
                        </p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)
        if ("WatchEvent" in event):
            # print("ORIGINAL REPO NAME: "+data[i]["repo"]["name"])
            # print("USER'S ACTION: "+data[i]["payload"]["action"])
            staredRepoURL = "https://github.com/"+data[i]["repo"]["name"]
            html = f'''
            <div class="row m-3 p-0 bg-normal">
                <div class="col-12 d-flex justify-content-left align-items-center">
                    <img src="{AVATAR}" class="img-fluid profile-picture">
                    <a href="https://github.com/{LOGIN}">
                        <p class="badge bg-primary">{LOGIN}</p>
                    </a>
                    <div class="badge bg-warning text-dark bg-content">
                        <p>
                            Watch/Starred a repository
                            <a class="repo-link" target="_blank" href="{staredRepoURL}">
                               {REPO}
                            </a>
                        </p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)
        if ("CreateEvent" in event):
            userRepoURL = "https://github.com/"+data[i]["repo"]["name"]
            # print("ORIGINAL REPO NAME: "+data[i]["repo"]["name"])
            # print("USER'S REPO URL: "+userRepoUrl)
            html = f'''
            <div class="row m-3 p-0 bg-normal">
                <div class="col-12 d-flex justify-content-left align-items-center">
                    <img src="{AVATAR}" class="img-fluid profile-picture">
                    <a href="https://github.com/{LOGIN}">
                        <p class="badge bg-primary">{LOGIN}</p>
                    </a>
                    <div class="badge bg-success text-white bg-content">
                        <p>
                            Created a repository
                            <a class="repo-link" target="_blank" href="{userRepoURL}">
                                {REPO}
                            </a>
                        </p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)
        if ("PublicEvent" in event):
            userRepoUrl = "https://github.com/"+data[i]["repo"]["name"]
            # print("PUBLISHED REPO URL: "+userRepoUrl)
            html = f'''
            <div class="row m-3 p-0 bg-normal">
                <div class="col-12 d-flex justify-content-left align-items-center">
                    <img src="{AVATAR}" class="img-fluid profile-picture">
                    <a href="https://github.com/{LOGIN}">
                        <p class="badge bg-primary">{LOGIN}</p>
                    </a>
                    <div class="badge bg-primary text-white bg-content">
                        <p>
                            Published a repository
                            <a class="repo-link" target="_blank" href="{userRepoUrl}">
                                {REPO}
                            </a>
                        </p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)
        if ("ReleaseEvent" in event):
            userRepoUrl = data[i]["payload"]["release"]["html_url"]
            # print("RELEASED REPO URL: "+userRepoUrl)
            html = f'''
            <div class="row m-3 p-0 bg-normal">
                <div class="col-12 d-flex justify-content-left align-items-center">
                    <img src="{AVATAR}" class="img-fluid profile-picture">
                    <a href="https://github.com/{LOGIN}">
                        <p class="badge bg-primary">{LOGIN}</p>
                    </a>
                    <div class="badge bg-primary text-white bg-content">
                        <p>
                            Released a repository
                            <a class="repo-link" target="_blank" href="{userRepoUrl}">
                                {REPO}
                            </a>
                        </p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)

    userStats = f'''
        <br>
        <div class="container">
            <div class="row d-flex justify-content-center align-items-center">
                <div class="col-12 col-md-6 d-flex justify-content-center">
                    <img class="img-fluid" src="{urls["mostUsedLanguages"]}">
                </div>
                <div class="col-12 col-md-6">
                    <center>
                        <img class="img-fluid w-100" src="{urls["githubStats"]}">
                        <img class="img-fluid w-100" src="{urls["streakContributionsLS"]}">
                    </center>
                </div>
            </div>
            <div class="row d-flex justify-content-center align-items-center">
                <div class="col-12 d-flex justify-content-center">
                    <img class="img-fluid" src="{urls["contributorGraphOne"]}">
                </div>
                <div class="col-12 d-flex justify-content-center">
                    <img class="img-fluid" src="{urls["contributorGraphTwo"]}">
                </div>
            </div>
        </div>
    </body>
    '''
    f.write(userStats)
    f.close()