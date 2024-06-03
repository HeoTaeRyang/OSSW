import Server
import My_Structs

class Registration:
    def __init__(self, ID, PW, name, tel, classification):
        self.ID = ID
        self.PW = PW
        self.name = name
        self.tel = tel
        self.classification = classification
        
    def checkID(self):
        if self.classification == 0:
            for i in range(len(Server.shop_owners)):
                if Server.shop_owners[i].getID() == self.ID:
                    return False
        if self.classification == 1:
            for i in range(len(Server.shop_staffs)):
                if Server.shop_staffs[i].getID() == self.ID:
                    return False
        if self.classification == 2:
            for i in range(len(Server.customers)):
                if Server.customers[i].getID() == self.ID:
                    return False
        return True

    def checkPW(self):
        if len(self.PW) < 8:
            return False
        return True
    
    def checkTel(self):
        tmp = self.tel.split('-')
        if len(tmp[0]) != 3 or not tmp[0].isdigit():
            return False
        if (len(tmp[1]) != 3 and len(tmp[1]) != 4) or not tmp[1].isdigit():
            return False
        if len(tmp[2]) != 4 or not tmp[2].isdigit():
            return False
        return True
        
    def addMember(self):
        if self.classification == 0:
            Server.addShopOwner(My_Structs.ShopOwner(self.ID, self.PW, self.name, self.tel,len(Server.shop_owners),[]))
        if self.classification == 1:
            Server.addShopStaff(My_Structs.ShopStaff(self.ID, self.PW, self.name, self.tel,len(Server.shop_staffs),-1))
        if self.classification == 2:
            Server.addCustomer(My_Structs.Member(self.ID, self.PW, self.name, self.tel,len(Server.customers)))