from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import My_Structs
import Server
import datetime
import Main

class ShopInfo():
    def setWindow(self,window):
        window.setupUi(window)
        window.mainButton.clicked.connect(lambda: window.main_page())
        window.shopButton.clicked.connect(lambda: window.shop_page(Main.num))
        window.staffButton.clicked.connect(lambda: window.staff_page(Main.num))
        window.reservationButton.clicked.connect(lambda: window.reservation_page())
        window.profileButton.clicked.connect(lambda: window.profile_page())
        window.setFixedSize(600, 400)
    
    def selectWindowShopOwner(self,window,num):
        l = ["white","white","white","white","white"]
        l[num] = "grey"
        window.mainButton.setStyleSheet(f"background-color: {l[0]}")
        window.shopButton.setStyleSheet(f"background-color: {l[1]}")
        window.staffButton.setStyleSheet(f"background-color: {l[2]}")
        window.reservationButton.setStyleSheet(f"background-color: {l[3]}")
        window.profileButton.setStyleSheet(f"background-color: {l[4]}")
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
        
    def showMainShopInfoPage(self,window,shop_num):
        shops = Server.getShops()
        window.name.setText(shops[shop_num].getName())
        window.address.setText(shops[shop_num].getAddress())
        window.backButton.clicked.connect(lambda: window.main_page())
        window.operation_hours.setText(self.getShopOperationHours(shops[shop_num].getOperationHours()))
        window.tel.setText(shops[shop_num].getTel())
    
    def getShopOperationHours(self,operation_hours):
        for i in range(len(Server.shops)):
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
        
        
        
        
        
        
        
        
        
        
        
        
        
    #아직 미사용   
    def checkReservationAvailableTime(self,shop_num, staff_num, date, procedure_num):
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
        
    def reservation(self, shop_num, staff_num, date,  procedure_num, start_time, customer_num):
        procedures = Server.getProcedures(shop_num, staff_num)
        reservation = My_Structs.Reservation(start_time, procedures[procedure_num], customer_num)
        Server.addReservation(shop_num, staff_num, date,  reservation, start_time)