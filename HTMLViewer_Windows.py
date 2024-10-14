import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMessageBox, QDesktopWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class HTMLViewer(QMainWindow):
    def __init__(self, html_path):
        super().__init__()
        self.setWindowTitle("GitHubUserDataExtractor - HTML Viewer")

        self.html_path = html_path

        if not os.path.exists(self.html_path):
            QMessageBox.critical(self, "File Not Found",
                                 f"The file '{self.html_path}' does not exist.")
            sys.exit(1)  # Exit the application if file is missing

        # Set up the web view to display the HTML file
        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl.fromLocalFile(self.html_path))

        # Layout to hold the web view
        layout = QVBoxLayout()
        layout.addWidget(self.webview)

        # Main widget setup
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Adjust window properties
        self.resize(900, 800)  # Make window resizable
        self.center_on_screen()

    def center_on_screen(self):
        """Centers the window on the screen."""
        frame_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())


def showHTMLWindow():
    """Launches the PyQt5 application to display the HTML content."""
    app = QApplication(sys.argv)

    # Absolute path to the HTML file
    html_file_path = os.path.abspath("Data/ReceivedEvents/index.html")

    # Create and display the browser window
    browser = HTMLViewer(html_file_path)
    browser.show()

    # Execute the application and ensure proper exit
    sys.exit(app.exec_())
