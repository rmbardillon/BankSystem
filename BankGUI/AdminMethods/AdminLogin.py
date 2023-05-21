from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QPushButton


class UiLoginWindow(object):

    def admin_menu(self):
        from AdminMenu import UIAdminMenu
        self.admin_menu = QtWidgets.QMainWindow()
        self.ui = UIAdminMenu()
        self.ui.setupUi(self.admin_menu)
        self.admin_menu.show()

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
        self.welcome_label.setGeometry(QtCore.QRect(40, 10, 251, 51))
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
        self.welcome_label.setText(_translate("MainWindow", "Welcome Administrator"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))

    def login_pressed(self, AdminLoginWindow):
        username_entry = self.username_input.text()
        pin_entry = self.password_input.text()
        if "admin" == username_entry and "1234" == pin_entry:
            AdminLoginWindow.hide()
            self.admin_menu()
        elif username_entry != "admin":
            self.login_error()
        else:
            self.login_error()

    def login_error(self):
        message = QMessageBox()
        message.setWindowTitle("Try again")
        message.setText("Username or Pin is incorrect.")
        message.setIcon(QMessageBox.Warning)
        message.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminLoginWindow = QtWidgets.QMainWindow()
    ui = UiLoginWindow()
    ui.setupUi(AdminLoginWindow)
    AdminLoginWindow.show()
    sys.exit(app.exec_())
