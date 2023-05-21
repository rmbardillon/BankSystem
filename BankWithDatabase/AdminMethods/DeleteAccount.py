from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QMessageBox
from BankGUI.AccountCsv import delete_account, user_update_history, admin_update_history, move_file
from BankWithDatabase.DatabaseMethods import delete_account_in_database, delete_account_transactions, account_is_existing

class UiDeleteAccountWindow(object):

    def main_menu(self):
        from AdminMenu import UIAdminMenu
        self.admin_menu = QtWidgets.QMainWindow()
        self.ui = UIAdminMenu()
        self.ui.setupUi(self.admin_menu)
        self.admin_menu.show()

    def setupUi(self, delete_account_window):
        delete_account_window.setObjectName("deposit_window")
        delete_account_window.resize(800, 600)
        delete_account_window.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(delete_account_window)
        self.centralwidget.setObjectName("centralwidget")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(30, 140, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.username_label.setObjectName("username_label")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(690, 10, 101, 91))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../../images/Bank logo 1.png"))
        self.logo_label.setObjectName("logo_label")
        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(370, 140, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "selection-background-color: rgb(85, 170, 255);")
        self.username_input.setText("")
        self.username_input.setObjectName("username_input")
        self.enter_button = QPushButton(self.centralwidget, clicked=lambda: self.enter_pressed_button(delete_account_window))
        self.enter_button.setGeometry(QtCore.QRect(450, 250, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.enter_button.setFont(font)
        self.enter_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(85, 170, 255);")
        self.enter_button.setObjectName("enter_button")
        self.cancel_button = QPushButton(self.centralwidget, clicked=lambda: self.main_menu())
        self.cancel_button.clicked.connect(lambda: delete_account_window.hide())
        self.cancel_button.setGeometry(QtCore.QRect(170, 260, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(170, 0, 0);")
        self.cancel_button.setObjectName("cancel_button")
        self.username_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.username_label_2.setGeometry(QtCore.QRect(300, 30, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.username_label_2.setFont(font)
        self.username_label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.username_label_2.setObjectName("username_label_2")
        delete_account_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(delete_account_window)
        self.statusbar.setObjectName("statusbar")
        delete_account_window.setStatusBar(self.statusbar)

        self.retranslateUi(delete_account_window)
        QtCore.QMetaObject.connectSlotsByName(delete_account_window)

    def retranslateUi(self, deposit_window):
        _translate = QtCore.QCoreApplication.translate
        deposit_window.setWindowTitle(_translate("deposit_window", "Delete Account"))
        self.username_label.setText(_translate("deposit_window", "Input username to delete"))
        self.enter_button.setText(_translate("deposit_window", "CONFIRM"))
        self.cancel_button.setText(_translate("deposit_window", "CANCEL"))
        self.username_label_2.setText(_translate("deposit_window", "DELETE ACCOUNT"))

    def enter_pressed_button(self, delete_account_window):
        username = self.username_input.text()
        if not account_is_existing(username):
            self.error()
        else:
            delete_account(username)
            delete_account_in_database(username)
            self.account_deleted_successfully()
            delete_account_window.hide()
            user_update_history(username, "Delete Account", "0")
            admin_update_history(username, "Delete Account")
            delete_account_transactions(username)
            move_file(username)

    def account_deleted_successfully(self):
        message = QMessageBox()
        message.setWindowTitle("Success")
        message.setText(f"User {self.username_input.text()} is deleted.")
        message.setIcon(QMessageBox.Information)
        message.exec_()
        self.main_menu()

    def error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText("Username not existing.")
        message.setIcon(QMessageBox.Warning)
        message.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_account_window = QtWidgets.QMainWindow()
    ui = UiDeleteAccountWindow()
    ui.setupUi(delete_account_window)
    delete_account_window.show()
    sys.exit(app.exec_())
