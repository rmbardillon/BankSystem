from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize, QDateTime, QTimer
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QCommandLinkButton, QLabel, QAbstractItemView
from BankWithDatabase.DatabaseMethods import get_admin_transactions_in_database


class Ui_Admin_View_Accounts(object):

    def main_menu(self):
        from AdminMenu import UIAdminMenu
        self.admin_menu = QtWidgets.QMainWindow()
        self.ui = UIAdminMenu()
        self.ui.setupUi(self.admin_menu)
        self.admin_menu.show()

    def showTime(self):
        current_time = QDateTime.currentDateTime().toString('hh:mm:ss ap\ndddd yyyy MMMM dd')
        self.clock_label.setText(current_time)

    def setupUi(self, Admin_View_Transaction):
        Admin_View_Transaction.setObjectName("Admin_View_Transaction")
        Admin_View_Transaction.resize(800, 600)
        Admin_View_Transaction.setStyleSheet("background-color: rgb(85, 116, 255);\n"
                                             "background-color: rgb(0, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(Admin_View_Transaction)
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
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(680, 20, 91, 81))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../../images/Bank logo 1.png"))
        self.logo_label.setObjectName("logo_label")
        font5 = QFont()
        font5.setPointSize(13)
        font5.setBold(False)
        font5.setWeight(75)
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
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 130, 779, 441))
        self.tableWidget.setDisabled(True)
        self.tableWidget.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0, 207)
        self.tableWidget.setFont(font5)
        self.tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(1, 190)
        self.tableWidget.setFont(font5)
        self.tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(2, 190)
        self.tableWidget.setFont(font5)
        self.tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(3, 190)
        self.tableWidget.setFont(font5)
        self.tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        row = 0
        for items in get_admin_transactions_in_database("customer"):
            self.tableWidget.setRowCount(len(get_admin_transactions_in_database("customer")))
            column = 0
            items[2] = str(items[2])
            items[3] = "₱{:,.2f}".format(float(items[3]))
            for item in items:
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(item))
                self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
                column += 1
            row += 1
        Admin_View_Transaction.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Admin_View_Transaction)
        self.statusbar.setObjectName("statusbar")
        Admin_View_Transaction.setStatusBar(self.statusbar)
        self.commandLinkButton = QCommandLinkButton(self.centralwidget, clicked=lambda: self.main_menu())
        self.commandLinkButton.clicked.connect(lambda: Admin_View_Transaction.hide())
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(0, 0, 41, 41))
        icon = QIcon()
        icon.addFile(u"../../images/back_button_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon)

        self.retranslateUi(Admin_View_Transaction)
        QtCore.QMetaObject.connectSlotsByName(Admin_View_Transaction)

    def retranslateUi(self, Admin_View_Transaction):
        _translate = QtCore.QCoreApplication.translate
        Admin_View_Transaction.setWindowTitle(_translate("Admin_View_Transaction", "Accounts"))
        self.atm_label.setText(_translate("Admin_View_Transaction", "ATM"))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setFont(font)
        item.setText(_translate("User_View_Transaction", "Username"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setFont(font)
        item.setText(_translate("User_View_Transaction", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setFont(font)
        item.setText(_translate("User_View_Transaction", "Pin"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setFont(font)
        item.setText(_translate("User_View_Transaction", "Balance"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Admin_View_Transaction = QtWidgets.QMainWindow()
    ui = Ui_Admin_View_Accounts()
    ui.setupUi(Admin_View_Transaction)
    Admin_View_Transaction.show()
    sys.exit(app.exec_())
