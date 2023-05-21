import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QTimer, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QMessageBox, QLabel
from AddAccount import UiAddAccountWindow
from DeleteAccount import UiDeleteAccountWindow
from BankGUI.AccountCsv import create_file


class UIAdminMenu(object):

    def log_in_window(self):
        from AdminLogin import UiLoginWindow
        self.AdminLoginWindow = QtWidgets.QMainWindow()
        self.ui = UiLoginWindow()
        self.ui.setupUi(self.AdminLoginWindow)
        self.AdminLoginWindow.show()

    def add_account(self):
        self.add_account_window = QtWidgets.QMainWindow()
        self.ui = UiAddAccountWindow()
        self.ui.setupUi(self.add_account_window)
        self.add_account_window.show()

    def delete_account(self):
        create_file()
        file = '../AdminHistoryFolder/' + 'Accounts.txt'
        if os.path.getsize(file) == 0:
            self.no_account_error()
            self.add_account()
        else:
            self.delete_account_window = QtWidgets.QMainWindow()
            self.ui = UiDeleteAccountWindow()
            self.ui.setupUi(self.delete_account_window)
            self.delete_account_window.show()

    def no_account_error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText("No Account as of the moment. Click Ok to add account.")
        message.setIcon(QMessageBox.Warning)
        message.exec_()

    def admin_transactions_window(self):
        from AdminViewTransactions import Ui_Admin_View_Transaction
        self.Admin_View_Transaction = QtWidgets.QMainWindow()
        self.ui = Ui_Admin_View_Transaction()
        self.ui.setupUi(self.Admin_View_Transaction)
        self.Admin_View_Transaction.show()

    def view_accounts_window(self):
        from AdminViewAccounts import Ui_Admin_View_Accounts
        self.Admin_View_Transaction = QtWidgets.QMainWindow()
        self.ui = Ui_Admin_View_Accounts()
        self.ui.setupUi(self.Admin_View_Transaction)
        self.Admin_View_Transaction.show()

    def showTime(self):
        current_time = QDateTime.currentDateTime().toString('hh:mm:ss ap\ndddd yyyy MMMM dd')
        self.clock_label.setText(current_time)

    def setupUi(self, Admin_Menu):
        Admin_Menu.setObjectName("main_menu")
        Admin_Menu.resize(800, 600)
        Admin_Menu.setStyleSheet("background-color: rgb(85, 116, 255);\n"
                                "background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(Admin_Menu)
        self.centralwidget.setObjectName("centralwidget")
        timer = QTimer(self.centralwidget)
        timer.timeout.connect(self.showTime)
        timer.start(0)
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setWeight(75)
        self.clock_label = QLabel(self.centralwidget)
        self.clock_label.setObjectName(u"clock_label")
        self.clock_label.setGeometry(QRect(260, 30, 401, 61))
        self.clock_label.setFont(font4)
        self.clock_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.atm_label = QtWidgets.QLabel(self.centralwidget)
        self.atm_label.setGeometry(QtCore.QRect(20, 30, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.atm_label.setFont(font)
        self.atm_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.atm_label.setObjectName("atm_label")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(20, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("color: rgb(0, 0, 127);\n"
                                         "color: rgb(85, 170, 255);")
        self.welcome_label.setObjectName("welcome_label")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(20, 190, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_label.setObjectName("name_label")
        self.delete_account_button = QPushButton(self.centralwidget, clicked=lambda: self.delete_account())
        self.delete_account_button.setGeometry(QtCore.QRect(510, 210, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.delete_account_button.setFont(font)
        self.delete_account_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                 "background-color: rgb(85, 170, 255);")
        self.delete_account_button.setObjectName("delete_account_button")
        self.delete_account_button.clicked.connect(lambda: Admin_Menu.hide())
        self.add_account_button = QPushButton(self.centralwidget, clicked=lambda: self.add_account())
        self.add_account_button.setGeometry(QtCore.QRect(240, 210, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.add_account_button.setFont(font)
        self.add_account_button.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                              "color: rgb(255, 255, 255);")
        self.add_account_button.setObjectName("add_account_button")
        self.add_account_button.clicked.connect(lambda: Admin_Menu.hide())
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(680, 20, 91, 81))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../../images/Bank logo 1.png"))
        self.logo_label.setObjectName("logo_label")
        self.exit_button = QPushButton(self.centralwidget, clicked=lambda: self.log_in_window())
        self.exit_button.setGeometry(QtCore.QRect(40, 410, 161, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font3 = QFont()
        font3.setPointSize(22)
        font3.setBold(True)
        font3.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(170, 0, 0);")
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(lambda: Admin_Menu.hide())
        self.view_transactions_button = QPushButton(self.centralwidget, clicked=lambda: self.admin_transactions_window())
        self.view_transactions_button.clicked.connect(lambda: Admin_Menu.hide())
        self.view_transactions_button.setObjectName(u"view_transactions_button")
        self.view_transactions_button.setGeometry(QRect(510, 330, 251, 81))
        self.view_transactions_button.setFont(font3)
        self.view_transactions_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                    "background-color: rgb(85, 170, 255);")
        self.view_account_button = QPushButton(self.centralwidget, clicked=lambda: self.view_accounts_window())
        self.view_account_button.clicked.connect(lambda: Admin_Menu.hide())
        self.view_account_button.setObjectName(u"view_account_button")
        self.view_account_button.setGeometry(QRect(240, 330, 251, 81))
        self.view_account_button.setFont(font3)
        self.view_account_button.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
                                               "color: rgb(255, 255, 255);")
        Admin_Menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Admin_Menu)
        self.statusbar.setObjectName("statusbar")
        Admin_Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Admin_Menu)
        QtCore.QMetaObject.connectSlotsByName(Admin_Menu)

    def retranslateUi(self, main_menu):
        _translate = QtCore.QCoreApplication.translate
        main_menu.setWindowTitle(_translate("main_menu", "Main Menu"))
        self.atm_label.setText(_translate("main_menu", "ATM"))
        self.welcome_label.setText(_translate("main_menu", "Welcome"))
        self.name_label.setText(_translate("main_menu", "ADMINISTRATOR"))
        self.delete_account_button.setText(_translate("main_menu", "DELETE\n"
                                                                   "ACCOUNT"))
        self.add_account_button.setText(_translate("main_menu", "ADD ACCOUNT"))
        self.exit_button.setText(_translate("main_menu", "EXIT"))
        self.view_transactions_button.setText(_translate("main_menu", u"VIEW\nTRANSACTIONS", None))
        self.view_account_button.setText(_translate("main_menu", u"VIEW\nACCOUNTS", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_menu = QtWidgets.QMainWindow()
    ui = UIAdminMenu()
    ui.setupUi(admin_menu)
    admin_menu.show()
    sys.exit(app.exec_())
