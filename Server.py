import pickle
import os
import shutil

with open("db\\members\\shop_owners.pickle","rb") as fr:
    shop_owners = pickle.load(fr)

with open("db\\members\\shop_staffs.pickle","rb") as fr:
    shop_staffs = pickle.load(fr)

with open("db\\members\\customers.pickle","rb") as fr:
    customers = pickle.load(fr)

with open("db\\shops.pickle","rb") as fr:
    shops = pickle.load(fr)

def addShopOwner(shop_owner):
    shop_owners.append(shop_owner)
    with open("db\\members\\shop_owners.pickle","wb") as fw:
        pickle.dump(shop_owners,fw)
        
def addShopStaff(shop_staff):
    shop_staffs.append(shop_staff)
    with open("db\\members\\shop_staffs.pickle","wb") as fw:
        pickle.dump(shop_staffs,fw)
    
def addCustomer(customer):
    customers.append(customer)
    with open("db\\members\\customers.pickle","wb") as fw:
        pickle.dump(customers,fw)
    
def addShop(shop):
    if shop.getNum < len(shops):
        shops[shop.getNum] = shop
    else:
        shops.append(shop)
    os.mkdir(f"shops\\{shop.getNum}")
    
    
def delShop(shop_num):
    shops[shop_num].num = -1
    with open("db\\shops.pickle","wb") as fw:
        pickle.dump(customers,fw)
    for i in range(len(shop_staffs)):
        if shop_staffs[i].getShopNum == shop_num:
            shop_staffs[i].num = -1
    with open("db\\members\\shop_staffs.pickle","wb") as fw:
        pickle.dump(shop_staffs,fw)
    shutil.rmtree(f'db\\shops\\{shop_num}')
    
    
# def addStaffToShop():
# def addProcedureToStaff():
# def addReservation():
# def addSchedule():
# def delReservation():
# def delSchedule():
def getReservations(shop_num, staff_num, date):
    with open(f"db\\shops\\{shop_num}\\{staff_num}\\{date}.pickle","rb") as fr:
        return pickle.load(fr)
# def getSchedules():