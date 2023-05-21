from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QPushButton
from BankGUI.AccountCsv import get_account, edit_account


class Ui_change_pin_window(object):

    def main_menu(self, user_index):
        from MainMenu import UiMainMenu
        self.main_menu = QtWidgets.QMainWindow()
        self.ui = UiMainMenu()
        self.ui.setupUi(self.main_menu, user_index)
        self.main_menu.show()

    def setupUi(self, change_pin_window, user_index):
        change_pin_window.setObjectName("change_pin_window")
        change_pin_window.resize(800, 600)
        change_pin_window.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(change_pin_window)
        self.centralwidget.setObjectName("centralwidget")
        self.change_pin_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_pin_label_2.setGeometry(QtCore.QRect(30, 140, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.change_pin_label_2.setFont(font)
        self.change_pin_label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.change_pin_label_2.setObjectName("change_pin_label_2")
        self.log_label = QtWidgets.QLabel(self.centralwidget)
        self.log_label.setGeometry(QtCore.QRect(690, 10, 101, 91))
        self.log_label.setText("")
        self.log_label.setPixmap(QtGui.QPixmap("../../images/Bank logo 1.png"))
        self.log_label.setObjectName("log_label")
        self.input_pin = QtWidgets.QLineEdit(self.centralwidget)
        self.input_pin.setGeometry(QtCore.QRect(270, 140, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.input_pin.setFont(font)
        self.input_pin.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "selection-background-color: rgb(85, 170, 255);")
        self.input_pin.setText("")
        self.input_pin.setObjectName("input_pin")
        self.input_pin.setEchoMode(QLineEdit.Password)
        self.input_pin.setValidator(QRegExpValidator(QRegExp("[0-9]{4}")))
        self.change_pin_label = QtWidgets.QLabel(self.centralwidget)
        self.change_pin_label.setGeometry(QtCore.QRect(330, 20, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.change_pin_label.setFont(font)
        self.change_pin_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.change_pin_label.setObjectName("change_pin_label")
        self.confirm_button = QPushButton(self.centralwidget, clicked=lambda: self.enter_pressed(user_index, change_pin_window))
        self.confirm_button.setGeometry(QtCore.QRect(420, 380, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_button.setFont(font)
        self.confirm_button.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                          "color: rgb(255, 255, 255);")
        self.confirm_button.setObjectName("confirm_button")
        self.confirm_pin = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_pin.setGeometry(QtCore.QRect(270, 250, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.confirm_pin.setFont(font)
        self.confirm_pin.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "selection-background-color: rgb(85, 170, 255);")
        self.confirm_pin.setText("")
        self.confirm_pin.setObjectName("confirm_pin")
        self.confirm_pin.setEchoMode(QLineEdit.Password)
        self.confirm_pin.setValidator(QRegExpValidator(QRegExp("[0-9]{4}")))
        self.change_pin_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.change_pin_label_3.setGeometry(QtCore.QRect(30, 250, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.change_pin_label_3.setFont(font)
        self.change_pin_label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.change_pin_label_3.setObjectName("change_pin_label_3")
        self.cancel_button = QPushButton(self.centralwidget, clicked=lambda: self.main_menu(user_index))
        self.cancel_button.setGeometry(QtCore.QRect(80, 380, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(170, 0, 0);")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(lambda: change_pin_window.hide())
        change_pin_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(change_pin_window)
        self.statusbar.setObjectName("statusbar")
        change_pin_window.setStatusBar(self.statusbar)

        self.retranslateUi(change_pin_window)
        QtCore.QMetaObject.connectSlotsByName(change_pin_window)

    def retranslateUi(self, change_pin_window):
        _translate = QtCore.QCoreApplication.translate
        change_pin_window.setWindowTitle(_translate("change_pin_window", "Change Pin"))
        self.change_pin_label_2.setText(_translate("change_pin_window", "New Pin\n4 digit pin only"))
        self.change_pin_label.setText(_translate("change_pin_window", "Change Pin"))
        self.confirm_button.setText(_translate("change_pin_window", "CONFIRM"))
        self.change_pin_label_3.setText(_translate("change_pin_window", "Confirm Pin\n4 digit pin only"))
        self.cancel_button.setText(_translate("change_pin_window", "CANCEL"))

    def enter_pressed(self, user_index, change_pin_window):
        input_pin = self.input_pin.text()
        confirm_pin = self.confirm_pin.text()
        if len(input_pin) == 0 and len(confirm_pin) == 0:
            self.error()
            return False
        elif len(confirm_pin) != 4:
            self.confirm_pin_error()
            return False
        elif len(input_pin) != 4:
            self.input_pin_error()
            return False
        elif input_pin == get_account()[user_index][1]:
            self.same_pin_error()
            return False
        elif input_pin != confirm_pin:
            self.different_pin_error()
            return False
        else:
            elements = get_account()
            elements[user_index][1] = confirm_pin
            edit_account(elements)
            self.change_pin_success(user_index)
            change_pin_window.hide()
            self.main_menu(user_index)
            return True

    def change_pin_success(self, user_index):
        pin = get_account()[user_index][1]
        message = QMessageBox()
        message.setWindowTitle("Successful")
        message.setText(f"Your new pin is {pin}")
        message.setIcon(QMessageBox.Information)
        message.exec_()

    def same_pin_error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText("You already use this password ")
        message.setIcon(QMessageBox.Warning)
        message.exec_()

    def different_pin_error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText("Password not the same ")
        message.setIcon(QMessageBox.Warning)
        message.exec_()

    def input_pin_error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText("Fill out the Input Pin ")
        message.setIcon(QMessageBox.Warning)
        message.exec_()

    def confirm_pin_error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText("Fill out the Confirm Pin ")
        message.setIcon(QMessageBox.Warning)
        message.exec_()

    def error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText("4 digit pin only ")
        message.setIcon(QMessageBox.Warning)
        message.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    change_pin = QtWidgets.QMainWindow()
    ui = Ui_change_pin_window()
    ui.setupUi(change_pin, 0)
    change_pin.show()
    sys.exit(app.exec_())
