from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Server
import Main
import My_Structs
import ShopInfo
import os

class shop_owner_window(QDialog,Main.form_shop_owner):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(600, 400)
        self.mainButton.clicked.connect(lambda: self.main_page())
        self.shopButton.clicked.connect(lambda: self.shop_page(Main.num))
        self.staffButton.clicked.connect(lambda: self.staff_page(Main.num))
        self.reservationButton.clicked.connect(lambda: self.reservation_page())
        self.profileButton.clicked.connect(lambda: self.profile_page())
        self.mainButton.setStyleSheet("background-color: white")
        self.shopButton.setStyleSheet("background-color: white")
        self.staffButton.setStyleSheet("background-color: white")
        self.reservationButton.setStyleSheet("background-color: white")
        self.profileButton.setStyleSheet("background-color: white")
        self.stackedWidget.setCurrentIndex(0)
        
    def main_page(self):
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
                button.clicked.connect(lambda checked, i=i: self.main_shop_info_page(i))
                button.setFixedHeight(30)
                layout.addWidget(button)
        
        content_widget = QWidget()
        content_widget.setLayout(layout)
        self.scrollArea.setWidget(content_widget)
        layout.addStretch(1)
    
    def main_shop_info_page(self,shop_num):
        self.stackedWidget.setCurrentIndex(1)
        self.name.setText(Server.shops[shop_num].getName())
        self.address.setText(Server.shops[shop_num].getAddress())
        self.backButton.clicked.connect(lambda: self.main_page())
        si = ShopInfo.ShopInfo()
        self.operation_hours.setText(si.ShopList(Server.shops[shop_num].getOperationHours()))
        self.tel.setText(Server.shops[shop_num].getTel())
            
    def shop_page(self,shop_owner_num):
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
            
            button1.clicked.connect(lambda checked, i=i: self.shop_mod_page(shop_nums[i]))
            button2.clicked.connect(lambda checked, i=i: self.delshop(shop_nums[i]))
            
            item_layout.addWidget(label)
            item_layout.addWidget(button1)
            item_layout.addWidget(button2)
            item_widget.setLayout(item_layout)
            item_widget.setFixedHeight(30)
            layout.addWidget(item_widget)
        button = QPushButton("추가")
        button.setFixedHeight(30)
        button.clicked.connect(lambda : self.shop_add_page())
        
        content_widget = QWidget()
        content_widget.setLayout(layout)
        layout.addWidget(button)
        self.scrollArea_3.setWidget(content_widget)
        layout.addStretch(1)
        
    def shop_mod_page(self,shop_num):
        self.stackedWidget.setCurrentIndex(3)
        self.cancelButton.clicked.connect(lambda : self.shop_page(Main.num))
        self.okButton.clicked.connect(lambda : self.mod_ok(shop_num))
        self.name_5.setText(Server.shops[shop_num].getName())
        self.lineEdit.setText(Server.shops[shop_num].getAddress())
        tel = list(Server.shops[shop_num].getTel().split("-"))
        self.lineEdit_2.setText(tel[0])
        self.lineEdit_3.setText(tel[1])
        self.lineEdit_4.setText(tel[2])
        operation_hours = Server.shops[shop_num].getOperationHours()
        
        if operation_hours[0] == -1:
            self.spinBox.setValue(0)
            self.spinBox_8.setValue(0)
            self.spinBox_15.setValue(0)
            self.spinBox_22.setValue(0)
            self.checkBox.setChecked(True)
        else:
            self.spinBox.setValue(operation_hours[0]//2)
            self.spinBox_8.setValue(operation_hours[0]%2*30)
            self.spinBox_15.setValue(operation_hours[1]//2)
            self.spinBox_22.setValue(operation_hours[1]%2*30)
            
        if operation_hours[2] == -1:
            self.spinBox_2.setValue(0)
            self.spinBox_9.setValue(0)
            self.spinBox_16.setValue(0)
            self.spinBox_23.setValue(0)
            self.checkBox_2.setChecked(True)
        else:
            self.spinBox_2.setValue(operation_hours[2]//2)
            self.spinBox_9.setValue(operation_hours[2]%2*30)
            self.spinBox_16.setValue(operation_hours[3]//2)
            self.spinBox_23.setValue(operation_hours[3]%2*30)
            
        if operation_hours[4] == -1:
            self.spinBox_3.setValue(0)
            self.spinBox_10.setValue(0)
            self.spinBox_17.setValue(0)
            self.spinBox_24.setValue(0)
            self.checkBox_3.setChecked(True)
        else:
            self.spinBox_3.setValue(operation_hours[4]//2)
            self.spinBox_10.setValue(operation_hours[4]%2*30)
            self.spinBox_17.setValue(operation_hours[5]//2)
            self.spinBox_24.setValue(operation_hours[5]%2*30)
            
        if operation_hours[6] == -1:
            self.spinBox_4.setValue(0)
            self.spinBox_11.setValue(0)
            self.spinBox_18.setValue(0)
            self.spinBox_25.setValue(0)
            self.checkBox_4.setChecked(True)
        else:
            self.spinBox_4.setValue(operation_hours[6]//2)
            self.spinBox_11.setValue(operation_hours[6]%2*30)
            self.spinBox_18.setValue(operation_hours[7]//2)
            self.spinBox_25.setValue(operation_hours[7]%2*30)
            
        if operation_hours[8] == -1:
            self.spinBox_5.setValue(0)
            self.spinBox_12.setValue(0)
            self.spinBox_19.setValue(0)
            self.spinBox_26.setValue(0)
            self.checkBox_5.setChecked(True)
        else:
            self.spinBox_5.setValue(operation_hours[8]//2)
            self.spinBox_12.setValue(operation_hours[8]%2*30)
            self.spinBox_19.setValue(operation_hours[9]//2)
            self.spinBox_26.setValue(operation_hours[9]%2*30)
            
        if operation_hours[10] == -1:
            self.spinBox_6.setValue(0)
            self.spinBox_13.setValue(0)
            self.spinBox_20.setValue(0)
            self.spinBox_27.setValue(0)
            self.checkBox_6.setChecked(True)
        else:
            self.spinBox_6.setValue(operation_hours[10]//2)
            self.spinBox_13.setValue(operation_hours[10]%2*30)
            self.spinBox_20.setValue(operation_hours[11]//2)
            self.spinBox_27.setValue(operation_hours[11]%2*30)
            
        if operation_hours[12] == -1:
            self.spinBox_7.setValue(0)
            self.spinBox_14.setValue(0)
            self.spinBox_21.setValue(0)
            self.spinBox_28.setValue(0)
            self.checkBox_7.setChecked(True)
        else:
            self.spinBox_7.setValue(operation_hours[12]//2)
            self.spinBox_14.setValue(operation_hours[12]%2*30)
            self.spinBox_21.setValue(operation_hours[13]//2)
            self.spinBox_28.setValue(operation_hours[13]%2*30)
        
        
            
    def mod_ok(self,shop_num):
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
            for i in range(7):
                if operation_hours[i*2] == operation_hours[i*2+1]:
                    operation_hours[i*2] = -1
                    operation_hours[i*2+1] = -1
            if self.check_operation_hours(operation_hours):
                QMessageBox.about(self,' ','시간이 잘못 입력되었습니다')
            else:
                Server.modShop(shop_num,My_Structs.Shop(Server.shops[shop_num].getName(),address,tel,operation_hours,shop_num))
                QMessageBox.about(self,' ','가게 수정이 완료되었습니다')
                self.shop_page(Main.num)
                    
    def check_operation_hours(self,operations_hours):
        for i in range(7):
            if operations_hours[i*2] > operations_hours[i*2+1] or operations_hours[i*2] > 48 or operations_hours[i*2+1] > 48 :
                return True
        return False
            
    def delshop(self,shop_num):
        buttonReply = QMessageBox.information(self,' ','삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        
        if buttonReply == QMessageBox.Yes:
            Server.delShop(shop_num,Main.num)
            self.shop_page(Main.num)
        
    
    def shop_add_page(self):
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("가게 이름")
        
        self.stackedWidget.setCurrentIndex(4)
        self.cancelButton_2.clicked.connect(lambda: self.shop_page(Main.num))
        self.okButton_2.disconnect()
        self.okButton_2.clicked.connect(lambda: self.add_ok())
        
    def add_ok(self):
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
                
                Server.addShop(Main.num,My_Structs.Shop(name,address,tel,operation_hours,shop_num))
                QMessageBox.about(self,' ','가게 생성이 완료되었습니다')
                self.shop_page(Main.num)
        
    def staff_page(self,shop_owner_num):
        self.mainButton.setStyleSheet("background-color: white")
        self.shopButton.setStyleSheet("background-color: white")
        self.staffButton.setStyleSheet("background-color: grey")
        self.reservationButton.setStyleSheet("background-color: white")
        self.profileButton.setStyleSheet("background-color: white")
        self.stackedWidget.setCurrentIndex(5)
        shop_nums = Server.shop_owners[shop_owner_num].getShopNums()
        self.comboBox.clear()
        self.comboBox.addItem("가게 선택")
        self.scrollArea_4.setWidget(QWidget())
        
        for i in range(len(shop_nums)):
            self.comboBox.addItem(Server.shops[shop_nums[i]].getName())
        self.comboBox.model().item(0).setEnabled(False)
        
        self.okButton_5.clicked.connect(lambda: self.staff_info_page(shop_nums))
        
        
    def staff_info_page(self,shop_nums):
        selected_shop_index = self.comboBox.currentIndex() - 1
        if selected_shop_index < 0:
            return
        
        shop_num = shop_nums[self.comboBox.currentIndex() - 1]
        
        staff_nums = list(map(int,os.listdir(f"db\\shops\\{shop_num}")))
        
        layout = QVBoxLayout()
        for i in range(len(staff_nums)):
            item_widget = QWidget()
            item_layout = QHBoxLayout()
            
            label1 = QLabel(Server.shop_staffs[staff_nums[i]].getName())
            procedures = Server.getProcedures(shop_num ,staff_nums[i])
            procedures_s = ""
            for j in range(len(procedures)):
                if procedures_s:
                    procedures_s += "/"
                procedures_s += procedures[j].getName()+"("+ str(procedures[j].getTime()//2) + ":" + str(procedures[j].getTime()%2*30).zfill(2) +")"
            label2 = QLabel(procedures_s)
            button1 = QPushButton("수정")
            button2 = QPushButton("삭제")
            label1.setFixedHeight(20)
            label2.setFixedHeight(20)
            button1.setFixedSize(50,20)
            button2.setFixedSize(50,20)
            
            button1.clicked.connect(lambda checked, i=i: self.staff_mod_page(shop_num,staff_nums[i]))
            button2.clicked.connect(lambda checked, i=i: self.delstaff(shop_num,staff_nums[i]))
            
            item_layout.addWidget(label1)
            item_layout.addWidget(label2)
            item_layout.addWidget(button1)
            item_layout.addWidget(button2)
            item_widget.setLayout(item_layout)
            item_widget.setFixedHeight(30)
            layout.addWidget(item_widget)
        button = QPushButton("추가")
        button.setFixedHeight(30)
        button.clicked.connect(lambda : self.staff_add_page(shop_num))
        
        layout.addWidget(button)
        layout.addStretch(1)
        
        content_widget = QWidget()
        content_widget.setLayout(layout)
        self.scrollArea_4.setWidget(content_widget)
        
        
    def staff_mod_page(self,shop_num,staff_num):
        self.stackedWidget.setCurrentIndex(6)
        self.label_5.setText(Server.shops[shop_num].getName())
        self.label_6.setText(Server.shop_staffs[staff_num].getName())
        
        procedures =  Server.getProcedures(shop_num, staff_num)
        layout = QVBoxLayout()
        for i in range(len(procedures)):
            item_widget = QWidget()
            item_layout = QHBoxLayout()
            
            label1 = QLabel(procedures[i].getName())
            label2 = QLabel(str(procedures[i].getTime()//2).zfill(2) + ":" + str(procedures[i].getTime()%2*30).zfill(2))
            button = QPushButton("삭제")
            label1.setFixedHeight(20)
            label2.setFixedHeight(20)
            button.setFixedSize(50,20)
            
            button.clicked.connect(lambda checked, i=i: delProcedure(i))
            
            item_layout.addWidget(label1)
            item_layout.addWidget(label2)
            item_layout.addWidget(button)
            item_widget.setLayout(item_layout)
            item_widget.setFixedHeight(30)
            layout.addWidget(item_widget)
            
        item_widget2 = QWidget()
        item_layout2 = QHBoxLayout()    
            
        line = QLineEdit("시술명")
        line.setFixedSize(100,20)
        
        spin1 = QSpinBox()
        spin1.setMinimum(0)
        spin1.setMaximum(24)
        spin1.setSingleStep(1)
        spin1.setFixedSize(50,20)
        
        label = QLabel(":")
        label.setFixedSize(10,20)
            
        spin2 = QSpinBox()
        spin2.setMinimum(0)
        spin2.setMaximum(30)
        spin2.setSingleStep(30)
        spin2.setFixedSize(50,20)
        
        button2 = QPushButton("추가")
        button2.setFixedSize(30,20)
        button2.clicked.connect(lambda : addProcedure())
        
        item_layout2.addWidget(line)
        item_layout2.addStretch(1)
        item_layout2.addWidget(spin1)
        item_layout2.addWidget(label)
        item_layout2.addWidget(spin2)
        item_layout2.addStretch(1)
        item_layout2.addWidget(button2)
        
        item_widget2.setLayout(item_layout2)
        item_widget2.setFixedHeight(30)
        layout.addWidget(item_widget2)
        layout.addStretch(1)
        
        content_widget = QWidget()
        content_widget.setLayout(layout)
        
        self.scrollArea_5.setWidget(content_widget)
        
        self.okButton_3.clicked.connect(lambda : self.staff_page(Main.num))
        
        def addProcedure():
            name = line.text()
            time = spin1.value()*2 + spin2.value()//30
            if Server.addProcedureToStaff(My_Structs.Procedure(name,time),shop_num,staff_num):
                self.staff_mod_page(shop_num,staff_num)
            else:
                QMessageBox.about(self,' ','중복된 시술 이름입니다')
                
        def delProcedure(procedure_num):
            Server.delProcedureToStaff(procedure_num, shop_num, staff_num)
            self.staff_mod_page(shop_num,staff_num)
        
    def delstaff(self,shop_num, staff_num):
        buttonReply = QMessageBox.information(self,' ','삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
    
        if buttonReply == QMessageBox.Yes:
            Server.delStaffToShop(shop_num,staff_num)
            self.staff_page(Main.num)
        
    def staff_add_page(self,shop_num):
        self.stackedWidget.setCurrentIndex(7)
        self.label_8.setText(Server.shops[shop_num].getName())
        self.okButton_4.clicked.connect(lambda : self.addStaff(shop_num))
        self.cancelButton_3.clicked.connect(lambda : self.staff_page(Main.num))
        
    def addStaff(self,shop_num):
        staff_num = int(self.lineEdit_10.text())
        print(f"shop_num = {shop_num}")
        result = Server.addStaffToShop(shop_num, staff_num)
        if result == 1:
            self.staff_page(Main.num)
        elif result == -1:
            QMessageBox.about(self,' ','이미 가게에 등록된 회원입니다')
        else:
            QMessageBox.about(self,' ','유효하지않은 회원번호입니다')
                    
    # def reservation(self):
    #     self.mainButton.setStyleSheet("background-color: white")
    #     self.shopButton.setStyleSheet("background-color: white")
    #     self.staffButton.setStyleSheet("background-color: white")
    #     self.reservationButton.setStyleSheet("background-color: grey")
    #     self.profileButton.setStyleSheet("background-color: white")
    # def profile(self):
    #     self.mainButton.setStyleSheet("background-color: white")
    #     self.shopButton.setStyleSheet("background-color: white")
    #     self.staffButton.setStyleSheet("background-color: white")
    #     self.reservationButton.setStyleSheet("background-color: white")
    #     self.profileButton.setStyleSheet("background-color: grey")