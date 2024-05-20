class Member:
    def __init__(self, ID, PW, name, tel, classification, num):
        self.ID = ID
        self.PW = PW
        self.name = name
        self.tel = tel
        self.classification = classification
        self.num = num
    
    def getID(self):
        return self.ID
    
    def getPW(self):
        return self.PW
    
    def getName(self):
        return self.name
    
    def getTel(self):
        return self.tel
    
    def getClassification(self):
        return self.classification
    
    def getNum(self):
        return self.num