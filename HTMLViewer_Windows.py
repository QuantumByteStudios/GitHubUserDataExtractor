from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os

class HTMLViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GitHubUserDataExtractor - HTML Viewer")

        # Local path to HTML file
        self.html_path = os.path.abspath("Data/ReceivedEvents/index.html")

        # WebEngineView to display HTML content
        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl.fromLocalFile(self.html_path))

        layout = QVBoxLayout()
        layout.addWidget(self.webview)

        # Main widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set screen dimensions and center the window
        self.setFixedSize(900, 800)
        self.center_on_screen()

    def center_on_screen(self):
        frame_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())


def showHTMLWindows():
    app = QApplication([])
    browser = HTMLViewer()
    browser.show()
    app.exec_()