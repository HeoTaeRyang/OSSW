import My_Structs
import Server
import datetime

class ShopInfo():
    def showShopList(self):
        for i in range(len(Server.shops)):
            Server.shops[i].info()
        
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