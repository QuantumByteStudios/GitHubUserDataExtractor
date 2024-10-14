import os
import platform
import utils as session
from utils import colors

# Clear Screen
session.clear()

# Display label and developer info
label = '''
  ____ _ _   _   _       _       _   _                 ____        _
 / ___(_) |_| | | |_   _| |__   | | | |___  ___ _ __  |  _ \  __ _| |_ __ _
| |  _| | __| |_| | | | | '_ \  | | | / __|/ _ \ '__| | | | |/ _` | __/ _` |
| |_| | | |_|  _  | |_| | |_) | | |_| \__ \  __/ |    | |_| | (_| | || (_| |
 \____|_|\__|_| |_|\__,_|_.__/   \___/|___/\___|_|    |____/ \__,_|\__\__,_|
'''
dev_information = (
    f"Developer: {colors.CYAN}QuantumByteStudios{colors.ENDC}\n"
    f"Website: {colors.CYAN}https://quantumbytestudios.in{colors.ENDC}"
)

print(f"{colors.GREEN + label + colors.ENDC}")
print(dev_information)
print("\n")

# Get GitHub Username
username = input(f"Enter a Github Username: {colors.WARNING}").strip().lower()
print(f"{colors.ENDC}")

# Validate if the input is empty
if not username:
    print(f"{colors.RED}Username cannot be empty!{colors.ENDC}")
    exit()

# URL for GitHub data
urls = {
    "mostUsedLanguages": f"\thttps://github-readme-stats.vercel.app/api/top-langs?username={username}&langs_count=8",
    "githubStats": f"\thttps://github-readme-stats.vercel.app/api?username={username}&show_icons=true&locale=en",
    "streakContributionsLS": f"\thttps://streak-stats.demolab.com/?user={username}&",
    "contributorGraphOne": f"\thttps://github-readme-activity-graph.vercel.app/graph?username={username}&bg_color=000000&color=ffffff&line=ffffff&point=ffffff&area=true&hide_border=true",
    "contributorGraphTwo": f"\thttps://github-profile-summary-cards.vercel.app/api/cards/profile-details?username={username}&theme=dark"
}


def get_user_data(username):
    # Handle exit command
    if username == "exit":
        print(colors.RED + 'Bye :P\n\n' + colors.ENDC)
        exit()

    # Fetch and print GitHub data
    session.fetch_and_print_data(username)

    # Show events and graphs
    session.show_events_and_graphs(urls)

    # Create HTML file for user's received events
    session.create_and_display_html_user_events(username, urls)

    # Open generated HTML file based on the operating system
    if platform.system() == "Linux":
        import HTMLViewer_Linux
        HTMLViewer_Linux.showHTMLLinux()
    else:
        import HTMLViewer_Windows
        HTMLViewer_Windows.showHTMLWindow()

    # Wait for user input to exit
    input("Press any key to exit...")

    # Clear the HTML file content after viewing
    html_file_path = os.path.join("Data", "ReceivedEvents", "index.html")
    try:
        with open(html_file_path, "w", encoding="utf_8") as f:
            f.truncate(0)
    except FileNotFoundError:
        print(
            f"{colors.WARNING}Warning: HTML file '{html_file_path}' not found to truncate.{colors.ENDC}")

    print("Closing...")
    exit()


# Execute the function to get user data
get_user_data(username)
