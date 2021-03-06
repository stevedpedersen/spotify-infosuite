"""
Fall 2017 CSc 690
File: single_frame.py
Author: Steve Pedersen & Andrew Lesondak
System: OS X
Date: 12/13/2017
Usage: python3 spotify_infosuite.py
Dependencies: pyqt5
Description: SingleFrameWindow class.  The expanded window for bio, lyrics, and reviews.

"""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QAction, QLineEdit, QVBoxLayout, QHBoxLayout, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import *
import os

class SingleFrameWindow(QWidget):
    """SingleFrameWindow is the expanded window for bio, lyrics, and reviews.  Users click a button
    to bring this window into view.

    Args:
        screen_w (int) -- width of screen where window displays
        screen_h (int) -- height of screen where window displays

    """
    def __init__(self, screen_w, screen_h):
        super().__init__()
        self.screen_w = screen_w
        self.screen_h = screen_h

    def init_popup(self, x, y, window_title, object_title):
        """Generates expanded view window

        Args:
            x (int) -- position of MultiFrameWindow
            y (int) -- position of MultiFrameWindow
            window_title (str) -- title text displayed at top of window
            object_title (str) - used to organize visual styling of elements

        """
        self.x = x
        self.y = y
        self.window_title = window_title
        self.object_title = object_title
        self.setWindowTitle(self.window_title)
        self.setObjectName(self.object_title)
        
        self.setFocus()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)


    def add_frame(self, frame):
        """Sets frame to expanded window

        Args:
            frame (object) -- frame to be added to expanded window

        """
        for component in frame.get_popup_components():
            component.show()        

        padding = 100
        self.w = 1000
        self.h = frame.popup_text.height() if (frame.popup_text.height() < self.screen_h-padding) else self.screen_h-padding
        self.x = self.screen_w/2 - self.w/2
        self.y = padding/2

        frame.popup_text.setAlignment(Qt.AlignTop)
        popup_scroll = QScrollArea()
        popup_scroll.setWidget(frame.popup_text)
        popup_scroll.setWidgetResizable(True)          
        popup_scroll.setFixedHeight(self.h)
        popup_scroll.setStyleSheet('background-color: #1D1D1D;')  
        popup_layout = QVBoxLayout(self)
        popup_layout.addWidget(popup_scroll)
       
        close_btn = QPushButton('x', self)
        close_btn.move(self.w-25, 0)
        close_btn.resize(25, 20)
        close_btn.setObjectName('close_popup_btn')
        close_btn.clicked.connect(self.close_popup)

        self.setGeometry(self.x, self.y, self.w, self.h)
        self.load_styles()

        frame.show()

    def close_popup(self):
        self.close()

    # Opens css stylesheet and apply it to Spotify Infosuite elements
    def load_styles(self):
        """Sets syling of elements in the window

        """
        self.setStyleSheet('')
        style = ''
        # with open('./view/style.css') as f:
        with open(os.path.dirname(__file__) + '/style.css') as f:
            for line in f:
                style += line
                # print(line)
        self.setStyleSheet(style)

