from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Server
import Main
import os
import datetime

class ReservationManagement:
    def showReservationPage(self,window,classification):
        num = Main.num
        if classification == 0:
            member = Server.getShopOwners()
            window.comboBox_5.clear()
            shop_nums = member[num].getShopNums()
            shops = Server.getShops()
            for i in range(len(shop_nums)):
                window.comboBox_5.addItem(shops[shop_nums[i]].getName())
                
            try:
                window.pushButton_7.clicked.disconnect()
            except TypeError:
                pass
            window.pushButton_7.clicked.connect(lambda: window.reservation_info_page())
        elif classification == 1:
            member = Server.getShopStaffs()
            window.label.setText(member[num].getName())
            try:
                window.pushButton_7.clicked.disconnect()
            except TypeError:
                pass
            window.pushButton_7.clicked.connect(lambda : window.reservation_info_page())
            window.reservation_info_page()
            
        else:
            member = Server.getCustomers()
            window.label_9.setText(member[num].getName())
            
            try:
                window.okButton_5.clicked.disconnect()
            except TypeError:
                pass
            
            window.okButton_5.clicked.connect(lambda : window.reservation_info_page())
            window.reservation_info_page()
    
    def showReservationInfoPage(self,window, classification):
        if classification == 0:
            if window.comboBox_5.currentIndex() < 0:
                return
            shop_owners = Server.getShopOwners()
            shops = Server.getShops()
            shop_staffs = Server.getShopStaffs()
            customers = Server.getCustomers()
            shop_nums = shop_owners[Main.num].getShopNums()
            shop_num = shop_nums[window.comboBox_5.currentIndex()]
            date = window.dateEdit.date().toString(Qt.ISODate)
            staff_nums = list(map(int,os.listdir(f"db\\shops\\{shop_num}")))
            staff_reservations_and_schedules = []
            for i in range(len(staff_nums)):
                staff_reservations_and_schedules.append(Server.getReservationsAndSchedules(shop_num, staff_nums[i], date))
            tmp_date_l = list(map(int,date.split("-")))
            week = datetime.datetime(year=tmp_date_l[0], month=tmp_date_l[1],day = tmp_date_l[2]).weekday()
            operation_hours = shops[shop_num].getOperationHours()
            open_time = operation_hours[week*2]
            close_time = operation_hours[week*2+1]
            time = close_time - open_time
            
            horizontal_headers = []
            for i in staff_nums:
                horizontal_headers.append(shop_staffs[i].getName())
            
            vertical_headers = []
            for i in range(open_time,close_time):
                vertical_headers.append(f"{str(i//2)}:{str(i%2*30).zfill(2)}")
            
            window.tableWidget.setColumnCount(len(staff_reservations_and_schedules))
            window.tableWidget.setRowCount(time)
            window.tableWidget.setHorizontalHeaderLabels(horizontal_headers)
            window.tableWidget.setVerticalHeaderLabels(vertical_headers)
            
            j = open_time
            cnt = 0
            for i in range(len(staff_reservations_and_schedules)):
                while(j != close_time):
                    if cnt >= len(staff_reservations_and_schedules[i]):
                        break
                    elif staff_reservations_and_schedules[i][cnt].getStartTime() == j:
                        time = staff_reservations_and_schedules[i][cnt].getTime()
                        if staff_reservations_and_schedules[i][cnt].type() == 0:
                            s = staff_reservations_and_schedules[i][cnt].getContent() + "\n" + f"({customers[staff_reservations_and_schedules[i][cnt].getReservationPersonNum()].getName()})"
                            window.tableWidget.setItem(j,i, QTableWidgetItem(s))
                            window.tableWidget.item(j, i).setBackground(Qt.red)
                        else:
                            window.tableWidget.setItem(j,i, QTableWidgetItem("일정"))
                            window.tableWidget.item(j, i).setBackground(Qt.blue)
                        window.tableWidget.item(j, i).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                        window.tableWidget.setSpan(j,i,time,1)
                        cnt += 1
                        j += time-1
                    else:
                        pass
                    j+= 1
        elif classification == 1:
            shop_staffs = Server.getShopStaffs()
            customers = Server.getCustomers()
            num = Main.num
            shop_num = shop_staffs[num].getShopNum()
            if shop_num == -1:
                return
            date = window.dateEdit.date().toString(Qt.ISODate)
            reservations_and_schedules = Server.getReservationsAndSchedules(shop_num, num, date)
            shops =Server.getShops()
            tmp_date_l = list(map(int,date.split("-")))
            week = datetime.datetime(year=tmp_date_l[0], month=tmp_date_l[1],day = tmp_date_l[2]).weekday()
            operation_hours = shops[shop_num].getOperationHours()
            open_time = operation_hours[week*2]
            close_time = operation_hours[week*2+1]
            time = close_time - open_time
            
            horizontal_headers = [shop_staffs[num].getName(),'']
            
            vertical_headers = []
            for i in range(open_time,close_time):
                vertical_headers.append(f"{str(i//2)}:{str(i%2*30).zfill(2)}")
                
            window.tableWidget.setColumnCount(0)
            window.tableWidget.setRowCount(0)
                
            window.tableWidget.setColumnCount(2)
            window.tableWidget.setRowCount(time)
            window.tableWidget.setHorizontalHeaderLabels(horizontal_headers)
            window.tableWidget.setVerticalHeaderLabels(vertical_headers)
            
            i = open_time
            cnt = 0
            n = -1
            while(i != close_time):
                if cnt >= len(reservations_and_schedules):
                    break
                elif reservations_and_schedules[cnt].getStartTime() == i:
                    time = reservations_and_schedules[cnt].getTime()
                    if reservations_and_schedules[cnt].type() == 0:
                        n += 1
                        s = reservations_and_schedules[cnt].getContent() + "\n" + f"({customers[reservations_and_schedules[cnt].getReservationPersonNum()].getName()})"
                        window.tableWidget.setItem(i,0, QTableWidgetItem(s))
                        window.tableWidget.item(i, 0).setBackground(Qt.red)
                        del_button = QPushButton("삭제")
                        del_button.clicked.connect(lambda checked, i=i, n=n: self.delReservation(window, date, shop_num,num, i, n))
                        window.tableWidget.setCellWidget(i,1,del_button)
                    else:
                        s = reservations_and_schedules[cnt].getContent()
                        window.tableWidget.setItem(i,0, QTableWidgetItem(s))
                        window.tableWidget.item(i, 0).setBackground(Qt.blue)
                    window.tableWidget.item(i, 0).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                    window.tableWidget.setSpan(i,0,time,1)
                    cnt += 1
                    i += time-1
                else:
                    pass
                i+= 1
        else:
            date = window.dateEdit_2.date().toString(Qt.ISODate)
            customers = Server.getCustomers()
            customer = customers[Main.num]
            reservations = customer.getReservations()
            checked_reservations = []
            for i in range(len(reservations)):
                if reservations[i][0] == date:
                    checked_reservations.append(reservations[i])
            
            shops = Server.getShops()
            shop_staffs = Server.getShopStaffs()
            layout = QVBoxLayout()
            
            if not checked_reservations:
                window.scrollArea_3.setWidget(QWidget())
                return
                
            for i in range(len(checked_reservations)):
                item_widget = QWidget()
                item_layout = QHBoxLayout()
                reservation = checked_reservations[i][3]
                start_time = reservation.getStartTime()
                end_time = reservation.getStartTime() + reservation.getTime()
                start_time_s = str(start_time//2) + ":" + str(start_time%2*30).zfill(2)
                end_time_s = str(end_time//2) + ":" + str(end_time%2*30).zfill(2)
                label = QLabel(checked_reservations[i][0] + " / " + shops[checked_reservations[i][1]].getName() + " / " + shop_staffs[checked_reservations[i][2]].getName() + " / " + start_time_s + "~" + end_time_s + " / " + reservation.getContent())
                button = QPushButton("삭제")
                label.setFixedHeight(20)
                button.setFixedSize(50,20)
                for j in range(len(reservations)):
                    if reservations[j][1] == checked_reservations[i][1] and reservations[j][2] == checked_reservations[i][2] and reservations[j][3].getStartTime() == checked_reservations[i][3].getStartTime():
                        reservation_num = j
                button.clicked.connect(lambda checked, i=i: self.delReservation(window, date, checked_reservations[i][1], checked_reservations[i][2], checked_reservations[i][3].getStartTime(),reservation_num))
                item_layout.addWidget(label)
                item_layout.addWidget(button)
                item_widget.setLayout(item_layout)
                item_widget.setFixedHeight(30)
                layout.addWidget(item_widget)
            layout.addStretch(1)
            content_widget = QWidget()
            content_widget.setLayout(layout)
            window.scrollArea_3.setWidget(content_widget)
            
    def delReservation(self,window, date, shop_num,shop_staff_num,start_time, reservation_num):
        buttonReply = QMessageBox.information(window,' ','삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
    
        if buttonReply == QMessageBox.Yes:
            Server.delReservation(date, shop_num, shop_staff_num, start_time, reservation_num)
            window.reservation_info_page()