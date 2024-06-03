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