"""Linux HTML viewer backed by pywebview/WebKit."""
import os
import sys
import webview  # type: ignore

# Suppress dconf "no database" warnings from GTK/WebKit
os.environ.setdefault("DCONF_PROFILE", "/dev/null")
# Suppress MESA ZINK (Vulkan-backed OpenGL) errors — fall back to software renderer
os.environ.setdefault("GALLIUM_DRIVER", "llvmpipe")


def show_html_linux():
    """Open the generated HTML report in a pywebview window."""
    app_name = "GitHubUserDataExtractor - HTML Viewer"
    html_file = os.path.abspath(os.path.join(
        ".temp", "index.html"))

    # Check if the file exists
    if not os.path.exists(html_file):
        print(f"Error: The file '{html_file}' does not exist.")
        sys.exit(1)  # Gracefully exit the program if the file is missing

    # Normalize path for webview
    file_url = f"file://{html_file}"

    # Open HTML File in a new pywebview window
    webview.create_window(app_name, file_url)
    webview.start()
