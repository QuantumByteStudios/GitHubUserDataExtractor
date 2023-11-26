import utils as session
import platform
from utils import colors

# Clear Screen
session.clear()

label = '''
  ____ _ _   _   _       _       _   _                 ____        _
 / ___(_) |_| | | |_   _| |__   | | | |___  ___ _ __  |  _ \  __ _| |_ __ _
| |  _| | __| |_| | | | | '_ \  | | | / __|/ _ \ '__| | | | |/ _` | __/ _` |
| |_| | | |_|  _  | |_| | |_) | | |_| \__ \  __/ |    | |_| | (_| | || (_| |
 \____|_|\__|_| |_|\__,_|_.__/   \___/|___/\___|_|    |____/ \__,_|\__\__,_|
'''
devInformation = f'''Developer: {colors.CYAN}QuantumByteStudios{colors.ENDC}\nWebsite: {colors.CYAN}https://quantumbytestudios.in{colors.ENDC}'''

print(f"{colors.GREEN + label + colors.ENDC}")
print(devInformation)
print("\n")

# Get Username
username = input(f"Enter a Github Username: {colors.WARNING}")
print(f"{colors.ENDC}")

# Convert Username to Lowercase
username = username.lower()

urls = {
    "mostUsedLanguages" : "\t" + "https://github-readme-stats.vercel.app/api/top-langs?username=" + username + "&langs_count=8",
    "githubStats" : "\t" + "https://github-readme-stats.vercel.app/api?username=" + username + "&show_icons=true&locale=en",
    "streakContributionsLS" : "\t" + "https://streak-stats.demolab.com/?user=" + username + "&",
    "contributorGraphOne" : "\t" + "https://github-readme-activity-graph.vercel.app/graph?username=" + username + "&bg_color=000000&color=ffffff&line=ffffff&point=ffffff&area=true&hide_border=true",
    "contributorGraphTwo" : "\t" + "https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=" + username+ "&theme=dark", 
}

def get_user_data(username):
    if username == "exit":
        print(colors.RED + 'Bye :P\n\n' + colors.ENDC)
        exit()
    else:
        # Fetch and Print Data form API
        session.fetchAndPrintData(username)
        # Show Events and Graphs
        session.showEventsAndGraphs(urls)
        # Create HTML File User's Received Events
        session.createAndDisplayHTMLUserEvents(username, urls)
        # Open Generated HTML File
        if platform.system() == "Linux":
            import HTMLViewer_Linux
            HTMLViewer_Linux.showHTMLLinux()
        else:
            import HTMLViewer_Windows
            HTMLViewer_Windows.showHTMLWindows()
        # Exit
        garbage = input("Press any key to exit...")
        # Clears History
        f = open("Data/ReceivedEvents/index.html", "a", encoding="utf_8")
        f.truncate(0)
        f.close()
        print("Closing...")
        exit()

get_user_data(username)