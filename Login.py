import Server

class Login:
    def __init__(self, ID, PW, classification):
        self.ID = ID
        self.PW = PW
        self.classification = classification
    def getMember(self):
        if self.classification == 0:
            for i in range(len(Server.shop_owners)):
                if Server.shop_owners[i].getID() == self.ID:
                    if Server.shop_owners[i].getPW() == self.PW:
                        return Server.shop_owners[i].getNum()
                    else:
                        return -1
            return -2
        if self.classification == 1:
            for i in range(len(Server.shop_staffs)):
                if Server.shop_staffs[i].getID() == self.ID:
                    if Server.shop_staffs[i].getPW() == self.PW:
                        return Server.shop_staffs[i].getNum()
                    else:
                        return -1
            return -2
        if self.classification == 2:
            for i in range(len(Server.customers)):
                if Server.customers[i].getID() == self.ID:
                    if Server.customers[i].getPW() == self.PW:
                        return Server.customers[i].getNum()
                    else:
                        return -1
            return -2