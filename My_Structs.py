class Member:
    def __init__(self, ID, PW, name, tel, num):
        self.ID = ID
        self.PW = PW
        self.name = name
        self.tel = tel
        self.num = num
    
    def getID(self):
        return self.ID
    
    def getPW(self):
        return self.PW
    
    def getName(self):
        return self.name
    
    def getTel(self):
        return self.tel
    
    def getNum(self):
        return self.num
    
    def setPW(self,PW):
        self.PW = PW
        
    def setTel(self,tel):
        self.tel = tel
    
class ShopOwner(Member):
    def __init__(self, ID, PW, name, tel, num, shop_nums):
        self.ID = ID
        self.PW = PW
        self.name = name
        self.tel = tel
        self.num = num
        self.shop_nums = shop_nums
    
    def getShopNums(self):
        return self.shop_nums

class ShopStaff(Member):
    def __init__(self, ID, PW, name, tel, num, shop_num):
        self.ID = ID
        self.PW = PW
        self.name = name
        self.tel = tel
        self.num = num
        self.shop_num = shop_num

    def getShopNum(self):
        return self.shop_num
    
class Customer(Member):
    def __init__(self, ID, PW, name, tel, num, reservations):
        self.ID = ID
        self.PW = PW
        self.name = name
        self.tel = tel
        self.num = num
        self.reservations = reservations
        
    def getReservations(self):
        return self.reservations
    
    def addReservation(self,reservation):
        for i in range(len(self.reservations)):
            if self.reservations[i][0] > reservation[0]:
                self.reservations.insert(i,reservation)
                return    
            elif self.reservations[i][0] == reservation[0]:
                if self.reservations[i][3].getStartTime() > reservation[3].getStartTime():
                    self.reservations.insert(i,reservation)
                    return
        self.reservations.append(reservation)
        
    
    def delReservation(self,reservation_num):
        del self.reservations[reservation_num]
        
    
class Shop:
    def __init__(self, name, address, tel, operation_hours, num):
        self.name = name
        self.address = address
        self.operation_hours = operation_hours
        self.tel = tel
        self.num = num
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def getOperationHours(self):
        return self.operation_hours
    
    def getTel(self):
        return self.tel
    
    def getNum(self):
        return self.num
        
class Procedure:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        
    def getName(self):
        return self.name

    def getTime(self):
        return self.time
        
class Reservation:
    def __init__(self, start_time, procedure, reservation_person_num):
        self.start_time = start_time
        self.content = procedure.getName()
        self.time = procedure.getTime()
        self.reservation_person_num = reservation_person_num
    def getStartTime(self):
        return self.start_time
    def getContent(self):
        return self.content
    def getTime(self):
        return self.time
    def getReservationPersonNum(self):
        return self.reservation_person_num
    def type(self):
        return 0
        
class Schedule:
    def __init__(self, start_time, content, time):
        self.start_time = start_time
        self.content = content
        self.time = time
    def getStartTime(self):
        return self.start_time
    def getContent(self):
        return self.content
    def getTime(self):
        return self.time
    def type(self):
        return 1