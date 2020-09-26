# -*- coding: utf-8 -*-
import sys, os
from PyQt5 import  uic, QtCore, QtGui
from PyQt5.QtWidgets import *
import qr_rc
class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("src/cafex.ui", self)
        self.button0=self.but0
        self.button1 = self.but1
        self.button2 = self.but2
        self.button3 = self.but3
        self.button4 = self.but4
        self.button5 = self.but5
        self.button6 = self.but6
        self.button7 = self.but7
        self.button8 = self.but8
        self.button9 = self.but9
        self.line=self.linepass
        self.validate=self.valid
        self.remove=self.supp

        self.button0.clicked.connect(self.clickbtn)
        self.button1.clicked.connect(self.clickbtn)
        self.button2.clicked.connect(self.clickbtn)
        self.button3.clicked.connect(self.clickbtn)
        self.button4.clicked.connect(self.clickbtn)
        self.button5.clicked.connect(self.clickbtn)
        self.button6.clicked.connect(self.clickbtn)
        self.button7.clicked.connect(self.clickbtn)
        self.button8.clicked.connect(self.clickbtn)
        self.button9.clicked.connect(self.clickbtn)


        self.supp.clicked.connect(self.rmvbtn)




    def rmvbtn(self):
        self.line.clear()

    def clickbtn(self):
        # print(self.sender)
        self.line.insert(self.sender().text())
    def validate(self):
        self.line.text()
        pass



app = QApplication(sys.argv)
window = UI()
window.show()
app.exec_()
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     window = Gispalt()
#     entre = Entree()
#     entre.setUp()
#     entre.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#     entre.show()
#     window.setUp()
#     window.showMaximized()
#     sys.exit(app.exec_())