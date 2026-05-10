"""Entry point for the GitHub User Data Extractor CLI."""
import os
import sys
import platform
import core.utils as session
from core.utils import colors


def display_banner():
    """Print the application banner and developer credits."""
    session.clear()
    banner = r'''
  ____ _ _   _   _       _       _   _                 ____        _
 / ___(_) |_| | | |_   _| |__   | | | |___  ___ _ __  |  _ \  __ _| |_ __ _
| |  _| | __| |_| | | | | '_ \  | | | / __|/ _ \ '__| | | | |/ _` | __/ _` |
| |_| | | |_|  _  | |_| | |_) | | |_| \__ \  __/ |    | |_| | (_| | || (_| |
 \____|_|\__|_| |_|\__,_|_.__/   \___/|___/\___|_|    |____/ \__,_|\__\__,_|
    '''
    print(f"{colors.GREEN}{banner}{colors.ENDC}")
    print(f"Developer: {colors.CYAN}QuantumByteStudios{colors.ENDC}")
    print(
        f"Website  : {colors.CYAN}https://quantumbytestudios.in{colors.ENDC}\n")


TOKEN_DIR = os.path.join(os.path.expanduser("~"), ".config", "githubuserdataextractor")
TOKEN_FILE = os.path.join(TOKEN_DIR, "github_token")
LEGACY_TOKEN_FILE = os.path.join(os.path.dirname(__file__), ".github_token")


def load_saved_token():
    """Return the GitHub token persisted on disk, or an empty string."""
    try:
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        try:
            with open(LEGACY_TOKEN_FILE, "r", encoding="utf-8") as f:
                token = f.read().strip()
            if token:
                save_token(token)
            return token
        except FileNotFoundError:
            return ""


def save_token(token):
    """Persist the supplied GitHub token to the token file."""
    os.makedirs(TOKEN_DIR, exist_ok=True)
    with open(TOKEN_FILE, "w", encoding="utf-8") as f:
        f.write(token)


def prompt_for_token():
    """Load a saved token or prompt the user for a new one."""
    saved = load_saved_token()
    if saved:
        os.environ["GITHUB_TOKEN"] = saved
        print(f"{colors.GREEN}Saved token loaded — "
               f"authenticated rate limit active (5,000 req/hr).{colors.ENDC}\n")
        return

    token = input(
        f"Enter a GitHub Access Token (leave blank to use unauthenticated): {colors.WARNING}"
    ).strip()
    print(colors.ENDC, end="")
    if token:
        os.environ["GITHUB_TOKEN"] = token
        save_token(token)
        print(f"{colors.GREEN}Token set and saved — "
               f"authenticated rate limit active (5,000 req/hr).{colors.ENDC}\n")
    else:
        print(f"{colors.WARNING}No token provided — "
               f"unauthenticated rate limit applies (60 req/hr).{colors.ENDC}\n")


def get_username():
    """Prompt for and return a non-empty GitHub username."""
    username = input(
        f"Enter a GitHub Username: {colors.WARNING}").strip().lower()
    print(colors.ENDC, end="")
    if not username:
        print(f"{colors.RED}Username cannot be empty!{colors.ENDC}")
        sys.exit(1)
    if username == "exit":
        print(colors.RED + 'Bye.' + colors.ENDC)
        sys.exit(0)
    return username


def get_stat_urls(username):
    """Return the mapping of stat-card URLs for the given username."""
    return {
        "mostUsedLanguages": (
            "https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language"
            f"?username={username}&theme=dark"
        ),
        "githubStats": (
            "https://github-profile-summary-cards.vercel.app/api/cards/stats"
            f"?username={username}&theme=dark"
        ),
        "streakContributionsLS": f"https://streak-stats.demolab.com/?user={username}",
        "contributorGraphOne": (
            "https://github-readme-activity-graph.vercel.app/graph"
            f"?username={username}"
            "&bg_color=000000&color=ffffff&line=ffffff"
            "&point=ffffff&area=true&hide_border=true"
        ),
        "contributorGraphTwo": (
            "https://github-profile-summary-cards.vercel.app/api/cards/profile-details"
            f"?username={username}&theme=dark"
        ),
    }


def open_html_viewer():
    """Open the generated HTML report in the platform-specific viewer."""
    html_file = os.path.join(".temp", "index.html")
    if platform.system() == "Linux":
        try:
            from htmlviewers import linux  # pylint: disable=import-outside-toplevel
            linux.show_html_linux()
        except ImportError:
            print(
                f"{colors.RED}Error: HTMLViewer_Linux module not found.{colors.ENDC}")
    elif platform.system() == "Windows":
        try:
            from htmlviewers import win as windows  # pylint: disable=import-outside-toplevel
            windows.show_html_window()
        except ImportError:
            print(
                f"{colors.RED}Error: HTMLViewer_Windows module not found.{colors.ENDC}")
    else:
        print(f"{colors.RED}Error: Unsupported platform.{colors.ENDC}")

    input("Press any key to exit...")
    try:
        with open(html_file, "w", encoding="utf_8") as f:
            f.write("")  # Clear the file content without deleting it
    except FileNotFoundError:
        print(f"{colors.WARNING}Warning: HTML file not found to clear.{colors.ENDC}")


def main():
    """Run the full extraction workflow end-to-end."""
    display_banner()
    prompt_for_token()
    username = get_username()
    urls = get_stat_urls(username)

    session.fetch_and_print_data(username)
    session.show_events_and_graphs()
    session.create_and_display_html_user_events(username, urls)
    open_html_viewer()

    print("Closing...")


if __name__ == "__main__":
    main()
