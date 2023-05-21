from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QRect, QDateTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox, QPushButton, QLabel
from BankGUI.AccountCsv import get_account
from ChangePin import Ui_change_pin_window
from Deposit import Ui_deposit_window
from Withdraw import Ui_withdraw_window


class UiMainMenu(object):

    def thank_you_window(self, main_menu):
        from ThankYou import UiThankYouMenu
        self.thank_you_menu = QtWidgets.QMainWindow()
        self.ui = UiThankYouMenu()
        self.ui.setupUi(self.thank_you_menu)
        self.log_in_window(main_menu)
        self.thank_you_menu.show()
        QTimer.singleShot(5000, self.thank_you_menu.close)

    def log_in_window(self, main_menu):
        from Login import UiLoginWindow
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = UiLoginWindow()
        self.ui.setupUi(self.LoginWindow)
        main_menu.hide()
        self.LoginWindow.show()

    def deposit_window(self, user_index, username):
        self.deposit_window = QtWidgets.QMainWindow()
        self.ui = Ui_deposit_window()
        self.ui.setupUi(self.deposit_window, user_index, username)
        self.deposit_window.show()

    def withdraw_window(self, user_index, username):
        self.withdraw_window = QtWidgets.QMainWindow()
        self.ui = Ui_withdraw_window()
        self.ui.setupUi(self.withdraw_window, user_index, username)
        self.withdraw_window.show()

    def show_balance(self, user_index):
        balance = get_account()[user_index][3]
        message = QMessageBox()
        message.setWindowTitle("Balance Inquiry")
        message.setText(f"Your balance is {'₱{:,.2f}'.format(int(balance))}")
        message.setIcon(QMessageBox.Information)
        message.exec_()

    def change_pin_window(self, user_index, username):
        self.change_pin_window = QtWidgets.QMainWindow()
        self.ui = Ui_change_pin_window()
        self.ui.setupUi(self.change_pin_window, user_index, username)
        self.change_pin_window.show()

    def user_transactions_window(self, user_index, username):
        from UserViewTransactions import Ui_User_View_Transaction
        self.User_View_Transaction = QtWidgets.QMainWindow()
        self.ui = Ui_User_View_Transaction()
        self.ui.setupUi(self.User_View_Transaction, user_index, username)
        self.User_View_Transaction.show()

    def showTime(self):
        current_time = QDateTime.currentDateTime().toString('hh:mm:ss ap\ndddd yyyy MMMM dd')
        self.clock_label.setText(current_time)

    def setupUi(self, main_menu, user_index, username):
        main_menu.setObjectName("main_menu")
        main_menu.resize(800, 600)
        main_menu.setStyleSheet("background-color: rgb(85, 116, 255);\n"
                                "background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(main_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.atm_label = QtWidgets.QLabel(self.centralwidget)
        self.atm_label.setGeometry(QtCore.QRect(20, 30, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.atm_label.setFont(font)
        self.atm_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.atm_label.setObjectName("atm_label")
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
        self.name_label.setGeometry(QtCore.QRect(20, 190, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_label.setObjectName("name_label")
        self.name_label.setText(get_account()[user_index][0])
        self.withdraw_button = QPushButton(self.centralwidget, clicked=lambda: self.withdraw_window(user_index, username))
        self.withdraw_button.setGeometry(QtCore.QRect(530, 180, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.withdraw_button.setFont(font)
        self.withdraw_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(85, 170, 255);")
        self.withdraw_button.setObjectName("withdraw_button")
        self.withdraw_button.clicked.connect(lambda: main_menu.hide())
        self.deposit_button = QPushButton(self.centralwidget, clicked=lambda: self.deposit_window(user_index, username))
        self.deposit_button.setGeometry(QtCore.QRect(260, 180, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.deposit_button.setFont(font)
        self.deposit_button.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                          "color: rgb(255, 255, 255);")
        self.deposit_button.setObjectName("deposit_button")
        self.deposit_button.clicked.connect(lambda: main_menu.hide())
        self.changepin_button = QPushButton(self.centralwidget, clicked=lambda: self.change_pin_window(user_index, username))
        self.changepin_button.setGeometry(QtCore.QRect(530, 300, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.changepin_button.setFont(font)
        self.changepin_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(85, 170, 255);")
        self.changepin_button.setObjectName("changepin_button")
        self.changepin_button.clicked.connect(lambda: main_menu.hide())
        self.balinquiry_button = QPushButton(self.centralwidget, clicked=lambda: self.show_balance(user_index))
        self.balinquiry_button.setGeometry(QtCore.QRect(260, 300, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.balinquiry_button.setFont(font)
        self.balinquiry_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(85, 170, 255);")
        self.balinquiry_button.setObjectName("balinquiry_button")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(680, 20, 91, 81))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../../images/Bank logo 1.png"))
        self.logo_label.setObjectName("logo_label")
        self.exit_button = QPushButton(self.centralwidget, clicked=lambda:  self.thank_you_window(main_menu))
        self.exit_button.setGeometry(QtCore.QRect(40, 410, 161, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(170, 0, 0);")
        self.exit_button.setObjectName("pushButton")
        main_menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_menu)
        self.statusbar.setObjectName("statusbar")
        main_menu.setStatusBar(self.statusbar)
        self.view_transactions_button = QPushButton(self.centralwidget, clicked=lambda: self.user_transactions_window(user_index, username))
        self.view_transactions_button.clicked.connect(lambda: main_menu.hide())
        self.view_transactions_button.setObjectName(u"view_transactions_button")
        self.view_transactions_button.setGeometry(QRect(640, 150, 141, 21))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setWeight(50)
        self.view_transactions_button.setFont(font6)
        self.view_transactions_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                    "background-color: rgb(85, 170, 255);")
        self.retranslateUi(main_menu)
        QtCore.QMetaObject.connectSlotsByName(main_menu)

    def retranslateUi(self, main_menu):
        _translate = QtCore.QCoreApplication.translate
        main_menu.setWindowTitle(_translate("main_menu", "Main Menu"))
        self.atm_label.setText(_translate("main_menu", "ATM"))
        self.welcome_label.setText(_translate("main_menu", "Welcome"))
        self.withdraw_button.setText(_translate("main_menu", "WITHDRAW"))
        self.deposit_button.setText(_translate("main_menu", "DEPOSIT"))
        self.changepin_button.setText(_translate("main_menu", "CHANGE PIN"))
        self.balinquiry_button.setText(_translate("main_menu", "BALANCE INQUIRY"))
        self.exit_button.setText(_translate("main_menu", "LOGOUT"))
        self.view_transactions_button.setText(_translate("main_menu", "View Transactions"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_menu = QtWidgets.QMainWindow()
    ui = UiMainMenu()
    ui.setupUi(main_menu, 0, "user")
    main_menu.show()
    sys.exit(app.exec_())
