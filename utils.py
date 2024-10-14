import json
import os
import platform
import requests
import subprocess
from colorama import Fore, Style
from requests.exceptions import HTTPError


class colors:
    HEADER = Fore.MAGENTA
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    WARNING = Fore.YELLOW
    FAIL = Fore.RED
    ENDC = Style.RESET_ALL
    BOLD = Style.BRIGHT


def clear():
    command = "cls" if platform.system() == "Windows" else "clear"
    os.system(command)


def fetch_and_print_data(username):
    """Fetches and prints user data from the GitHub API."""
    print(f"Fetching data for user: {colors.FAIL + username + colors.ENDC}")
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Pretty print selected fields instead of replacing characters
        formatted_data = json.dumps(data, indent=2)
        print(f"\n{colors.WARNING}{formatted_data}{colors.ENDC}")
    except HTTPError as http_err:
        print(f"{colors.FAIL}HTTP error occurred: {http_err}{colors.ENDC}")
    except Exception as err:
        print(f"{colors.FAIL}An error occurred: {err}{colors.ENDC}")


def show_events_and_graphs(urls):
    """Display user event statistics and graphs."""
    print(
        f"\nGraphs available in Received Events [{colors.GREEN}✓{colors.ENDC}]")
    # Here you could include logic to show or download these graphs.


def generate_html_event_row(avatar, login, event_type, repo_name, repo_url, badge_class, action_text):
    """Helper to generate a single event row for HTML output."""
    return f'''
    <div class="row m-3 p-0 bg-normal">
        <div class="col-12 d-flex justify-content-left align-items-center">
            <img src="{avatar}" class="img-fluid profile-picture">
            <a href="https://github.com/{login}">
                <p class="badge bg-primary">{login}</p>
            </a>
            <div class="badge {badge_class} text-white bg-content">
                <p>{action_text}
                    <a class="repo-link" target="_blank" href="{repo_url}">
                        {repo_name}
                    </a>
                </p>
            </div>
        </div>
    </div>
    '''


def create_and_display_html_user_events(username, urls):
    """Fetch user events and generate HTML file."""
    events_url = f"https://api.github.com/users/{username}/received_events"
    print(
        f"HTML received events generated successfully [{colors.GREEN}✓{colors.ENDC}]\n\n")

    if os.path.exists("Data/ReceivedEvents/index.html"):
        os.remove("Data/ReceivedEvents/index.html")

    try:
        response = requests.get(events_url)
        response.raise_for_status()
        data = response.json()

        with open("Data/ReceivedEvents/index.html", "a", encoding="utf_8") as f:
            stylesheet = f'''
            <head>
                <title>GitHubUserDataExtractor - Output</title>
                <link rel="icon" href="https://quantumbytestudios.in/src/images/ClassicWhiteVeryBig.png" type="image/x-icon">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
                <link rel="stylesheet" type="text/css" href="style.css">
                <script src="main.js"></script>
            </head>
            <body class="container-lg p-lg-5">
            <div class="w-100">
            '''
            f.write(stylesheet)

            for event in data:
                event_type = event['type']
                login = event["actor"]["login"]
                avatar = event["actor"]["avatar_url"]
                repo_name = event["repo"]["name"]

                if event_type == "ForkEvent":
                    forked_repo_url = event["payload"]["forkee"]["html_url"]
                    f.write(generate_html_event_row(avatar, login, event_type,
                            repo_name, forked_repo_url, "bg-danger", "Forked a repository"))

                elif event_type == "WatchEvent":
                    starred_repo_url = f"https://github.com/{repo_name}"
                    f.write(generate_html_event_row(avatar, login, event_type, repo_name,
                            starred_repo_url, "bg-warning text-dark", "Watch/Starred a repository"))

                elif event_type == "CreateEvent":
                    user_repo_url = f"https://github.com/{repo_name}"
                    f.write(generate_html_event_row(avatar, login, event_type,
                            repo_name, user_repo_url, "bg-success", "Created a repository"))

                elif event_type == "PublicEvent":
                    public_repo_url = f"https://github.com/{repo_name}"
                    f.write(generate_html_event_row(avatar, login, event_type, repo_name,
                            public_repo_url, "bg-primary", "Published a repository"))

                elif event_type == "ReleaseEvent":
                    release_repo_url = event["payload"]["release"]["html_url"]
                    f.write(generate_html_event_row(avatar, login, event_type, repo_name,
                            release_repo_url, "bg-primary", "Released a repository"))

            user_stats = f'''
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
            </div>
            </body>
            '''
            f.write(user_stats)

    except HTTPError as http_err:
        print(f"{colors.FAIL}HTTP error occurred: {http_err}{colors.ENDC}")
    except Exception as err:
        print(f"{colors.FAIL}An error occurred: {err}{colors.ENDC}")
