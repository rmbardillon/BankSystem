from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QPushButton, QMessageBox, QLineEdit
from BankGUI.AccountCsv import get_account, edit_account, user_update_history, admin_update_history
from BankWithDatabase.DatabaseMethods import add_account, account_is_existing

class UiAddAccountWindow(object):

    def main_menu(self):
        from AdminMenu import UIAdminMenu
        self.admin_menu = QtWidgets.QMainWindow()
        self.ui = UIAdminMenu()
        self.ui.setupUi(self.admin_menu)
        self.admin_menu.show()

    def setupUi(self, add_account_window):
        add_account_window.setObjectName("add_account_window")
        add_account_window.resize(800, 600)
        add_account_window.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(add_account_window)
        self.centralwidget.setObjectName("centralwidget")
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(280, 90, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_input.setFont(font)
        self.name_input.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "selection-background-color: rgb(85, 170, 255);")
        self.name_input.setText("")
        self.name_input.setObjectName("name_input")
        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(280, 190, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "selection-background-color: rgb(85, 170, 255);")
        self.username_input.setText("")
        self.username_input.setObjectName("username_input")
        self.pin_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pin_input.setEchoMode(QLineEdit.Password)
        self.pin_input.setValidator(QRegExpValidator(QRegExp("[0-9]{4}")))
        self.pin_input.setGeometry(QtCore.QRect(280, 300, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pin_input.setFont(font)
        self.pin_input.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "selection-background-color: rgb(85, 170, 255);")
        self.pin_input.setText("")
        self.pin_input.setObjectName("pin_input")
        self.balance_input = QtWidgets.QLineEdit(self.centralwidget)
        self.balance_input.setValidator(QRegExpValidator(QRegExp("[0-9]{6}")))
        self.balance_input.setGeometry(QtCore.QRect(280, 400, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.balance_input.setFont(font)
        self.balance_input.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(85, 170, 255);")
        self.balance_input.setText("")
        self.balance_input.setObjectName("balance_input")
        self.confirm_button = QPushButton(self.centralwidget, clicked=lambda: self.enter_pressed_button(add_account_window))
        self.confirm_button.setGeometry(QtCore.QRect(410, 500, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_button.setFont(font)
        self.confirm_button.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                          "color: rgb(255, 255, 255);")
        self.confirm_button.setObjectName("confirm_button")
        self.cancel_button = QPushButton(self.centralwidget, clicked=lambda: self.main_menu())
        self.cancel_button.clicked.connect(lambda: add_account_window.hide())
        self.cancel_button.setGeometry(QtCore.QRect(60, 500, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(170, 0, 0);")
        self.cancel_button.setObjectName("cancel_button")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(40, 190, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.username_label.setObjectName("username_label")
        self.log_label = QtWidgets.QLabel(self.centralwidget)
        self.log_label.setGeometry(QtCore.QRect(690, 10, 101, 91))
        self.log_label.setText("")
        self.log_label.setPixmap(QtGui.QPixmap("../../images/Bank logo 1.png"))
        self.log_label.setObjectName("log_label")
        self.add_account_label = QtWidgets.QLabel(self.centralwidget)
        self.add_account_label.setGeometry(QtCore.QRect(330, 10, 200, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.add_account_label.setFont(font)
        self.add_account_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.add_account_label.setObjectName("add_account_label")
        self.pin_label = QtWidgets.QLabel(self.centralwidget)
        self.pin_label.setGeometry(QtCore.QRect(40, 300, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pin_label.setFont(font)
        self.pin_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.pin_label.setObjectName("pin_label")
        self.balance_label = QtWidgets.QLabel(self.centralwidget)
        self.balance_label.setGeometry(QtCore.QRect(20, 400, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.balance_label.setFont(font)
        self.balance_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.balance_label.setObjectName("balance_label")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(40, 90, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_label.setObjectName("name_label")
        add_account_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(add_account_window)
        self.statusbar.setObjectName("statusbar")
        add_account_window.setStatusBar(self.statusbar)

        self.retranslateUi(add_account_window)
        QtCore.QMetaObject.connectSlotsByName(add_account_window)

    def retranslateUi(self, change_pin_window):
        _translate = QtCore.QCoreApplication.translate
        change_pin_window.setWindowTitle(_translate("add_account_window", "Add Account"))
        self.username_label.setText(_translate("add_account_window", "Username"))
        self.add_account_label.setText(_translate("add_account_window", "ADD ACCOUNT"))
        self.confirm_button.setText(_translate("add_account_window", "CONFIRM"))
        self.pin_label.setText(_translate("add_account_window", "Pin\n4 digit pin only"))
        self.cancel_button.setText(_translate("add_account_window", "CANCEL"))
        self.balance_label.setText(_translate("add_account_window", "Initial Balance\n(₱ 100 above)"))
        self.name_label.setText(_translate("add_account_window", "Name"))

    def enter_pressed_button(self, add_account_window):
        new_user = []
        username_entry = self.username_input.text()
        if account_is_existing(username_entry):
            self.duplicate_account_error()
        elif len(username_entry) == 0 or len(self.balance_input.text()) == 0 or len(self.pin_input.text()) == 0:
            self.error()
        elif int(self.balance_input.text()) < 100:
            self.balance_error()
        else:
            name_entry = self.name_input.text()
            new_user.append(name_entry)
            new_user.append(username_entry)
            pin_entry = self.pin_input.text()
            if len(pin_entry) != 4:
                self.error()
            else:
                new_user.append(pin_entry)
                balance_entry = self.balance_input.text()
                new_user.append(balance_entry)
                existing_users = get_account()
                existing_users.append(new_user)
                edit_account(existing_users)
                user_update_history(username_entry, "Create Account", self.balance_input.text())
                admin_update_history(username_entry, "Add Account")
                add_account(username_entry, name_entry, pin_entry, int(self.balance_input.text()))
                self.add_account_success()
                add_account_window.hide()
                self.main_menu()

    def add_account_success(self):
        message = QMessageBox()
        message.setWindowTitle("Successful")
        message.setText(f"New user\nName: {self.name_input.text()}\nUsername: {self.username_input.text()}\nPin: {self.pin_input.text()}")
        message.setIcon(QMessageBox.Information)
        message.exec_()

    def duplicate_account_error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText(f"{self.username_input.text()} already exists. ")
        message.setIcon(QMessageBox.Warning)
        message.exec_()

    def empty_account_error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText(f"Null username is not allowed.")
        message.setIcon(QMessageBox.Warning)
        message.exec_()

    def error(self):
        message = QMessageBox()
        message.setWindowTitle("Try Again")
        message.setText("Please fill out the form properly.")
        message.setIcon(QMessageBox.Warning)
        message.exec_()

    def balance_error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText("Initial Balance should not be less than 100.")
        message.setIcon(QMessageBox.Warning)
        message.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_account_window = QtWidgets.QMainWindow()
    ui = UiAddAccountWindow()
    ui.setupUi(add_account_window)
    add_account_window.show()
    sys.exit(app.exec_())
