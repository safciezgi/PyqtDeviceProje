# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from design import Ui_MainWindow
from SSHConnect import SSH_operation



class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ssh_obj = SSH_operation()
        self.ui.connect_btn.clicked.connect(self.ConnectButtonClicked)
        self.ui.send_btn.clicked.connect(self.SendButtonClicked)
        self.show()




    def ConnectButtonClicked(self):
        ip = self.ui.ssh_ip.text()
        user = self.ui.ssh_user.text()
        passwd = self.ui.ssh_pass.text()
        print(ip + " " + user + " " + passwd)
        self.ssh_obj.ssh_con(ip, user, passwd)


    def SendButtonClicked(self):
        hostn_send = self.ui.hostn_text.text()
        ip_send = self.ui.ip_text.text()
        subnet_send = self.ui.subnet_text.text()
        gateway_send = self.ui.gateway_text.text()
        print(hostn_send + " " + ip_send + " " + subnet_send + " " + gateway_send)
        self.ssh_obj.ssh_command("sed -i '$a Trailor' /home/ezgi/Desktop/sedsil.txt")








# ssh_obj = SSH_operation()
# ssh_obj.ssh_con("10.1.3.75", "ezgi", "0000")
# ssh_obj.ssh_command("pwd")


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())