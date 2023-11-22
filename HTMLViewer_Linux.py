from tkinter import *
import webview
import os

def showHTMLLinux():
    tk = Tk()
    # Functions & Global Variables
    appName = "GitHubUserDataExtractor - HTML Viewer"
    path = os.path.abspath(f"Data/ReceivedEvents/index.html")
    path = path.replace('\\', '/')

    tk.title('GitHubUserDataExtractor - HTML Viewer')

    # get the screen dimension
    screen_width = tk.winfo_screenwidth()
    screen_height = tk.winfo_screenheight()

    # Set Window Width
    window_width = int(screen_width/2)
    window_height = int(screen_height/2)

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    # set the position of the window to the center of the screen
    tk.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Open HTML File
    webview.create_window(appName, path)
    webview.start()