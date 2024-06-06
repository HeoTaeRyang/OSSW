from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Server
import Main
import My_Structs
import os

class StaffManagement:
    def showStaffPage(self,window):
        shop_owner_num = Main.num
        shop_owners = Server.getShopOwners()
        shops = Server.getShops()
        shop_nums = shop_owners[shop_owner_num].getShopNums()
        window.comboBox.clear()
        window.comboBox.addItem("가게 선택")
        window.scrollArea_4.setWidget(QWidget())
        
        for i in range(len(shop_nums)):
            window.comboBox.addItem(shops[shop_nums[i]].getName())
        window.comboBox.model().item(0).setEnabled(False)
        try:
            window.okButton_5.clicked.disconnect()
        except TypeError:
            pass
        window.okButton_5.clicked.connect(lambda: window.staff_info_page(shop_nums))
        
    def showStaffInfoPage(self, window, shop_nums):
        shop_staffs = Server.getShopStaffs()
        selected_shop_index = window.comboBox.currentIndex() - 1
        if selected_shop_index < 0:
            return
        
        shop_num = shop_nums[window.comboBox.currentIndex() - 1]
        
        staff_nums = list(map(int,os.listdir(f"db\\shops\\{shop_num}")))
        
        layout = QVBoxLayout()
        for i in range(len(staff_nums)):
            item_widget = QWidget()
            item_layout = QHBoxLayout()
            
            label1 = QLabel(shop_staffs[staff_nums[i]].getName())
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
            
            button1.clicked.connect(lambda checked, i=i: window.staff_mod_page(shop_num,staff_nums[i]))
            button2.clicked.connect(lambda checked, i=i: self.delstaff(window,shop_num,staff_nums[i]))
            
            item_layout.addWidget(label1)
            item_layout.addWidget(label2)
            item_layout.addWidget(button1)
            item_layout.addWidget(button2)
            item_widget.setLayout(item_layout)
            item_widget.setFixedHeight(30)
            layout.addWidget(item_widget)
        button = QPushButton("추가")
        button.setFixedHeight(30)
        button.clicked.connect(lambda : window.staff_add_page(shop_num))
        
        layout.addWidget(button)
        layout.addStretch(1)
        
        content_widget = QWidget()
        content_widget.setLayout(layout)
        window.scrollArea_4.setWidget(content_widget)
         
    def showStaffModPage(self,window,shop_num,staff_num):
        shops = Server.getShops()
        shop_staffs = Server.getShopStaffs()
        window.stackedWidget.setCurrentIndex(8)
        window.label_5.setText(shops[shop_num].getName())
        window.label_6.setText(shop_staffs[staff_num].getName())
        
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
        
        window.scrollArea_5.setWidget(content_widget)
        
        
        try:
            window.okButton_3.clicked.disconnect()
        except TypeError:
            pass
        window.okButton_3.clicked.connect(lambda : window.staff_page())

        def addProcedure():
            name = line.text()
            time = spin1.value()*2 + spin2.value()//30
            if time == 0 or time>48:
                QMessageBox.about(window,' ','시간이 잘못 입력되었습니다')
            elif Server.addProcedureToStaff(My_Structs.Procedure(name,time),shop_num,staff_num):
                window.staff_mod_page(shop_num,staff_num)
            else:
                QMessageBox.about(window,' ','중복된 시술 이름입니다')
                
        def delProcedure(procedure_num):
            buttonReply = QMessageBox.information(window,' ','직원의 모든 예약들이 삭제됩니다\n수정하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
    
            if buttonReply == QMessageBox.Yes:
                Server.delProcedureToStaff(procedure_num, shop_num, staff_num)
                window.staff_mod_page(shop_num,staff_num)
            
            
            
    def showStaffAddPage(self,window,shop_num):
        shops = Server.getShops()
        window.stackedWidget.setCurrentIndex(9)
        window.label_8.setText(shops[shop_num].getName())
        try:
            window.okButton_4.clicked.disconnect()
        except TypeError:
            pass
        window.okButton_4.clicked.connect(lambda : self.addStaff(window,shop_num))
        try:
            window.cancelButton_3.clicked.disconnect()
        except TypeError:
            pass
        window.cancelButton_3.clicked.connect(lambda : window.staff_page())
            
    def delstaff(self,window,shop_num, staff_num):
        buttonReply = QMessageBox.information(window,' ','직원의 모든 예약들이 삭제됩니다\n삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
    
        if buttonReply == QMessageBox.Yes:
            Server.delStaffToShop(shop_num,staff_num)
            window.staff_page()
            
    def addStaff(self,window, shop_num):
        staff_num = int(window.lineEdit_10.text())
        result = Server.addStaffToShop(shop_num, staff_num)
        if result == 1:
            QMessageBox.about(window,' ','직원이 등록되었습니다')
            window.staff_page()
        elif result == -1:
            QMessageBox.about(window,' ','이미 가게에 등록된 회원입니다')
        else:
            QMessageBox.about(window,' ','유효하지않은 회원번호입니다')
    