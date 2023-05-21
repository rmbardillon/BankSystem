from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QPushButton
from BankGUI.AccountCsv import get_account, edit_account, user_update_history


class Ui_withdraw_window(object):

    def main_menu(self, user_index):
        from MainMenu import UiMainMenu
        self.main_menu = QtWidgets.QMainWindow()
        self.ui = UiMainMenu()
        self.ui.setupUi(self.main_menu, user_index)
        self.main_menu.show()

    def setupUi(self, withdraw_window, user_index):
        withdraw_window.setObjectName("withdraw_window")
        withdraw_window.resize(800, 600)
        withdraw_window.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(withdraw_window)
        self.centralwidget.setObjectName("centralwidget")
        self.withdraw_label = QtWidgets.QLabel(self.centralwidget)
        self.withdraw_label.setGeometry(QtCore.QRect(30, 140, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.withdraw_label.setFont(font)
        self.withdraw_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.withdraw_label.setObjectName("withdraw_label")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(690, 0, 101, 91))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../../images/Bank logo 1.png"))
        self.logo_label.setObjectName("logo_label")
        self.input_withdraw = QtWidgets.QLineEdit(self.centralwidget)
        self.input_withdraw.setGeometry(QtCore.QRect(370, 140, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.input_withdraw.setFont(font)
        self.input_withdraw.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(85, 170, 255);")
        self.input_withdraw.setObjectName("input_deposit")
        self.input_withdraw.setValidator(QRegExpValidator(QRegExp("[0-9]{6}")))
        self.enter_button = QPushButton(self.centralwidget, clicked=lambda: self.enter_pressed(user_index, withdraw_window))
        self.enter_button.setGeometry(QtCore.QRect(530, 260, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.enter_button.setFont(font)
        self.enter_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(85, 170, 255);")
        self.enter_button.setObjectName("enter_button")
        self.cancel_button = QPushButton(self.centralwidget, clicked=lambda: self.main_menu(user_index))
        self.cancel_button.setGeometry(QtCore.QRect(200, 260, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(170, 0, 0);")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(lambda: withdraw_window.hide())
        withdraw_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(withdraw_window)
        self.statusbar.setObjectName("statusbar")
        withdraw_window.setStatusBar(self.statusbar)

        self.retranslateUi(withdraw_window)
        QtCore.QMetaObject.connectSlotsByName(withdraw_window)

    def retranslateUi(self, withdraw_window):
        _translate = QtCore.QCoreApplication.translate
        withdraw_window.setWindowTitle(_translate("withdraw_window", "Withdraw"))
        self.withdraw_label.setText(_translate("withdraw_window", "Input amount to withdraw"))
        self.enter_button.setText(_translate("withdraw_window", "ENTER"))
        self.cancel_button.setText(_translate("withdraw_window", "CANCEL"))

    def enter_pressed(self, user_index, withdraw_window):
        s_money_withdraw = self.input_withdraw.text()
        elements = get_account()
        balance = int(elements[user_index][2])
        if len(s_money_withdraw) == 0:
            self.error()
        else:
            money_withdraw = int(s_money_withdraw)
            if money_withdraw < 1:
                self.error()
            elif money_withdraw > balance:
                self.not_enough_money_error()
            else:
                balance -= money_withdraw
                elements[user_index][2] = balance
                edit_account(elements)
                self.withdraw_success(user_index)
                withdraw_window.hide()
                user_update_history(elements[user_index][0], "Withdraw", s_money_withdraw)
                self.main_menu(user_index)

    def withdraw_success(self, user_index):
        balance = get_account()[user_index][2]
        message = QMessageBox()
        message.setWindowTitle("Successful")
        message.setText(f"Your new balance is {'₱{:,.2f}'.format(int(balance))}")
        message.setIcon(QMessageBox.Information)
        message.exec_()


    def not_enough_money_error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText("Not enough Balance! ")
        message.setIcon(QMessageBox.Warning)
        message.exec_()


    def error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText("Your withdraw should not be less than ₱1! ")
        message.setIcon(QMessageBox.Warning)
        message.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    withdraw_window = QtWidgets.QMainWindow()
    ui = Ui_withdraw_window()
    ui.setupUi(withdraw_window, 0)
    withdraw_window.show()
    sys.exit(app.exec_())
