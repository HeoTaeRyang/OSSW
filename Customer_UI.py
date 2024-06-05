from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Main

class customer_window(QDialog,Main.form_customer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(600, 400)
        self.mainButton.clicked.connect(lambda: main())
        self.reservationButton.clicked.connect(lambda: reservation())
        self.profileButton.clicked.connect(lambda: profile())
        lambda: main()
        
        def main():
            self.mainButton.setStyleSheet("background-color: grey")
            self.reservationButton.setStyleSheet("background-color: white")
            self.profileButton.setStyleSheet("background-color: white")
        def reservation():
            self.mainButton.setStyleSheet("background-color: white")
            self.reservationButton.setStyleSheet("background-color: grey")
            self.profileButton.setStyleSheet("background-color: white")
        def profile():
            self.mainButton.setStyleSheet("background-color: white")
            self.reservationButton.setStyleSheet("background-color: white")
            self.profileButton.setStyleSheet("background-color: grey")