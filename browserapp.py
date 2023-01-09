import sys
import PyQt5
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QVBoxLayout, QHBoxLayout, QAction, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.view = QWebEngineView()
        self.url_input = QLineEdit()
        self.text_edit = QTextEdit()

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.url_input)

        # Create main widget and set layout
        main_widget = QWidget()
        main_widget.setLayout(layout)

        # Set main widget as central widget of MainWindow
        self.setCentralWidget(main_widget)

        # Create action to navigate to URL
        self.url_input.returnPressed.connect(self.navigate_to_url)

        # Create actions for file menu
        open_action = QAction("Open", self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.open_file)
        save_action = QAction("Save", self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.triggered.connect(self.save_file)

        # Add actions to file menu
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        # Create actions for edit menu
        copy_action = QAction("Copy", self)
        copy_action.setShortcut(QKeySequence.Copy)
        copy_action.triggered.connect(self.text_edit.copy)
        paste_action = QAction("Paste", self)
        paste_action.setShortcut(QKeySequence.Paste)
        paste_action.triggered.connect(self.text_edit.paste)

        # Add actions to edit menu
        edit_menu = self.menuBar().addMenu("Edit")
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)

        # Create actions for view menu
        zoom_in_action = QAction("Zoom In", self)
        zoom_in_action.setShortcut(QKeySequence.ZoomIn)
        zoom_in_action.triggered.connect(self.view.zoomIn)
        zoom_out_action = QAction("Zoom Out", self)
        zoom_out_action.setShortcut(QKeySequence.ZoomOut)
        zoom_
