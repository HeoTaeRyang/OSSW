from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Main
import ShopInfo
import ReservationManagement
import ScheduleManagement
import ProfileManagement

class shop_staff_window(QDialog,Main.form_shop_staff):
    def __init__(self):
        super().__init__()
        self.shop_info = ShopInfo.ShopInfo()
        self.reservation_management = ReservationManagement.ReservationManagement()
        self.schedule_management = ScheduleManagement.ScheduleManagement()
        self.profile_management = ProfileManagement.ProfileManagement()
        self.shop_info.setWindow(self,1)
        
    def main_page(self):
        self.shop_info.selectWindow(self,0,1)
        self.shop_info.showMainPage(self)
        
    def main_shop_info_page(self,shop_num):
        self.shop_info.showMainShopInfoPage(self,shop_num,1)
    
    def reservation_page(self):
        self.shop_info.selectWindow(self,1,1)
        self.reservation_management.showReservationPage(self,1)
    
    def reservation_info_page(self):
        self.reservation_management.showReservationInfoPage(self,1)
        
    def schedule_page(self):
        self.shop_info.selectWindow(self,2,1)
        self.schedule_management.showSchedulePage(self)
        
    def schedule_info_page(self):
        self.schedule_management.showScheduleInfoPage(self)
        
    def profile_page(self):
        self.shop_info.selectWindow(self,3,1)
        self.profile_management.showProfilePage(self,1)