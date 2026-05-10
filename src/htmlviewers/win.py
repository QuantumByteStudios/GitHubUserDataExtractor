"""Windows HTML viewer backed by PyQt5 QWebEngineView."""
import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QMessageBox, QDesktopWidget
)
from PyQt5.QtWebEngineWidgets import QWebEngineView


class HTMLViewer(QMainWindow):  # pylint: disable=too-few-public-methods  # noqa: D203,D211
    """Main window that renders the generated HTML report."""

    def __init__(self, html_path):
        """Initialize the viewer window for the given HTML file path."""
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
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setStretch(0, 1)

        # Main widget setup
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Adjust window properties
        self.resize(1000, 800)  # Make window resizable
        self.center_on_screen()

    def center_on_screen(self):
        """Centers the window on the screen."""
        frame_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())


def show_html_window():
    """Launch the PyQt5 application and display the HTML content."""
    app = QApplication(sys.argv)

    # Absolute path to the HTML file
    html_file_path = os.path.abspath(".temp/index.html")

    # Create and display the browser window
    browser = HTMLViewer(html_file_path)
    browser.show()

    # Execute the application and capture the exit code so cleanup can run.
    exit_code = app.exec_()

    # Delete the HTML file after closing the viewer
    try:
        os.remove(html_file_path)
    except FileNotFoundError:
        print(f"Warning: HTML file '{html_file_path}' not found to delete.")
    except OSError as e:
        print(f"Error deleting HTML file: {e}")

    # Exit with the same code returned by Qt.
    sys.exit(exit_code)
