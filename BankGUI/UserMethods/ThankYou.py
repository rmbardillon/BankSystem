from PyQt5 import QtCore, QtGui, QtWidgets


class UiThankYouMenu(object):
    def setupUi(self, main_menu):
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
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(150, 130, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcome_label.setObjectName("welcome_label")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(680, 20, 91, 81))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../../images/Bank logo 1.png"))
        self.logo_label.setObjectName("logo_label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(170, 250, 421, 181))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        main_menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_menu)
        self.statusbar.setObjectName("statusbar")
        main_menu.setStatusBar(self.statusbar)

        self.retranslateUi(main_menu)
        QtCore.QMetaObject.connectSlotsByName(main_menu)

    def retranslateUi(self, main_menu):
        _translate = QtCore.QCoreApplication.translate
        main_menu.setWindowTitle(_translate("main_menu", "Main Menu"))
        self.atm_label.setText(_translate("main_menu", "ATM"))
        self.welcome_label.setText(_translate("main_menu", "THANK YOU FOR USING OUR BANK SYSTEM."))
        self.textBrowser.setHtml(_translate("main_menu",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GROUP MEMBERS</p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bardillon, Romeo Jr. M.</p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Porlares, Aaron S.</p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rivera, Rhodemil Zeth M.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    thank_you_menu = QtWidgets.QMainWindow()
    ui = UiThankYouMenu()
    ui.setupUi(thank_you_menu)
    thank_you_menu.show()
    sys.exit(app.exec_())
