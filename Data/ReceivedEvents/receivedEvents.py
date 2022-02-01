# IGNORE THIS FILE !!!

import json
import requests

url = "https://api.github.com/users/quantumbytestudios/received_events"
r = requests.get(url)
data = json.loads(r.text)
username = "boi"
START = 0
END = len(data)
f = open("index.html", "a")

stylesheet = '''
	<head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    	<link rel="stylesheet" type="text/css" href="style.css">
	</head>
'''
f.write(stylesheet)

for i in range(START, END):
    # print(sep)
    # BASIC INFO
    ID = data[i]["id"]
    LOGIN = data[i]["actor"]["login"]
    AVATAR = data[i]["actor"]["avatar_url"]
    EVENT = data[i]["type"]
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
                    <p class="fork">Forked: <a target="_blank" href="{forkedRepoUrl}">Visit Repository</a></p>
                </div>
            </div>
        </div>
        '''
        f.write(html)

    if("WatchEvent" in event):
        # print("ORIGINAL REPO NAME: "+data[i]["repo"]["name"])
        # print("USER'S ACTION: "+data[i]["payload"]["action"])
        repoName = data[i]["repo"]["name"]
        html = f'''
        <div class="card">
            <div class="row">
                <div class="col-2">
                    <img src="{AVATAR}" class="img-fluid profilePicture" alt="ProfilePicture">
                </div>
                <div class="col-10">
                    <a href="https://github.com/{LOGIN}"><p>{LOGIN}</p></a>
                    <p class="watch-star">Watch/Starred: <a target="_blank" href="{repoName}">Visit Repository</a></p>
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
                    <p class="create">Created: <a target="_blank" href="{userRepoUrl}">Visit Repository</a></p>
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
                    <p class="publish">Published: <a target="_blank" href="{userRepoUrl}">Visit Repository</a></p>
                </div>
            </div>
        </div>
        '''
        f.write(html)

    if("ReleaseEvent" in event):
        userRepoUrl = "https://github.com/"+data[i]["payload"]["release"]["html_url"]
        # print("RELEASED REPO URL: "+userRepoUrl)
        html = f'''
        <div class="card">
            <div class="row">
                <div class="col-2">
                    <img src="{AVATAR}" class="img-fluid profilePicture" alt="ProfilePicture">
                </div>
                <div class="col-10">
                    <a href="https://github.com/{LOGIN}"><p>{LOGIN}</p></a>
                    <p class="release">Released: <a target="_blank" href="{userRepoUrl}">Visit Repository</a></p>
                </div>
            </div>
        </div>
        '''
        f.write(html)



f.close()
# # trash = input("Ho Gaya Bhai..!")