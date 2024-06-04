import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Server
import My_Structs
import Login
import Registration

form_class = uic.loadUiType("ui\\login.ui")[0]
form_registration = uic.loadUiType("ui\\registration.ui")[0]
form_shop_owner = uic.loadUiType("ui\\shop_owner.ui")[0]
form_shop_staff = uic.loadUiType("ui\\shop_staff.ui")[0]
form_customer = uic.loadUiType("ui\\customer.ui")[0]
num = -1
Server.shop_owners[0].info()

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
        self.shopButton.clicked.connect(lambda: shop(num))
        self.staffButton.clicked.connect(lambda: staff())
        self.reservationButton.clicked.connect(lambda: reservation())
        self.profileButton.clicked.connect(lambda: profile())
        self.mainButton.setStyleSheet("background-color: white")
        self.shopButton.setStyleSheet("background-color: white")
        self.staffButton.setStyleSheet("background-color: white")
        self.reservationButton.setStyleSheet("background-color: white")
        self.profileButton.setStyleSheet("background-color: white")
        self.stackedWidget.setCurrentIndex(0)
        
        def main():
            self.mainButton.setStyleSheet("background-color: grey")
            self.shopButton.setStyleSheet("background-color: white")
            self.staffButton.setStyleSheet("background-color: white")
            self.reservationButton.setStyleSheet("background-color: white")
            self.profileButton.setStyleSheet("background-color: white")
            self.stackedWidget.setCurrentIndex(0)
            layout = QVBoxLayout()
            for i in range(len(Server.shops)):
                if Server.shops[i].getNum() != -1:
                    button = QPushButton(Server.shops[i].getName())
                    button.clicked.connect(lambda checked, i=i: main2(i))
                    button.setFixedHeight(30)
                    layout.addWidget(button)
            
            content_widget = QWidget()
            content_widget.setLayout(layout)
            self.scrollArea.setWidget(content_widget)
            layout.addStretch(1)
        
        def main2(shop_num):
            self.stackedWidget.setCurrentIndex(1)
            self.name.setText(Server.shops[shop_num].getName())
            self.address.setText(Server.shops[shop_num].getAddress())
            self.backButton.clicked.connect(lambda: main())
            tmp_l = Server.shops[shop_num].getOperationHours()
            operation_hours_s = ""
            if tmp_l[0] != -1:
                operation_hours_s += "월 " + str(tmp_l[0]*30//60).zfill(2) + ":" + str(tmp_l[0]*30%60).zfill(2) + " ~ " + str(tmp_l[1]*30//60).zfill(2) + ":" + str(tmp_l[1]*30%60).zfill(2)
            else:
                operation_hours_s += "월 휴무"
            operation_hours_s += "\n"
            if tmp_l[2] != -1:
                operation_hours_s += "화 " + str(tmp_l[2]*30//60).zfill(2) + ":" + str(tmp_l[2]*30%60).zfill(2) + " ~ " + str(tmp_l[3]*30//60).zfill(2) + ":" + str(tmp_l[3]*30%60).zfill(2)
            else:
                operation_hours_s += "화 휴무"
            operation_hours_s += "\n"
            if tmp_l[4] != -1:
                operation_hours_s += "수 " + str(tmp_l[4]*30//60).zfill(2) + ":" + str(tmp_l[4]*30%60).zfill(2) + " ~ " + str(tmp_l[5]*30//60).zfill(2) + ":" + str(tmp_l[5]*30%60).zfill(2)
            else:
                operation_hours_s += "수 휴무"
            operation_hours_s += "\n"
            if tmp_l[6] != -1:
                operation_hours_s += "목 " + str(tmp_l[6]*30//60).zfill(2) + ":" + str(tmp_l[6]*30%60).zfill(2) + " ~ " + str(tmp_l[7]*30//60).zfill(2) + ":" + str(tmp_l[7]*30%60).zfill(2)
            else:
                operation_hours_s += "목 휴무"
            operation_hours_s += "\n"
            if tmp_l[8] != -1:
                operation_hours_s += "금 " + str(tmp_l[8]*30//60).zfill(2) + ":" + str(tmp_l[8]*30%60).zfill(2) + " ~ " + str(tmp_l[9]*30//60).zfill(2) + ":" + str(tmp_l[9]*30%60).zfill(2)
            else:
                operation_hours_s += "금 휴무"
            operation_hours_s += "\n"
            if tmp_l[10] != -1:
                operation_hours_s += "토 " + str(tmp_l[10]*30//60).zfill(2) + ":" + str(tmp_l[10]*30%60).zfill(2) + " ~ " + str(tmp_l[11]*30//60).zfill(2) + ":" + str(tmp_l[11]*30%60).zfill(2)
            else:
                operation_hours_s += "토 휴무"
            operation_hours_s += "\n"
            if tmp_l[12] != -1:
                operation_hours_s += "일 " + str(tmp_l[12]*30//60).zfill(2) + ":" + str(tmp_l[12]*30%60).zfill(2) + " ~ " + str(tmp_l[13]*30//60).zfill(2) + ":" + str(tmp_l[13]*30%60).zfill(2)
            else:
                operation_hours_s += "일 휴무"
            
            self.operation_hours.setText(operation_hours_s)
            self.tel.setText(Server.shops[shop_num].getTel())
                
        def shop(shop_owner_num):
            self.stackedWidget.setCurrentIndex(2)
            self.mainButton.setStyleSheet("background-color: white")
            self.shopButton.setStyleSheet("background-color: grey")
            self.staffButton.setStyleSheet("background-color: white")
            self.reservationButton.setStyleSheet("background-color: white")
            self.profileButton.setStyleSheet("background-color: white")
            layout = QVBoxLayout()
            shop_nums = Server.shop_owners[shop_owner_num].getShopNums()
            for i in range(len(shop_nums)):
                item_widget = QWidget()
                item_layout = QHBoxLayout()
                
                label = QLabel(Server.shops[shop_nums[i]].getName())
                button1 = QPushButton("수정")
                button2 = QPushButton("삭제")
                label.setFixedHeight(20)
                button1.setFixedSize(50,20)
                button2.setFixedSize(50,20)
                
                button1.clicked.connect(lambda checked, i=i: shop2(shop_nums[i]))
                button2.clicked.connect(lambda checked, i=i: delshop(shop_nums[i]))
                
                item_layout.addWidget(label)
                item_layout.addWidget(button1)
                item_layout.addWidget(button2)
                item_widget.setLayout(item_layout)
                item_widget.setFixedHeight(30)
                layout.addWidget(item_widget)
            button = QPushButton("추가")
            button.setFixedHeight(30)
            button.clicked.connect(lambda : shop3())
            
            layout.addWidget(button)
            
            content_widget = QWidget()
            content_widget.setLayout(layout)
            layout.addWidget(button)
            self.scrollArea_3.setWidget(content_widget)
            layout.addStretch(1)
            
        def shop2(shop_num):
            self.stackedWidget.setCurrentIndex(3)
            self.cancelButton.clicked.connect(lambda : shop(num))
            self.okButton.clicked.connect(lambda : ok())
            self.name_5.setText(Server.shops[shop_num].getName())
                
            def ok():
                tel1 = self.lineEdit_2.text()
                tel2 = self.lineEdit_3.text()
                tel3 = self.lineEdit_4.text()
                if not tel1.isdigit() or not tel2.isdigit() or not tel3.isdigit():
                    QMessageBox.about(self,' ','잘못된 전화번호입니다')
                else:
                    address = self.lineEdit.text()
                    tel = tel1 + '-' + tel2 + '-' + tel3
                    operation_hours = []
                    if self.checkBox.isChecked():
                        operation_hours += [-1,-1]
                    else:  
                        operation_hours += [self.spinBox.value()*2 + self.spinBox_8.value()//30, self.spinBox_15.value()*2 + self.spinBox_22.value()//30]
                    if self.checkBox_2.isChecked():
                        operation_hours += [-1,-1]
                    
                    else:
                        operation_hours += [self.spinBox_2.value()*2 + self.spinBox_9.value()//30, self.spinBox_16.value()*2 + self.spinBox_23.value()//30]
                    
                    if self.checkBox_3.isChecked():
                        operation_hours += [-1,-1]
                    
                    else:  
                        operation_hours += [self.spinBox_3.value()*2 + self.spinBox_10.value()//30, self.spinBox_17.value()*2 + self.spinBox_24.value()//30]
                    
                    if self.checkBox_4.isChecked():
                        operation_hours += [-1,-1]
                    
                    else:  
                        operation_hours += [self.spinBox_4.value()*2 + self.spinBox_11.value()//30, self.spinBox_18.value()*2 + self.spinBox_25.value()//30]
                    
                    if self.checkBox_5.isChecked():
                        operation_hours += [-1,-1]
                    
                    else:  
                        operation_hours += [self.spinBox_5.value()*2 + self.spinBox_12.value()//30, self.spinBox_19.value()*2 + self.spinBox_26.value()//30]
                    
                    if self.checkBox_6.isChecked():
                        operation_hours += [-1,-1]
                    
                    else:  
                        operation_hours += [self.spinBox_6.value()*2 + self.spinBox_13.value()//30, self.spinBox_20.value()*2 + self.spinBox_27.value()//30]
                    
                    if self.checkBox_7.isChecked():
                        operation_hours += [-1,-1]

                    else:  
                        operation_hours += [self.spinBox_7.value()*2 + self.spinBox_14.value()//30, self.spinBox_21.value()*2 + self.spinBox_28.value()//30]
                    Server.modShop(shop_num,My_Structs.Shop(Server.shops[shop_num].getName(),address,tel,operation_hours,shop_num))
                    QMessageBox.about(self,' ','가게 수정이 완료되었습니다')
                    shop(num)
                
        def delshop(shop_num):
            buttonReply = QMessageBox.information(self,' ','삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
            
            if buttonReply == QMessageBox.Yes:
                Server.delShop(shop_num,num)
                shop(num)
            
        
        def shop3():
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.lineEdit_8.setText("")
            self.lineEdit_9.setText("가게 이름")
            
            self.stackedWidget.setCurrentIndex(4)
            self.cancelButton_2.clicked.connect(lambda: shop(num))
            self.okButton_2.disconnect()
            self.okButton_2.clicked.connect(lambda: ok2())
            
        def ok2():
                tel1 = self.lineEdit_8.text()
                tel2 = self.lineEdit_6.text()
                tel3 = self.lineEdit_5.text()
                if not tel1.isdigit() or not tel2.isdigit() or not tel3.isdigit():
                    QMessageBox.about(self,' ','잘못된 전화번호입니다')
                else:
                    name = self.lineEdit_9.text()
                    address = self.lineEdit_7.text()
                    tel = tel1 + '-' + tel2 + '-' + tel3
                    operation_hours = []
                    if self.checkBox.isChecked():
                        operation_hours += [-1,-1]
                    else:  
                        operation_hours += [self.spinBox_54.value()*2 + self.spinBox_56.value()//30, self.spinBox_43.value()*2 + self.spinBox_40.value()//30]
                    if self.checkBox_2.isChecked():
                        operation_hours += [-1,-1]
                    
                    else:
                        operation_hours += [self.spinBox_42.value()*2 + self.spinBox_36.value()//30, self.spinBox_37.value()*2 + self.spinBox_38.value()//30]
                    
                    if self.checkBox_3.isChecked():
                        operation_hours += [-1,-1]
                    
                    else:  
                        operation_hours += [self.spinBox_35.value()*2 + self.spinBox_51.value()//30, self.spinBox_53.value()*2 + self.spinBox_48.value()//30]
                    
                    if self.checkBox_4.isChecked():
                        operation_hours += [-1,-1]
                    
                    else:  
                        operation_hours += [self.spinBox_55.value()*2 + self.spinBox_47.value()//30, self.spinBox_41.value()*2 + self.spinBox_44.value()//30]
                    
                    if self.checkBox_5.isChecked():
                        operation_hours += [-1,-1]
                    
                    else:  
                        operation_hours += [self.spinBox_33.value()*2 + self.spinBox_46.value()//30, self.spinBox_49.value()*2 + self.spinBox_32.value()//30]
                    
                    if self.checkBox_6.isChecked():
                        operation_hours += [-1,-1]
                    
                    else:  
                        operation_hours += [self.spinBox_34.value()*2 + self.spinBox_45.value()//30, self.spinBox_50.value()*2 + self.spinBox_39.value()//30]
                    
                    if self.checkBox_7.isChecked():
                        operation_hours += [-1,-1]

                    else:  
                        operation_hours += [self.spinBox_29.value()*2 + self.spinBox_52.value()//30, self.spinBox_31.value()*2 + self.spinBox_30.value()//30]
                    shop_num = -1
                    for i in range(len(Server.shops)):
                        if Server.shops[i].getNum() == -1:
                            shop_num = i
                            break
                    if shop_num == -1:
                        shop_num = len(Server.shops)
                    
                    Server.addShop(My_Structs.Shop(name,address,tel,operation_hours,shop_num))
                    Server.addShopToShopOwner(num,shop_num)
                    QMessageBox.about(self,' ','가게 생성이 완료되었습니다')
                    shop(num)
            
            
            
            
            
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