import os
from PyQt5.QtGui import QIntValidator
from BankGUI.AccountCsv import account_index, create_file
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QPushButton
from BankWithDatabase.DatabaseMethods import account_is_existing, is_correct

class UiLoginWindow(object):

    def main_menu(self, user_index, username):
        from MainMenu import UiMainMenu
        self.main_menu = QtWidgets.QMainWindow()
        self.ui = UiMainMenu()
        self.ui.setupUi(self.main_menu, user_index, username)
        self.main_menu.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(343, 414)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(85, 116, 255);\n"
                                 "background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(20, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcome_label.setObjectName("welcome_label")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(70, 220, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(70, 250, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.password_label.setObjectName("password_label")
        self.login_button = QPushButton(self.centralwidget, clicked=lambda: self.login_pressed(MainWindow))
        self.login_button.setGeometry(QtCore.QRect(190, 280, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.login_button.setObjectName("login_button")
        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(150, 220, 113, 20))
        self.username_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.username_input.setText("")
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(150, 250, 113, 20))
        self.password_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.password_input.setInputMethodHints(QtCore.Qt.ImhNone)
        self.password_input.setText("")
        self.password_input.setObjectName("password_input")
        self.password_input.setValidator(QIntValidator(1000, 9999))
        self.password_input.setEchoMode(QLineEdit.Password)
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(150, 110, 111, 91))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../../images/Bank logo 1.png"))
        self.logo_label.setObjectName("logo_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.close_window = MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bank System"))
        self.welcome_label.setText(_translate("MainWindow", "Welcome to our Bank System"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))

    def login_pressed(self, LoginWindow):
        username_entry = self.username_input.text()
        pin_entry = self.password_input.text()
        user_index = account_index(username_entry)
        if not account_is_existing(username_entry):
            self.no_user_existing_error()
        elif len(pin_entry) < 4:
            self.login_error()
        else:
            if is_correct(username_entry, int(pin_entry)):
                LoginWindow.hide()
                self.main_menu(user_index, username_entry)
            else:
                self.login_error()

    def login_error(self):
        message = QMessageBox()
        message.setWindowTitle("Try again")
        message.setText("Username or Pin is incorrect")
        message.setIcon(QMessageBox.Warning)
        message.exec_()

    def no_user_existing_error(self):
        message = QMessageBox()
        message.setWindowTitle("Try again")
        message.setText("No existing user. ")
        message.setIcon(QMessageBox.Warning)
        message.exec_()


def no_account_error():
    message = QMessageBox()
    message.setWindowTitle("Error")
    message.setText("No Account as of the moment. Go to Admin to Add Account.")
    message.setIcon(QMessageBox.Warning)
    message.exec_()


if __name__ == "__main__":
    import sys

    admin_save_path = "../AdminHistoryFolder/"
    file = admin_save_path + 'Accounts.txt'
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = UiLoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    create_file()
    if os.path.getsize(file) == 0:
        no_account_error()
    else:
        sys.exit(app.exec_())
