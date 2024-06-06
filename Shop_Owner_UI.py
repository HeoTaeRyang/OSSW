from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Main
import ShopInfo
import ShopManagement
import StaffManagement
import ReservationManagement
import ProfileManagement

class shop_owner_window(QDialog,Main.form_shop_owner):
    def __init__(self):
        super().__init__()
        self.shop_info = ShopInfo.ShopInfo()
        self.shop_management = ShopManagement.ShopManagement()
        self.staff_management = StaffManagement.StaffManagement()
        self.reservation_management = ReservationManagement.ReservationManagement()
        self.profile_management = ProfileManagement.ProfileManagement()
        self.shop_info.setWindow(self,0)
        
    def main_page(self):
        self.shop_info.selectWindow(self,0,0)
        self.shop_info.showMainPage(self)
    
    def main_shop_info_page(self,shop_num):
        self.shop_info.showMainShopInfoPage(self,shop_num,0)
            
    def shop_page(self):
        self.shop_info.selectWindow(self,1,0)
        self.shop_management.showShopPage(self)
        
    def shop_mod_page(self,shop_num):
        self.shop_management.showShopModPage(self,shop_num)
    
    def shop_add_page(self):
        self.shop_management.showShopAddPage(self)
        
    def staff_page(self):
        self.shop_info.selectWindow(self,2,0)
        self.staff_management.showStaffPage(self)
        
    def staff_info_page(self,shop_nums):
        self.staff_management.showStaffInfoPage(self,shop_nums)
        
    def staff_mod_page(self,shop_num,staff_num):
        self.staff_management.showStaffModPage(self,shop_num,staff_num)
        
    def staff_add_page(self,shop_num):
        self.staff_management.showStaffAddPage(self,shop_num)
                    
    def reservation_page(self):
        self.shop_info.selectWindow(self,3,0)
        self.reservation_management.showReservationPage(self,0)
        
    def reservation_info_page(self):
        self.reservation_management.showReservationInfoPage(self,0)
        
    def profile_page(self):
        self.shop_info.selectWindow(self,4,0)
        self.profile_management.showProfilePage(self,0)