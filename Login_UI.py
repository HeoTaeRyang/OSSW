from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Main
import Login
import Registration_UI
import Shop_Owner_UI
import Shop_Staff_UI
import Customer_UI

class login_window(QMainWindow, Main.form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(350, 400)
        self.loginButton.clicked.connect(lambda: self.login())
        self.pw_lineEdit.returnPressed.connect(lambda: self.login())
        self.registrationButton.clicked.connect(lambda: self.registration())
        
    def login(self):
        id = self.id_lineEdit.text()
        pw = self.pw_lineEdit.text()
        classification = self.comboBox.currentIndex()
        L = Login.Login(id,pw,classification)
        Main.num = L.getMember()
        if Main.num < 0:
            QMessageBox.about(self,' ','ID/PW가 일치하지 않습니다')
        else:
            self.hide()
            if classification == 0:
                self.second = Shop_Owner_UI.shop_owner_window()
            if classification == 1:
                self.second = Shop_Staff_UI.shop_staff_window()
            if classification == 2:    
                self.second = Customer_UI.customer_window()
                
            self.second.exec()
            self.show()
        
    def registration(self):
        self.hide()
        self.second = Registration_UI.registration_window()
        self.second.exec()
        self.show()