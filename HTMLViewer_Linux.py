import webview
import os

def showHTMLLinux():
    # Functions & Global Variables
    appName = "GitHubUserDataExtractor - HTML Viewer"
    path = os.path.abspath(f"Data/ReceivedEvents/index.html")
    path = path.replace('\\', '/')
    # Open HTML File
    webview.create_window(appName, path)
    webview.start()