import My_Structs

shop_owners = []
shop_staffs = []
customers = []
shops = []

file = open(r"db\shop_owners.txt", "r", encoding="UTF-8")
line = file.readline()
while line:
    tmp_l = line.split(',')
    tmp_shop_nums = []
    for i in range(5,len(tmp_l)):
        tmp_shop_nums.append(int(tmp_l[i]))
    tmp = My_Structs.ShopOwner(tmp_l[0], tmp_l[1], tmp_l[2], tmp_l[3], int(tmp_l[4]), tmp_shop_nums)
    shop_owners.append(tmp)
    line = file.readline()
file.close()

file = open(r"db\shop_staffs.txt", "r", encoding="UTF-8")
line = file.readline()
while line:
    tmp_l = line.split(',')
    tmp = My_Structs.ShopStaff(tmp_l[0], tmp_l[1], tmp_l[2], tmp_l[3], int(tmp_l[4]), int(tmp_l[5]))
    shop_staffs.append(tmp)
    line = file.readline()
file.close()

file = open(r"db\customers.txt", "r", encoding="UTF-8")
line = file.readline()
while line:
    tmp_l = line.split(',')
    tmp = My_Structs.Member(tmp_l[0], tmp_l[1], tmp_l[2], tmp_l[3], int(tmp_l[4]))
    customers.append(tmp)
    line = file.readline()
file.close()

file = open(r"db\shops.txt", "r", encoding="UTF-8")
line = file.readline()
while line:
    tmp_l = line.split(',')
    tmp_operation_hours = list(map(int, tmp_l[3:-1]))
    tmp = My_Structs.Shop(tmp_l[0],tmp_l[1],tmp_l[2],tmp_operation_hours,int(tmp_l[-1]))
    shops.append(tmp)
    line = file.readline()
file.close()

def addShopOwner(shop_owner):
    shop_owners.append(shop_owner)
    tmp = [shop_owner.getID(),shop_owner.getPW(),shop_owner.getName(),shop_owner.getTel(),str(shop_owner.getNum())]+list(map(str,shop_owner.getShopNums()))
    file = open('db\shop_owners.txt', 'a', encoding="UTF-8")
    file.writelines(','.join(tmp))
    file.write("\n")
    file.close()
def addShopStaff(shop_staff):
    shop_staffs.append(shop_staff)
    tmp = [shop_staff.getID(),shop_staff.getPW(),shop_staff.getName(),shop_staff.getTel(),str(shop_staff.getNum()),str(shop_staff.getShopNum())]
    file = open('db\shop_staffs.txt', 'a', encoding="UTF-8")
    file.writelines(','.join(tmp))
    file.write("\n")
    file.close()
def addCustomer(customer):
    customers.append(customer)
    tmp = [customer.getID(),customer.getPW(),customer.getName(),customer.getTel(),str(customer.getNum())]
    file = open('db\customers.txt', 'a', encoding="UTF-8")
    file.writelines(','.join(tmp))
    file.write("\n")
    file.close()
# def addShop(shop):