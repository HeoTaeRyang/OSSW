from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Server
import Main
import My_Structs

class ShopManagement:
    def showShopPage(self,window):
        shop_owner_num = Main.num
        layout = QVBoxLayout()
        shop_owners = Server.getShopOwners()
        shops = Server.getShops()
        shop_nums = shop_owners[shop_owner_num].getShopNums()
        for i in range(len(shop_nums)):
            item_widget = QWidget()
            item_layout = QHBoxLayout()
            
            label = QLabel(shops[shop_nums[i]].getName())
            button1 = QPushButton("수정")
            button2 = QPushButton("삭제")
            label.setFixedHeight(20)
            button1.setFixedSize(50,20)
            button2.setFixedSize(50,20)
            
            button1.clicked.connect(lambda checked, i=i: window.shop_mod_page(shop_nums[i]))
            button2.clicked.connect(lambda checked, i=i: self.delete(window,shop_nums[i]))
            
            item_layout.addWidget(label)
            item_layout.addWidget(button1)
            item_layout.addWidget(button2)
            item_widget.setLayout(item_layout)
            item_widget.setFixedHeight(30)
            layout.addWidget(item_widget)
        button = QPushButton("추가")
        button.setFixedHeight(30)
        button.clicked.connect(lambda : window.shop_add_page())
        
        content_widget = QWidget()
        content_widget.setLayout(layout)
        layout.addWidget(button)
        window.scrollArea_3.setWidget(content_widget)
        layout.addStretch(1)
    
    def showShopModPage(self,window,shop_num):
        window.stackedWidget.setCurrentIndex(6)
        shops = Server.getShops()
        try:
            window.cancelButton.clicked.disconnect()
        except TypeError:
            pass
        window.cancelButton.clicked.connect(lambda : window.shop_page())
        try:
            window.okButton.clicked.disconnect()
        except TypeError:
            pass
        window.okButton.clicked.connect(lambda : self.mod(window,shop_num))
        window.name_5.setText(shops[shop_num].getName())
        window.lineEdit.setText(shops[shop_num].getAddress())
        tel = list(shops[shop_num].getTel().split("-"))
        window.lineEdit_2.setText(tel[0])
        window.lineEdit_3.setText(tel[1])
        window.lineEdit_4.setText(tel[2])
        operation_hours = shops[shop_num].getOperationHours()
        
        for i in range(7):
            if operation_hours[i * 2] == -1:
                window.findChild(QSpinBox, f"spinBox_{i + 1}").setValue(0)
                window.findChild(QSpinBox, f"spinBox_{i + 8}").setValue(0)
                window.findChild(QSpinBox, f"spinBox_{i + 15}").setValue(0)
                window.findChild(QSpinBox, f"spinBox_{i + 22}").setValue(0)
                window.findChild(QCheckBox, f"checkBox_{i + 1}").setChecked(True)
            else:
                window.findChild(QSpinBox, f"spinBox_{i + 1}").setValue(operation_hours[i * 2] // 2)
                window.findChild(QSpinBox, f"spinBox_{i + 8}").setValue(operation_hours[i * 2] % 2 * 30)
                window.findChild(QSpinBox, f"spinBox_{i + 15}").setValue(operation_hours[i * 2 + 1] // 2)
                window.findChild(QSpinBox, f"spinBox_{i + 22}").setValue(operation_hours[i * 2 + 1] % 2 * 30)
    
    def showShopAddPage(self,window):
        window.stackedWidget.setCurrentIndex(7)
        window.lineEdit_5.setText("")
        window.lineEdit_6.setText("")
        window.lineEdit_7.setText("")
        window.lineEdit_8.setText("")
        window.lineEdit_9.setText("가게 이름")
        
        try:
            window.cancelButton_2.clicked.disconnect()
        except TypeError:
            pass
        window.cancelButton_2.clicked.connect(lambda: window.shop_page())
        
        try:
            window.okButton_2.clicked.disconnect()
        except TypeError:
            pass
        window.okButton_2.clicked.connect(lambda: self.add(window))
    
    def mod(self,window,shop_num):
        shops = Server.getShops()
        tel1 = window.lineEdit_2.text()
        tel2 = window.lineEdit_3.text()
        tel3 = window.lineEdit_4.text()
        if not self.checkTel(tel1,tel2,tel3):
            QMessageBox.about(window,' ','잘못된 전화번호입니다')
        else:
            address = window.lineEdit.text()
            tel = tel1 + '-' + tel2 + '-' + tel3
            operation_hours = []
            
            for i in range(7):
                if window.findChild(QCheckBox, f"checkBox_{i + 1}").isChecked():
                    operation_hours += [-1, -1]
                else:
                    start_value = window.findChild(QSpinBox, f"spinBox_{i + 1}").value() * 2 + window.findChild(QSpinBox, f"spinBox_{i + 8}").value() // 30
                    end_value = window.findChild(QSpinBox, f"spinBox_{i + 15}").value() * 2 + window.findChild(QSpinBox, f"spinBox_{i + 22}").value() // 30
                    operation_hours += [start_value, end_value]
              
            for i in range(7):
                if operation_hours[i*2] == operation_hours[i*2+1]:
                    operation_hours[i*2] = -1
                    operation_hours[i*2+1] = -1
            
            if self.checkOperationHours(operation_hours):   
                QMessageBox.about(window,' ','시간이 잘못 입력되었습니다')
            else:
                buttonReply = QMessageBox.information(window,' ','가게의 모든 예약들이 삭제됩니다\n수정하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        
                if buttonReply == QMessageBox.Yes:
                    Server.modShop(shop_num,My_Structs.Shop(shops[shop_num].getName(),address,tel,operation_hours,shop_num))
                    QMessageBox.about(window,' ','가게 수정이 완료되었습니다')
                    window.shop_page()   
                
                
                
    def delete(self,window,shop_num):
        buttonReply = QMessageBox.information(window,' ','가게에 등록된 모든 직원들과 예약들이 삭제됩니다\n삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        
        if buttonReply == QMessageBox.Yes:
            Server.delShop(shop_num,Main.num)
            window.shop_page()   
        
    def add(self,window):
        shops = Server.getShops()
        tel1 = window.lineEdit_8.text()
        tel2 = window.lineEdit_6.text()
        tel3 = window.lineEdit_5.text()
        if not self.checkTel(tel1,tel2,tel3):
            QMessageBox.about(window,' ','잘못된 전화번호입니다')
        else:
            name = window.lineEdit_9.text()
            address = window.lineEdit_7.text()
            tel = tel1 + '-' + tel2 + '-' + tel3
            operation_hours = []
            
            for i in range(7):
                if window.findChild(QCheckBox, f"checkBox_{i + 8}").isChecked():
                    operation_hours += [-1,-1]
                else:  
                    operation_hours += [window.findChild(QSpinBox, f"spinBox_{i + 200}").value()*2 + window.findChild(QSpinBox, f"spinBox_{i + 207}").value()//30, window.findChild(QSpinBox, f"spinBox_{i + 214}").value()*2 + window.findChild(QSpinBox, f"spinBox_{i + 221}").value()//30]
            
            for i in range(7):
                if operation_hours[i*2] == operation_hours[i*2+1]:
                    operation_hours[i*2] = -1
                    operation_hours[i*2+1] = -1
            
            shop_num = -1
            for i in range(len(shops)):
                if shops[i].getNum() == -1:
                    shop_num = i
                    break
            if shop_num == -1:
                shop_num = len(shops)
                
            if self.checkOperationHours(operation_hours):   
                QMessageBox.about(window,' ','시간이 잘못 입력되었습니다')
            else:
                Server.addShop(Main.num,My_Structs.Shop(name,address,tel,operation_hours,shop_num))
                QMessageBox.about(window,' ','가게 생성이 완료되었습니다')
                window.shop_page() 
    
    def checkTel(self,tel1,tel2,tel3):
        if not tel1.isdigit() or not tel2.isdigit() or not tel3.isdigit():
            return False
        return True
        
    def checkOperationHours(self,operations_hours):
        for i in range(7):
            if operations_hours[i*2] > operations_hours[i*2+1] or operations_hours[i*2] > 48 or operations_hours[i*2+1] > 48 :
                return True
        return False
    
    
        
        