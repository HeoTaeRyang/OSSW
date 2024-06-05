import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Login_UI

form_class = uic.loadUiType("ui\\login.ui")[0]
form_registration = uic.loadUiType("ui\\registration.ui")[0]
form_shop_owner = uic.loadUiType("ui\\shop_owner.ui")[0]
form_shop_staff = uic.loadUiType("ui\\shop_staff.ui")[0]
form_customer = uic.loadUiType("ui\\customer.ui")[0]
num = -1

if __name__ == "__main__" :
    app = QApplication(sys.argv) 

    myWindow = Login_UI.login_window() 
    myWindow.show()

    app.exec_()