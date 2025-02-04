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

def addShop(shop_owner_num,shop):
    if shop.getNum() < len(shops):
        shops[shop.getNum()] = shop
    else:
        shops.append(shop)
    os.mkdir(f"db\\shops\\{shop.getNum()}")
    with open("db\\shops.pickle","wb") as fw:
        pickle.dump(shops,fw)
    shop_num = shop.getNum()
    shop_nums = shop_owners[shop_owner_num].getShopNums()
    check = 0
    for i in range(len(shop_nums)):
        if shop_nums[i] > shop_num:
            shop_nums.insert(i,shop_num)
            check = 1
            break
    if check == 0:
        shop_nums.append(shop_num)
    shop_owners[shop_owner_num].shop_nums = shop_nums
    with open("db\\members\\shop_owners.pickle","wb") as fw:
        pickle.dump(shop_owners,fw)
    
def delShop(shop_num,shop_owner_num):
    staff_nums = list(map(int,os.listdir(f"db\\shops\\{shop_num}")))
    
    for i in range(len(staff_nums)):
        l = list(map(int,os.listdir(f"db\\shops\\{shop_num}\\{staff_nums[i]}")))
        l = l[:-1]
        for j in range(len(l)):
            with open(f"db\\shops\\{shop_num}\\{staff_nums[i]}\\{l[j]}","rb") as fr:
                reservations_and_shedules = pickle.load(fr)
            for k in range(len(reservations_and_shedules)):
                if reservations_and_shedules[k].type() == 0:
                    delReservation(l[j][:-7],shop_num,staff_nums[i],reservations_and_shedules[k].getStartTime(),reservations_and_shedules[k].getReservationPersonNum())
    shutil.rmtree(f'db\\shops\\{shop_num}')
    shops[shop_num].num = -1
    with open("db\\shops.pickle","wb") as fw:
        pickle.dump(shops,fw)
    tmp_l = shop_owners[shop_owner_num].getShopNums()
    for i in range(len(tmp_l)):
        if tmp_l[i] == shop_num:
            del tmp_l[i]
            break
    shop_owners[shop_owner_num].shop_nums = tmp_l
    with open("db\\shops.pickle","wb") as fw:
        pickle.dump(shops,fw)
    with open("db\\members\\shop_owners.pickle","wb") as fw:
        pickle.dump(shop_owners,fw)
    
    
def modShop(shop_num, shop):
    staff_nums = os.listdir(f"db\\shops\\{shop_num}")
    
    for i in range(len(staff_nums)):
        l = os.listdir(f"db\\shops\\{shop_num}\\{staff_nums[i]}")
        l = l[:-1]
        for j in range(len(l)):
            with open(f"db\\shops\\{shop_num}\\{staff_nums[i]}\\{l[j]}","rb") as fr:
                reservations_and_shedules = pickle.load(fr)
            for k in range(len(reservations_and_shedules)):
                if reservations_and_shedules[k].type() == 0:
                    delReservation(l[j][:-7],shop_num,staff_nums[i],reservations_and_shedules[k].getStartTime(),reservations_and_shedules[k].getReservationPersonNum())
    shops[shop_num] = shop
    with open("db\\shops.pickle","wb") as fw:
        pickle.dump(shops,fw)
    
def addStaffToShop(shop_num, staff_num):
    if staff_num >= len(shop_staffs):
        return 0
    elif shop_staffs[staff_num].getShopNum() != -1:
        return -1
    else:
        shop_staffs[staff_num].shop_num = shop_num
        print(f"shop_num = {shop_num}")
        with open("db\\members\\shop_staffs.pickle","wb") as fw:
            pickle.dump(shop_staffs,fw)
        os.mkdir(f"db\\shops\\{shop_num}\\{staff_num}")
        with open(f"db\\shops\\{shop_num}\\{staff_num}\\procedures.pickle","wb") as fw:
            pickle.dump([],fw)
        return 1
        

def delStaffToShop(shop_num, staff_num):
    l = os.listdir(f"db\\shops\\{shop_num}\\{staff_num}")
    l = l[:-1]
    for j in range(len(l)):
        with open(f"db\\shops\\{shop_num}\\{staff_num}\\{l[j]}","rb") as fr:
            reservations_and_shedules = pickle.load(fr)
        for k in range(len(reservations_and_shedules)):
            if reservations_and_shedules[k].type() == 0:
                delReservation(l[j][:-7],shop_num,staff_num,reservations_and_shedules[k].getStartTime(),reservations_and_shedules[k].getReservationPersonNum())
    
    shutil.rmtree(f'db\\shops\\{shop_num}\\{staff_num}')
    shop_staffs[staff_num].shop_num = -1
    with open("db\\members\\shop_staffs.pickle","wb") as fw:
        pickle.dump(shop_staffs,fw)
    
    

def addProcedureToStaff(procedure, shop_num, staff_num):
    with open(f"db\\shops\\{shop_num}\\{staff_num}\\procedures.pickle","rb") as fr:
        procedures = pickle.load(fr)
        
    for i in range(len(procedures)):
        if procedures[i].getName() == procedure.getName():
            return False
    
    procedures.append(procedure)
    with open(f"db\\shops\\{shop_num}\\{staff_num}\\procedures.pickle","wb") as fw:
        pickle.dump(procedures,fw)
    return True
    
    
def delProcedureToStaff(procedure_num, shop_num, staff_num):
    l = os.listdir(f"db\\shops\\{shop_num}\\{staff_num}")
    l = l[:-1]
    for j in range(len(l)):
        with open(f"db\\shops\\{shop_num}\\{staff_num}\\{l[j]}","rb") as fr:
            reservations_and_shedules = pickle.load(fr)
        for k in range(len(reservations_and_shedules)):
            if reservations_and_shedules[k].type() == 0:
                delReservation(l[j][:-7],shop_num,staff_num,reservations_and_shedules[k].getStartTime(),reservations_and_shedules[k].getReservationPersonNum())
    with open(f"db\\shops\\{shop_num}\\{staff_num}\\procedures.pickle","rb") as fr:
        procedures = pickle.load(fr)
    del procedures[procedure_num]
    with open(f"db\\shops\\{shop_num}\\{staff_num}\\procedures.pickle","wb") as fw:
        pickle.dump(procedures,fw)
     

def addReservation(shop_num, staff_num, date,  reservation, start_time,customer_num):
    reservations_and_schedules = []
    if os.path.exists(f"db\\shops\\{shop_num}\\{staff_num}\\{date}.pickle"):
        with open(f"db\\shops\\{shop_num}\\{staff_num}\\{date}.pickle","rb") as fr:
            reservations_and_schedules =  pickle.load(fr)
    check = 0
    for i in range(len(reservations_and_schedules)):
        if reservations_and_schedules[i].getStartTime() > start_time:
            reservations_and_schedules.insert(i,reservation)
            check = 1
            break
    if check == 0:
        reservations_and_schedules.append(reservation)
    with open(f"db\\shops\\{shop_num}\\{staff_num}\\{date}.pickle","wb") as fw:
        pickle.dump(reservations_and_schedules,fw)
    
    customers[customer_num].addReservation([date,shop_num,staff_num,reservation])
    with open("db\\members\\customers.pickle","wb") as fw:
        pickle.dump(customers,fw)

def addSchedule(shop_num, staff_num, date,  schedule, start_time):
    reservations_and_schedules = []
    if os.path.exists(f"db\\shops\\{shop_num}\\{staff_num}\\{date}.pickle"):
        with open(f"db\\shops\\{shop_num}\\{staff_num}\\{date}.pickle","rb") as fr:
            reservations_and_schedules =  pickle.load(fr)
    check = 0
    for i in range(len(reservations_and_schedules)):
        if reservations_and_schedules[i].getStartTime() > start_time:
            reservations_and_schedules.insert(i,schedule)
            check = 1
            break
    if check == 0:
        reservations_and_schedules.append(schedule)
    with open(f"db\\shops\\{shop_num}\\{staff_num}\\{date}.pickle","wb") as fw:
        pickle.dump(reservations_and_schedules,fw)
        
def delReservation(date, shop_num,staff_num,start_time, reservation_num):
    reservations_and_schedules = getReservationsAndSchedules(shop_num, staff_num, date)
    for i in range(len(reservations_and_schedules)):
        if reservations_and_schedules[i].getStartTime() == start_time:
            reservation = reservations_and_schedules[i]
            del reservations_and_schedules[i]
            break
    with open(f"db\\shops\\{shop_num}\\{staff_num}\\{date}.pickle","wb") as fw:
        pickle.dump(reservations_and_schedules,fw)
    
    customer_num = reservation.getReservationPersonNum()
    
    customers[customer_num].delReservation(reservation_num)
    with open("db\\members\\customers.pickle","wb") as fw:
        pickle.dump(customers,fw)


    
    
def delSchedule(date, shop_num, staff_num, start_time):
    reservations_and_schedules = getReservationsAndSchedules(shop_num, staff_num, date)
    for i in range(len(reservations_and_schedules)):
        if reservations_and_schedules[i].getStartTime() == start_time:
            del reservations_and_schedules[i]
            break
    with open(f"db\\shops\\{shop_num}\\{staff_num}\\{date}.pickle","wb") as fw:
        pickle.dump(reservations_and_schedules,fw)

def modTel(tel,num,classification):
    if classification == 0:
        shop_owners[num].setTel(tel)
        with open("db\\members\\shop_owners.pickle","wb") as fw:
            pickle.dump(shop_owners,fw)
            
    elif classification == 1:
        shop_staffs[num].setTel(tel)
        with open("db\\members\\shop_staffs.pickle","wb") as fw:
            pickle.dump(shop_staffs,fw)
    
    else:
        customers[num].setTel(tel)
        with open("db\\members\\customers.pickle","wb") as fw:
            pickle.dump(customers,fw)
        

def modPW(PW,num,classification):
    if classification == 0:
        shop_owners[num].setPW(PW)
        with open("db\\members\\shop_owners.pickle","wb") as fw:
            pickle.dump(shop_owners,fw)
            
    if classification == 1:
        shop_staffs[num].setPW(PW)
        with open("db\\members\\shop_staffs.pickle","wb") as fw:
            pickle.dump(shop_staffs,fw)
    
    else:
        customers[num].setPW(PW)
        with open("db\\members\\customers.pickle","wb") as fw:
            pickle.dump(customers,fw)
    

def getReservationsAndSchedules(shop_num, staff_num, date):
    if os.path.exists(f"db\\shops\\{shop_num}\\{staff_num}\\{date}.pickle"):
        with open(f"db\\shops\\{shop_num}\\{staff_num}\\{date}.pickle","rb") as fr:
            return pickle.load(fr)
    else:
        return []
    
def getProcedures(shop_num, staff_num):
    with open(f"db\\shops\\{shop_num}\\{staff_num}\\procedures.pickle","rb") as fr:
        return pickle.load(fr)
    
def getShopOwners():
    return shop_owners

def getShopStaffs():
    return shop_staffs

def getCustomers():
    return customers

def getShops():
    return shops