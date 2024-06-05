from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Main

class shop_staff_window(QDialog,Main.form_shop_staff):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(600, 400)
        self.mainButton.clicked.connect(lambda: main())
        self.reservationButton.clicked.connect(lambda: reservation())
        self.scheduleButton.clicked.connect(lambda: schedule())
        self.profileButton.clicked.connect(lambda: profile())
        lambda: main()
        
        def main():
            self.mainButton.setStyleSheet("background-color: grey")
            self.reservationButton.setStyleSheet("background-color: white")
            self.scheduleButton.setStyleSheet("background-color: white")
            self.profileButton.setStyleSheet("background-color: white")
        def reservation():
            self.mainButton.setStyleSheet("background-color: white")
            self.reservationButton.setStyleSheet("background-color: grey")
            self.scheduleButton.setStyleSheet("background-color: white")
            self.profileButton.setStyleSheet("background-color: white")
        def schedule():
            self.mainButton.setStyleSheet("background-color: white")
            self.reservationButton.setStyleSheet("background-color: white")
            self.scheduleButton.setStyleSheet("background-color: grey")
            self.profileButton.setStyleSheet("background-color: white")
        def profile():
            self.mainButton.setStyleSheet("background-color: white")
            self.reservationButton.setStyleSheet("background-color: white")
            self.scheduleButton.setStyleSheet("background-color: white")
            self.profileButton.setStyleSheet("background-color: grey")