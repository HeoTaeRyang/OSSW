from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import My_Structs
import Server
import datetime
import Main
import os

class ShopInfo():
    def setWindow(self,window,classification):
        if classification == 0:
            window.setupUi(window)
            window.mainButton.clicked.connect(lambda: window.main_page())
            window.shopButton.clicked.connect(lambda: window.shop_page())
            window.staffButton.clicked.connect(lambda: window.staff_page())
            window.reservationButton.clicked.connect(lambda: window.reservation_page())
            window.profileButton.clicked.connect(lambda: window.profile_page())
            window.setFixedSize(600, 400)
            window.main_page()
        elif classification == 1:
            window.setupUi(window)
            window.mainButton.clicked.connect(lambda: window.main_page())
            window.reservationButton.clicked.connect(lambda: window.reservation_page())
            window.scheduleButton.clicked.connect(lambda: window.schedule_page())
            window.profileButton.clicked.connect(lambda: window.profile_page())
            window.setFixedSize(600, 400)
            window.main_page()
        else:
            window.setupUi(window)
            window.mainButton.clicked.connect(lambda: window.main_page())
            window.reservationButton.clicked.connect(lambda: window.reservation_page())
            window.profileButton.clicked.connect(lambda: window.profile_page())
            window.setFixedSize(600, 400)
            window.main_page()
    
    def selectWindow(self,window,num,classification):
        if classification == 0:
            l = ["white","white","white","white","white"]
            l[num] = "grey"
            window.mainButton.setStyleSheet(f"background-color: {l[0]}")
            window.shopButton.setStyleSheet(f"background-color: {l[1]}")
            window.staffButton.setStyleSheet(f"background-color: {l[2]}")
            window.reservationButton.setStyleSheet(f"background-color: {l[3]}")
            window.profileButton.setStyleSheet(f"background-color: {l[4]}")
            window.stackedWidget.setCurrentIndex(num)
        elif classification == 1:
            l = ["white","white","white","white"]
            l[num] = "grey"
            window.mainButton.setStyleSheet(f"background-color: {l[0]}")
            window.reservationButton.setStyleSheet(f"background-color: {l[1]}")
            window.scheduleButton.setStyleSheet(f"background-color: {l[2]}")
            window.profileButton.setStyleSheet(f"background-color: {l[3]}")
            window.stackedWidget.setCurrentIndex(num)
        else:
            l = ["white","white","white"]
            l[num] = "grey"
            window.mainButton.setStyleSheet(f"background-color: {l[0]}")
            window.reservationButton.setStyleSheet(f"background-color: {l[1]}")
            window.profileButton.setStyleSheet(f"background-color: {l[2]}")
            window.stackedWidget.setCurrentIndex(num)
        
    def showMainPage(self,window):
        layout = QVBoxLayout()
        shops = Server.getShops()
        for i in range(len(shops)):
            if shops[i].getNum() != -1:
                button = QPushButton(shops[i].getName())
                button.clicked.connect(lambda checked, i=i: window.main_shop_info_page(i))
                button.setFixedHeight(30)
                layout.addWidget(button)
        layout.addStretch(1)
        content_widget = QWidget()
        content_widget.setLayout(layout)
        window.scrollArea.setWidget(content_widget)
        
    def showMainShopInfoPage(self,window,shop_num,classification):
        if classification == 0:
            window.stackedWidget.setCurrentIndex(5)
        elif classification == 1:
            window.stackedWidget.setCurrentIndex(4)
        else:
            window.stackedWidget.setCurrentIndex(3)
        shops = Server.getShops()
        window.name.setText(shops[shop_num].getName())
        window.address.setText(shops[shop_num].getAddress())
        try:
            window.backButton.clicked.disconnect()
        except TypeError:
            pass
        window.backButton.clicked.connect(lambda: window.main_page())
        window.operation_hours.setText(self.getShopOperationHours(shops[shop_num].getOperationHours()))
        window.tel.setText(shops[shop_num].getTel())
        if classification == 2:
            try:
                window.reservationButton_2.clicked.disconnect()
            except TypeError:
                pass
            window.reservationButton_2.clicked.connect(lambda: window.main_reservation_page(shop_num))
            
    def showMainReservationPage(self,window,shop_num):
        window.stackedWidget.setCurrentIndex(4)
        shops = Server.getShops()
        shop_staffs = Server.getShopStaffs()
        window.label.setText(shops[shop_num].getName())
        staff_nums = list(map(int,os.listdir(f"db\\shops\\{shop_num}")))
        window.comboBox.setEnabled(True)
        window.pushButton_4.setEnabled(True)
        window.comboBox_2.setEnabled(False)
        window.dateEdit.setEnabled(False)
        window.comboBox_3.setEnabled(False)
        window.pushButton_5.setEnabled(False)
        window.pushButton_3.setEnabled(False)
        window.pushButton_7.setEnabled(False)
        window.comboBox.clear()
        window.comboBox_2.clear()
        window.comboBox_3.clear()
        
        try:
            window.pushButton_6.clicked.disconnect()
        except TypeError:
            pass    
        window.pushButton_6.clicked.connect(lambda:window.main_shop_info_page(shop_num))
        if not staff_nums:
            window.main_shop_info_page(shop_num)
            QMessageBox.about(window,' ','직원이 없는 가게입니다')
            return
        for i in range(len(staff_nums)):
            window.comboBox.addItem(shop_staffs[staff_nums[i]].getName())
        try:
            window.pushButton_4.clicked.disconnect()
        except TypeError:
            pass    
        window.pushButton_4.clicked.connect(lambda:staff_ok())
        
        def staff_ok():
            procedures = Server.getProcedures(shop_num, staff_nums[window.comboBox.currentIndex()])
            
            if not procedures:
                QMessageBox.about(window,' ','가능한 시술이 없는 직원입니다')
                return
            
            window.comboBox.setEnabled(False)
            window.pushButton_4.setEnabled(False)
            window.comboBox_2.setEnabled(True)
            window.pushButton_5.setEnabled(True)
            for i in range(len(procedures)):
                window.comboBox_2.addItem(procedures[i].getName())
            try:
                window.pushButton_5.clicked.disconnect()
            except TypeError:
                pass    
            window.pushButton_5.clicked.connect(lambda: procedure_ok())
        
        def procedure_ok():
            window.comboBox_2.setEnabled(False)
            window.pushButton_5.setEnabled(False)
            window.dateEdit.setEnabled(True)
            window.pushButton_3.setEnabled(True)
            try:
                window.pushButton_3.clicked.disconnect()
            except TypeError:
                pass    
            window.pushButton_3.clicked.connect(lambda: date_ok())
        
        def date_ok():
            date = window.dateEdit.date().toString(Qt.ISODate)
            
            available_times = checkReservationAvailableTime(shop_num, staff_nums[window.comboBox.currentIndex()] , date, window.comboBox_2.currentIndex())
            
            if not available_times:
                QMessageBox.about(window,' ','시술 가능한 시간이 없는 날짜입니다')
                return
            
            window.dateEdit.setEnabled(False)
            window.pushButton_3.setEnabled(False)
            window.comboBox_3.setEnabled(True)
            window.pushButton_7.setEnabled(True)
            for i in range(len(available_times)):
                window.comboBox_3.addItem(str(available_times[i]//2) + ":" + str(available_times[i]%2*30).zfill(2))
            try:
                window.pushButton_7.clicked.disconnect()
            except TypeError:
                pass    
            window.pushButton_7.clicked.connect(lambda: reservation(available_times))
                
                
        def checkReservationAvailableTime(shop_num, staff_num, date, procedure_num):
            available_times = []
            tmp_reservations_and_schedules = Server.getReservationsAndSchedules(shop_num, staff_num, date)
            tmp_date_l = list(map(int, date.split('-')))
            week = datetime.datetime(year=tmp_date_l[0], month=tmp_date_l[1],day = tmp_date_l[2]).weekday()
            operation_hours = Server.shops[shop_num].getOperationHours()
            open_time = operation_hours[week*2]
            close_time = operation_hours[week*2+1]
            procedures = Server.getProcedures(shop_num, staff_num)
            procedure_time = procedures[procedure_num].getTime()
            if open_time == -1:
                return available_times
            i = 0
            now = open_time
            while (now + procedure_time) <= close_time and i < len(tmp_reservations_and_schedules):
                if (now + procedure_time) <= tmp_reservations_and_schedules[i].getStartTime():
                    available_times.append(now)
                    now += 1
                else:
                    now = tmp_reservations_and_schedules[i].getStartTime() + tmp_reservations_and_schedules[i].getTime()
                    i += 1
            for j in range(now, close_time-procedure_time + 1):
                available_times.append(j)
            return available_times
            
        def reservation(available_times):
            if window.comboBox_3.currentIndex() < 0:
                QMessageBox.about(window,' ','시간을 선택하세요')
                return
            customer_num = Main.num
            start_time = available_times[window.comboBox_3.currentIndex()]
            procedures = Server.getProcedures(shop_num, staff_nums[window.comboBox.currentIndex()])
            reservation = My_Structs.Reservation(start_time, procedures[ window.comboBox_2.currentIndex()], customer_num)
            Server.addReservation(shop_num, staff_nums[window.comboBox.currentIndex()], window.dateEdit.date().toString(Qt.ISODate), reservation, start_time , Main.num)
            QMessageBox.about(window,' ','예약 되었습니다')
            window.main_shop_info_page(shop_num)
    
    def getShopOperationHours(self,operation_hours):
        operation_hours_s = ""
        if operation_hours[0] != -1:
            operation_hours_s += "월 " + str(operation_hours[0]*30//60).zfill(2) + ":" + str(operation_hours[0]*30%60).zfill(2) + " ~ " + str(operation_hours[1]*30//60).zfill(2) + ":" + str(operation_hours[1]*30%60).zfill(2)
        else:
            operation_hours_s += "월 휴무"
        operation_hours_s += "\n"
        if operation_hours[2] != -1:
            operation_hours_s += "화 " + str(operation_hours[2]*30//60).zfill(2) + ":" + str(operation_hours[2]*30%60).zfill(2) + " ~ " + str(operation_hours[3]*30//60).zfill(2) + ":" + str(operation_hours[3]*30%60).zfill(2)
        else:
            operation_hours_s += "화 휴무"
        operation_hours_s += "\n"
        if operation_hours[4] != -1:
            operation_hours_s += "수 " + str(operation_hours[4]*30//60).zfill(2) + ":" + str(operation_hours[4]*30%60).zfill(2) + " ~ " + str(operation_hours[5]*30//60).zfill(2) + ":" + str(operation_hours[5]*30%60).zfill(2)
        else:
            operation_hours_s += "수 휴무"
        operation_hours_s += "\n"
        if operation_hours[6] != -1:
            operation_hours_s += "목 " + str(operation_hours[6]*30//60).zfill(2) + ":" + str(operation_hours[6]*30%60).zfill(2) + " ~ " + str(operation_hours[7]*30//60).zfill(2) + ":" + str(operation_hours[7]*30%60).zfill(2)
        else:
            operation_hours_s += "목 휴무"
        operation_hours_s += "\n"
        if operation_hours[8] != -1:
            operation_hours_s += "금 " + str(operation_hours[8]*30//60).zfill(2) + ":" + str(operation_hours[8]*30%60).zfill(2) + " ~ " + str(operation_hours[9]*30//60).zfill(2) + ":" + str(operation_hours[9]*30%60).zfill(2)
        else:
            operation_hours_s += "금 휴무"
        operation_hours_s += "\n"
        if operation_hours[10] != -1:
            operation_hours_s += "토 " + str(operation_hours[10]*30//60).zfill(2) + ":" + str(operation_hours[10]*30%60).zfill(2) + " ~ " + str(operation_hours[11]*30//60).zfill(2) + ":" + str(operation_hours[11]*30%60).zfill(2)
        else:
            operation_hours_s += "토 휴무"
        operation_hours_s += "\n"
        if operation_hours[12] != -1:
            operation_hours_s += "일 " + str(operation_hours[12]*30//60).zfill(2) + ":" + str(operation_hours[12]*30%60).zfill(2) + " ~ " + str(operation_hours[13]*30//60).zfill(2) + ":" + str(operation_hours[13]*30%60).zfill(2)
        else:
            operation_hours_s += "일 휴무"
        return operation_hours_s