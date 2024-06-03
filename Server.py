import pickle
import My_Structs

with open("db\members\shop_owners.pickle","rb") as fr:
    shop_owners = pickle.load(fr)

with open("db\members\shop_staffs.pickle","rb") as fr:
    shop_staffs = pickle.load(fr)

with open("db\members\customers.pickle","rb") as fr:
    customers = pickle.load(fr)

with open("db\shops.pickle","rb") as fr:
    shops = pickle.load(fr)

def addShopOwner(shop_owner):
    shop_owners.append(shop_owner)
    with open("db\members\shop_owners.pickle","wb") as fw:
        pickle.dump(shop_owners,fw)
        
def addShopStaff(shop_staff):
    shop_staffs.append(shop_staff)
    with open("db\members\shop_staffs.pickle","wb") as fw:
        pickle.dump(shop_staffs,fw)
    
def addCustomer(customer):
    customers.append(customer)
    with open("db\members\customers.pickle","wb") as fw:
        pickle.dump(customers,fw)
    
# def addShop(shop):
# def delShop():
# def addStaffToShop():
# def addProcedureToStaff():
# def addReservation():
# def addSchedule():
# def delReservation():
# def delSchedule():
# def getReservations():
# def getSchedules():