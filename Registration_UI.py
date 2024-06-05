from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Main
import Registration

class registration_window(QDialog,Main.form_registration):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(350, 400)
        self.registrationButton.clicked.connect(lambda: self.registration())
        self.cancelButton.clicked.connect(lambda: self.cancel())
        
    def registration(self):
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
            
    def cancel(self):
        self.close()