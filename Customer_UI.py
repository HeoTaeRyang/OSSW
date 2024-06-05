from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Main
import ShopInfo
import ReservationManagement
import ProfileManagement

class customer_window(QDialog,Main.form_customer):
    def __init__(self):
        super().__init__()
        self.shop_info = ShopInfo.ShopInfo()
        self.reservation_management = ReservationManagement.ReservationManagement()
        self.profile_management = ProfileManagement.ProfileManagement()
        self.shop_info.setWindow(self,2)
        
    def main_page(self):
        self.shop_info.selectWindow(self,0,2)
        self.shop_info.showMainPage(self)
        
    def main_shop_info_page(self,shop_num):
        self.shop_info.showMainShopInfoPage(self,shop_num,2)
        
    def main_reservation_page(self,shop_num):
        self.shop_info.showMainReservationPage(self,shop_num)
    
    def reservation_page(self):
        self.shop_info.selectWindow(self,1,2)
        self.reservation_management.showReservationPage(self,2)
        
    def reservation_info_page(self):
        self.reservation_management.showReservationInfoPage(self,2)
        
    def profile_page(self):
        self.shop_info.selectWindow(self,2,2)
        self.profile_management.showProfilePage(self,2)