import json
import os
import platform
import requests
import subprocess
import tkinter as tk
from tkinter import ttk
from colorama import Fore
from tkinter import messagebox
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

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

# HTML Viewer
class HTMLViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GitHubUserDataExtractor - HTML Viewer")

        # Local path to HTML file
        self.html_path = os.path.abspath("Data/ReceivedEvents/index.html")

        # WebEngineView to display HTML content
        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl.fromLocalFile(self.html_path))

        layout = QVBoxLayout()
        layout.addWidget(self.webview)

        # Main widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set screen dimensions and center the window
        self.setFixedSize(900, 800)
        self.center_on_screen()

    def center_on_screen(self):
        frame_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

# Clear Screen
def clear():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)  # nosec B602, B607
    else:
        subprocess.run("clear", shell=True)  # nosec B602, B607

# Open Result
def openResult():
    app = QApplication([])
    browser = HTMLViewer()
    browser.show()
    app.exec_()
    # Old Logic
    # if platform.system() == "Windows":
    #     subprocess.run('start Data/ReceivedEvents/boot.html', shell=True)  # nosec B602, B607
    # else:
    #     subprocess.run('open Data/ReceivedEvents/boot.html 2>/dev/null', shell=True)  # nosec B602, B607


# Fetch and Print Data form API
def fetchAndPrintData(username):
    print(f"Fetching Data From API For User: {colors.FAIL + username + colors.ENDC}")
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
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
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
        <!-- <button id="downloadButton" class="button-30" onclick="getPDF()">Convert To PDF and Download</button> -->
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
        if ("ForkEvent" in event):
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
        if ("WatchEvent" in event):
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
                        <p class="watch-star">Watch/Starred a repository: <a target="_blank" href="{staredRepoName}">&nbsp{REPO}</a></p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)
        if ("CreateEvent" in event):
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
        if ("PublicEvent" in event):
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
                        <p class="publish">Published a repository: <a target="_blank" href="{userRepoUrl}">&nbsp;{REPO}</a><p>
                    </div>
                </div>
            </div>
            '''
            f.write(html)
        if ("ReleaseEvent" in event):
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
                    <img src="{urls["mostUsedLanguages"]}" alt="GitHubUserDataExtractor">
                </div>
                <br>
                <div class="col-md-12">
                    <img src="{urls["githubStats"]}" alt="GitHubUserDataExtractor">
                </div>
                <br>
                <div class="col-md-12">
                    <img src="{urls["streakContributionsLS"]}" alt="GitHubUserDataExtractor"><br>
                    <br><br>
                </div>                    
                <hr><br><br>
                <div class="col-md-12">
                    <img class="imgCustStyle" src="{urls["contributorGraphOne"]}" alt="GitHubUserDataExtractor"><br>
                </div>
                <br>
                <div class="col-md-12">
                    <img class="imgCustStyle" src="{urls["contributorGraphTwo"]}" alt="GitHubUserDataExtractor"><br>
                </div>
                <br>
            </div>
            <br>
        </center>
    </div>
    '''
    # f.write(userStats)
    f.close()