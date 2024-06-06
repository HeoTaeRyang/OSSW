from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Server
import Main
import My_Structs

class ProfileManagement:
    def showProfilePage(self,window,classification):
        num = Main.num
        
        if classification == 0:
            window.label_187.setText("가게 주인")
            members = Server.getShopOwners()
            shop_nums = members[num].getShopNums()
            shop_nums_s = ''
            for i in range(len(shop_nums)):
                if shop_nums_s:
                   shop_nums_s += ", "
                shop_nums_s += str(shop_nums[i])
            if shop_nums:
                window.label_391.setText(shop_nums_s)
        elif classification == 1:
            window.label_187.setText("가게 직원")
            members = Server.getShopStaffs()
            shop_num = members[num].getShopNum()
            if shop_num != -1:
                window.label_189.setText(str(shop_num))
        else:
            window.label_187.setText("손님")
            members = Server.getCustomers()
        
        window.label_185.setText(members[num].getID())
        window.label_186.setText(members[num].getName())
        window.label_184.setText(str(num))
        tel = list(members[num].getTel().split("-"))
        window.lineEdit_21.setText(tel[0])
        window.lineEdit_22.setText(tel[1])
        window.lineEdit_23.setText(tel[2])
        window.lineEdit_24.setText(members[num].getPW())
        window.lineEdit_25.setText(members[num].getPW())
        
        try:
            window.pushButton.clicked.disconnect()
        except TypeError:
            pass
        try:
            window.pushButton_2.clicked.disconnect()
        except TypeError:
            pass
        
        window.pushButton.clicked.connect(lambda: self.modTel(window,classification))
        window.pushButton_2.clicked.connect(lambda: self.modPW(window,classification))
        
    def modTel(self,window,classification):
        tel1 = window.lineEdit_21.text()
        tel2 = window.lineEdit_22.text()
        tel3 = window.lineEdit_23.text()
        
        if self.checkTel(tel1,tel2,tel3):
            tel = tel1 + "-" + tel2 + "-" + tel3
            Server.modTel(tel,Main.num,classification)
            QMessageBox.about(window,' ','전화번호가 변경되었습니다')
        else:
            QMessageBox.about(window,' ','잘못된 전화번호입니다')
        
    def checkTel(self,tel1,tel2,tel3):
        if len(tel1) != 3 or not tel1.isdigit():
            return False
        if (len(tel2) != 3 and len(tel2) != 4) or not tel2.isdigit():
            return False
        if len(tel3) != 4 or not tel3.isdigit():
            return False
        return True
        
    def modPW(self,window,classification):
        PW1 = window.lineEdit_24.text()
        PW2 = window.lineEdit_25.text()
        
        if PW1 != PW2:
            QMessageBox.about(window,' ','비밀번호가 다릅니다')
        elif self.checkPW(PW1):
            Server.modPW(PW1,Main.num,classification)
            QMessageBox.about(window,' ','비밀번호가 변경되었습니다')
        else:
            QMessageBox.about(window,' ','잘못된 PW입니다')
        
    def checkPW(self,PW1):
        if len(PW1) < 8:
            return False
        return True
        