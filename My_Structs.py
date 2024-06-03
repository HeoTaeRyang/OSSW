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
    
    def info(self):
        print("ID",self.ID)
        print("PW",self.PW)
        print("이름",self.name)
        print("전화번호",self.tel)
        print("회원번호",self.num)
    
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

    def info(self):
        print("ID",self.ID)
        print("PW",self.PW)
        print("이름",self.name)
        print("전화번호",self.tel)
        print("회원번호",self.num)
        print("가게번호들",self.shop_nums)
    

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
    
    def info(self):
        print("ID",self.ID)
        print("PW",self.PW)
        print("이름",self.name)
        print("전화번호",self.tel)
        print("회원번호",self.num)
        print("가게번호",self.shop_num)
    
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
    
    def info(self):
        print("이름",self.name)
        print("주소",self.address)
        print("전화번호",self.tel)
        print("영업시간")
        if self.operation_hours[0] != -1:
            print("월",self.operation_hours[0]*30//60,":",self.operation_hours[0]*30%60,"~",self.operation_hours[1]*30//60,":",self.operation_hours[1]*30%60)
        else:
            print("월 휴무")
        if self.operation_hours[2] != -1:
            print("화",self.operation_hours[2]*30//60,":",self.operation_hours[2]*30%60,"~",self.operation_hours[3]*30//60,":",self.operation_hours[3]*30%60)
        else:
            print("화 휴무")
        if self.operation_hours[4] != -1:
            print("수",self.operation_hours[4]*30//60,":",self.operation_hours[4]*30%60,"~",self.operation_hours[5]*30//60,":",self.operation_hours[5]*30%60)
        else:
            print("수 휴무")
        if self.operation_hours[6] != -1:
            print("목",self.operation_hours[6]*30//60,":",self.operation_hours[6]*30%60,"~",self.operation_hours[7]*30//60,":",self.operation_hours[7]*30%60)
        else:
            print("목 휴무")
        if self.operation_hours[8] != -1:
            print("금",self.operation_hours[8]*30//60,":",self.operation_hours[8]*30%60,"~",self.operation_hours[9]*30//60,":",self.operation_hours[9]*30%60)
        else:
            print("금 휴무")
        if self.operation_hours[10] != -1:
            print("토",self.operation_hours[10]*30//60,":",self.operation_hours[10]*30%60,"~",self.operation_hours[11]*30//60,":",self.operation_hours[11]*30%60)
        else:
            print("토 휴무")
        if self.operation_hours[12] != -1:
            print("일",self.operation_hours[12]*30//60,":",self.operation_hours[12]*30%60,"~",self.operation_hours[13]*30//60,":",self.operation_hours[13]*30%60)
        else:
            print("일 휴무")
        print("가게번호",self.num)
        
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