#!/usr/bin/env python

# imports
from PyQt5.QtWidgets import QApplication, QLabel, QErrorMessage, QPushButton, QLineEdit, QDialog
from PyQt5 import QtCore
import sys


# a custom dialog class containing a text field and a button
class dialog(QDialog):
    def __init__(self, width: int, height: int, title: str):
        super(dialog, self).__init__()
        self.width = width
        self.height = height
        self.title = title

    def dialog_layout(self, button_texts: list, error_message: str) -> str:
        '''A method that creates different modules for the 
           dialog and creates the layout of these modules
        
           Input: list [accept_button_text, reject_button_text]
                  str error_message
        '''
        # Set input perametes
        self.error_message = error_message
        self.input_text = ""
        # Setting the window size
        window_width = self.width/4
        window_height = self.height/13

        self.setWindowTitle(self.title)

        # change background color
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QtCore.Qt.gray)
        self.setPalette(pal)

        # creating models
        if len(button_texts) == 2:
            button_accept = QPushButton(button_texts[0], self)
            button_reject = QPushButton(button_texts[1], self)
        else:
            button_accept = QPushButton(button_texts[0], self)
        self.text_field = QLineEdit(self)
        self.error_label = QLabel(self)

        # Setting size
        self.setMinimumSize(window_width, window_height)
        self.setFixedSize(window_width, window_height)
        self.error_label.setMinimumSize(80,20)

        # Change color
        self.error_label.setStyleSheet("color: red")

        # arrange modules in the window
        if len(button_texts) == 2:
            button_accept.move(window_width/2, window_height/1.5)
            button_reject.move(window_width/3.5, window_height/1.5)
        else:
            button_accept.move(window_width/2, window_height/1.5)
        self.text_field.setFixedWidth(self.width/5)
        self.text_field.move(window_width/10, window_height/3)
        self.error_label.move(window_width/1.45, window_height/1.5)
    
        # event listeners
        if len(button_texts) == 2:
            button_accept.clicked.connect(self.button_accept_action)
            button_reject.clicked.connect(self.button_reject_action)
        else:
            button_accept.clicked.connect(self.button_accept_action)
        self.keyPressEvent = self.enter_key_pressed

        self.exec_()
        return self.input_text

    # Button actions
    @QtCore.pyqtSlot()
    def button_accept_action(self) -> str:
        if(len(self.text_field.text()) < 1):
            self.error_label.setText(self.error_message)
        else:
            self.accept()
            self.input_text = self.text_field.text()

    @QtCore.pyqtSlot()
    def button_reject_action(self):
        self.reject()
    
    @QtCore.pyqtSlot()
    def enter_key_pressed(self, e):
        if e.key() == QtCore.Qt.Key_Enter or e.key() == QtCore.Qt.Key_Return:
            self.accept()
            self.input_text = self.text_field.text()
        elif e.key() == QtCore.Qt.Key_Escape:
            self.reject()


def start_gui(button_text=[], error_text="No entry given", title = "No title given") -> str:
    '''
        Input: list [accept_button_text, reject_button_text]
               str error_text
    '''
    app = QApplication([])
    screen_res = app.desktop().screenGeometry()
    width, height = screen_res.width(), screen_res.height()
    inputd = dialog(width, height, title)
    input_text = inputd.dialog_layout(button_text, error_text)
    app.closeAllWindows()
    app.quit()
    return input_text
