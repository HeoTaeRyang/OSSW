import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import Login
import Registration
import Server
import time

form_class = uic.loadUiType("ui\\login.ui")[0]
form_registration = uic.loadUiType("ui\\registration.ui")[0]
form_shop_owner = uic.loadUiType("ui\\shop_owner.ui")[0]
form_shop_owner_main = uic.loadUiType("ui\\shop_owner_main.ui")[0]
form_shop_staff = uic.loadUiType("ui\\shop_staff.ui")[0]
form_customer = uic.loadUiType("ui\\customer.ui")[0]
num = -1

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(350, 400)
        self.loginButton.clicked.connect(lambda: login())
        self.pw_lineEdit.returnPressed.connect(lambda: login())
        self.registrationButton.clicked.connect(lambda: registration())
        
        def login():
            id = self.id_lineEdit.text()
            pw = self.pw_lineEdit.text()
            classification = self.comboBox.currentIndex()
            L = Login.Login(id,pw,classification)
            num = L.getMember()
            if num < 0:
                QMessageBox.about(self,' ','ID/PW가 일치하지 않습니다')
            else:
                self.hide()
                if classification == 0:
                    self.second = shop_owner_window()
                if classification == 1:
                    self.second = shop_staff_window()
                if classification == 2:    
                    self.second = customer_window()
                    
                self.second.exec()
                self.show()
        
        def registration():
            self.hide()
            self.second = registration_window()
            self.second.exec()
            self.show()
            
class registration_window(QDialog,form_registration):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(350, 400)
        self.registrationButton.clicked.connect(lambda: registration())
        self.cancelButton.clicked.connect(lambda: cancel())
        
        def registration():
            id = self.id_lineEdit.text()
            pw = self.pw_lineEdit.text()
            pw2 = self.pw_lineEdit_2.text()
            name = self.name_lineEdit.text()
            tel1 = self.tel_lineEdit.text()
            tel2 = self.tel_lineEdit_2.text()
            tel3 = self.tel_lineEdit_3.text()
            tel = tel1 + "-" + tel2 + "-" + tel3
            classification = self.comboBox.currentIndex()
            R = Registration.Registration(id,pw,name,tel,classification)
            
            if pw != pw2:
                QMessageBox.about(self,' ','비밀번호와 비밀번호 확인이 일치하지 않습니다')
            elif not R.checkID():
                QMessageBox.about(self,' ','중복된 ID입니다')
            elif not R.checkPW():
                QMessageBox.about(self,' ','잘못된 PW입니다')
            elif not name:
                QMessageBox.about(self,' ','이름을 입력하세요')
            elif not R.checkTel():
                QMessageBox.about(self,' ','잘못된 전화번호입니다')
            else:
                R.addMember()
                QMessageBox.about(self,' ','회원가입이 완료되었습니다')
                self.close()
                
        def cancel():
            self.close()
            

class shop_owner_window(QDialog,form_shop_owner):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(600, 400)
        self.mainButton.clicked.connect(lambda: main())
        self.shopButton.clicked.connect(lambda: shop())
        self.staffButton.clicked.connect(lambda: staff())
        self.reservationButton.clicked.connect(lambda: reservation())
        self.profileButton.clicked.connect(lambda: profile())
        lambda: main()
        
        def main():
            self.mainButton.setStyleSheet("background-color: grey")
            self.shopButton.setStyleSheet("background-color: white")
            self.staffButton.setStyleSheet("background-color: white")
            self.reservationButton.setStyleSheet("background-color: white")
            self.profileButton.setStyleSheet("background-color: white")
        def shop():
            self.mainButton.setStyleSheet("background-color: white")
            self.shopButton.setStyleSheet("background-color: grey")
            self.staffButton.setStyleSheet("background-color: white")
            self.reservationButton.setStyleSheet("background-color: white")
            self.profileButton.setStyleSheet("background-color: white")
        def staff():
            self.mainButton.setStyleSheet("background-color: white")
            self.shopButton.setStyleSheet("background-color: white")
            self.staffButton.setStyleSheet("background-color: grey")
            self.reservationButton.setStyleSheet("background-color: white")
            self.profileButton.setStyleSheet("background-color: white")
        def reservation():
            self.mainButton.setStyleSheet("background-color: white")
            self.shopButton.setStyleSheet("background-color: white")
            self.staffButton.setStyleSheet("background-color: white")
            self.reservationButton.setStyleSheet("background-color: grey")
            self.profileButton.setStyleSheet("background-color: white")
        def profile():
            self.mainButton.setStyleSheet("background-color: white")
            self.shopButton.setStyleSheet("background-color: white")
            self.staffButton.setStyleSheet("background-color: white")
            self.reservationButton.setStyleSheet("background-color: white")
            self.profileButton.setStyleSheet("background-color: grey")
    
class shop_staff_window(QDialog,form_shop_staff):
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
            
class customer_window(QDialog,form_customer):
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

if __name__ == "__main__" :
    app = QApplication(sys.argv) 

    myWindow = WindowClass() 
    myWindow.show()

    app.exec_()