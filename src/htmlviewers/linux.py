import webview  # type: ignore
import os
import sys


def showHTMLLinux():
    # Functions & Global Variables
    app_name = "GitHubUserDataExtractor - HTML Viewer"
    html_file = os.path.abspath(os.path.join(
        "Data", "ReceivedEvents", "index.html"))

    # Check if the file exists
    if not os.path.exists(html_file):
        print(f"Error: The file '{html_file}' does not exist.")
        sys.exit(1)  # Gracefully exit the program if the file is missing

    # Normalize path for webview
    file_url = f"file://{html_file}"

    # Open HTML File in a new pywebview window
    webview.create_window(app_name, file_url)
    webview.start()
