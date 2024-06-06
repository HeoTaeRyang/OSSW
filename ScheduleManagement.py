from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Server
import Main
import datetime
import My_Structs

class ScheduleManagement:
    def showSchedulePage(self,window):
        member = Server.getShopStaffs()
        num = Main.num
        window.label_5.setText(member[num].getName())
        try:
            window.pushButton_8.clicked.disconnect()
        except TypeError:
            pass
        window.pushButton_8.clicked.connect(lambda : window.schedule_info_page())
        
        try:
            window.pushButton_3.clicked.disconnect()
        except TypeError:
            pass
        window.pushButton_3.clicked.connect(lambda : self.addSchedule(window))
        
        window.schedule_info_page()
    
    def showScheduleInfoPage(self,window):
        shop_staffs = Server.getShopStaffs()
        customers = Server.getCustomers()
        num = Main.num
        shop_num = shop_staffs[num].getShopNum()
        if shop_num == -1:
            return
        date = window.dateEdit_2.date().toString(Qt.ISODate)
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
            
        window.tableWidget_2.setColumnCount(0)
        window.tableWidget_2.setRowCount(0)
            
        window.tableWidget_2.setColumnCount(2)
        window.tableWidget_2.setRowCount(time)
        window.tableWidget_2.setHorizontalHeaderLabels(horizontal_headers)
        window.tableWidget_2.setVerticalHeaderLabels(vertical_headers)
        
        i = open_time
        cnt = 0
        while(i != close_time):
            if cnt >= len(reservations_and_schedules):
                break
            elif reservations_and_schedules[cnt].getStartTime() == i:
                time = reservations_and_schedules[cnt].getTime()
                if reservations_and_schedules[cnt].type() == 0:
                    s = reservations_and_schedules[cnt].getContent() + "\n" + f"({customers[reservations_and_schedules[cnt].getReservationPersonNum()].getName()})"
                    window.tableWidget_2.setItem(i,0, QTableWidgetItem(s))
                    window.tableWidget_2.item(i, 0).setBackground(Qt.red)
                else:
                    s = reservations_and_schedules[cnt].getContent()
                    window.tableWidget_2.setItem(i,0, QTableWidgetItem(s))
                    window.tableWidget_2.item(i, 0).setBackground(Qt.blue)
                    del_button = QPushButton("삭제")
                    del_button.clicked.connect(lambda checked, i=i: self.delSchedule(window, date, shop_num, i))
                    window.tableWidget_2.setCellWidget(i,1,del_button)
                window.tableWidget_2.item(i, 0).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                window.tableWidget_2.setSpan(i,0,time,1)
                cnt += 1
                i += time-1
            else:
                pass
            i+= 1
    
    def delSchedule(self,window, date, shop_num, start_time):
        buttonReply = QMessageBox.information(window,' ','삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
    
        if buttonReply == QMessageBox.Yes:
            Server.delSchedule(date, shop_num, Main.num, start_time)
            window.schedule_info_page()
    
    def addSchedule(self, window):
        num = Main.num
        shop_staffs = Server.getShopStaffs()
        shops = Server.getShops()
        shop_num = shop_staffs[num].getShopNum()
        date = window.dateEdit_2.date().toString(Qt.ISODate)
        start_time = window.spinBox.value()*2 + window.spinBox_2.value()//30
        end_time = window.spinBox_3.value()*2 + window.spinBox_4.value()//30
        time = end_time - start_time
        content = window.lineEdit.text()
        reservation_and_schedule = Server.getReservationsAndSchedules(shop_num,num,date)
        operation_hours = shops[shop_num].getOperationHours()
        tmp_date_l = list(map(int, date.split('-')))
        week = datetime.datetime(year=tmp_date_l[0], month=tmp_date_l[1],day = tmp_date_l[2]).weekday()
        open_time = operation_hours[week*2]
        close_time = operation_hours[week*2+1]
        
        if end_time <= start_time:
            QMessageBox.about(window,' ','시간이 잘못 입력되었습니다')
            return
        
        now = open_time
        for i in range(0,len(reservation_and_schedule)):
            if reservation_and_schedule[i].getStartTime() >= end_time and now <= start_time:
                break
            else:
                now = reservation_and_schedule[i].getStartTime() + reservation_and_schedule[i].getTime()
        if now != close_time:
            if now <= start_time and close_time >= end_time:
                pass
            else:
                QMessageBox.about(window,' ','이미 예약이나 일정이 있는 시간대입니다')
                return
        
        buttonReply = QMessageBox.information(window,' ',f'{date}\n{window.spinBox.value()}시 {window.spinBox_2.value()}분 ~ {window.spinBox_3.value()}시 {window.spinBox_4.value()}분\n{content}\n추가하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
    
        if buttonReply == QMessageBox.Yes:
            Server.addSchedule(shop_num, num, date,  My_Structs.Schedule(start_time,content,time), start_time)
            window.schedule_info_page()
        
        
        