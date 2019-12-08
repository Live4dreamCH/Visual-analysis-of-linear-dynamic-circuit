# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'one.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cgitb
cgitb.enable()


class SecondWindow(object):
    # def __init__(self, *args, **kwargs):
    #     super.__init__(*args, **kwargs)

    my_main = None
    windowList = []

    def setupui(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setMinimumSize(QtCore.QSize(800, 600))
        mainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(15)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(280, 10, 20, 121))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.splitter_5 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_5.setGeometry(QtCore.QRect(10, 10, 261, 121))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        self.label_3.setObjectName("label_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.LCin = QtWidgets.QLineEdit(self.splitter)
        self.LCin.setObjectName("LCin")
        self.U0in = QtWidgets.QLineEdit(self.splitter)
        self.U0in.setObjectName("U0in")
        self.Uooin = QtWidgets.QLineEdit(self.splitter)
        self.Uooin.setObjectName("Uooin")
        self.Rin = QtWidgets.QLineEdit(self.splitter)
        self.Rin.setObjectName("Rin")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.LCchoose = QtWidgets.QComboBox(self.splitter_4)
        self.LCchoose.setObjectName("LCchoose")
        self.draw = QtWidgets.QPushButton(self.splitter_4)
        self.draw.setObjectName("draw")
        self.clear = QtWidgets.QPushButton(self.splitter_4)
        self.clear.setObjectName("clear")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(570, 10, 20, 121))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.return_first = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.return_first.setGeometry(QtCore.QRect(590, 10, 185, 41))
        self.return_first.setObjectName("return_first")
        self.splitter_9 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_9.setGeometry(QtCore.QRect(310, 10, 251, 121))
        self.splitter_9.setOrientation(QtCore.Qt.Vertical)
        self.splitter_9.setObjectName("splitter_9")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.label_5 = QtWidgets.QLabel(self.splitter_7)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.splitter_7)
        self.label_6.setObjectName("label_6")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.showT = QtWidgets.QLCDNumber(self.splitter_6)
        self.showT.setObjectName("showT")
        self.showF = QtWidgets.QLCDNumber(self.splitter_6)
        self.showF.setObjectName("showF")
        self.slideT = QtWidgets.QSlider(self.splitter_9)
        self.slideT.setOrientation(QtCore.Qt.Horizontal)
        self.slideT.setObjectName("slideT")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionhelp = QtWidgets.QAction(mainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.menu.addAction(self.actionhelp)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "动态电路时域分析"))
        self.label_4.setText(_translate("mainWindow", "L/C"))
        self.label.setText(_translate("mainWindow", "U0"))
        self.label_2.setText(_translate("mainWindow", "Uoo"))
        self.label_3.setText(_translate("mainWindow", "R"))
        self.draw.setText(_translate("mainWindow", "RL电路分析"))
        self.clear.setText(_translate("mainWindow", "清空"))
        self.return_first.setText(_translate("mainWindow", "返回"))
        self.label_5.setText(_translate("mainWindow", "时间t："))
        self.label_6.setText(_translate("mainWindow", "电压U/电流I："))
        self.menu.setTitle(_translate("mainWindow", "帮助"))
        self.actionhelp.setText(_translate("mainWindow", "help"))
        self.my_main = mainWindow
        self.return_first.clicked.connect(self.goback)
        print("have connected")

    def goback(self):
        print("let's go!")
        MainWindow0 = QtWidgets.QMainWindow()
        self.windowList.append(MainWindow0)  ##注：没有这句，是不打开另一个主界面的！
        the_window = FirstWindow()
        the_window.setupUi(MainWindow0)
        self.my_main.close()
        MainWindow0.show()


class FirstWindow(object):
    my_main = None
    windowList = []

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setMinimumSize(QtCore.QSize(800, 600))
        mainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(15)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(80, 260, 191, 31))
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(490, 260, 191, 31))
        self.two.setObjectName("two")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionhelp = QtWidgets.QAction(mainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.menu.addAction(self.actionhelp)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.one.setText(_translate("mainWindow", "一阶电路全响应分析"))
        self.one.clicked.connect(self.open_second)
        self.two.setText(_translate("mainWindow", "二阶电路全响应分析"))
        self.two.clicked.connect(self.open_third)
        self.menu.setTitle(_translate("mainWindow", "帮助"))
        self.actionhelp.setText(_translate("mainWindow", "help"))
        self.my_main = mainWindow

    def open_third(self):
        MainWindow3 = QtWidgets.QMainWindow()
        the_window = SecondWindow()
        the_window.setupui(MainWindow3)
        self.windowList.append(MainWindow3)  ##注：没有这句，是不打开另一个主界面的！
        self.my_main.close()
        MainWindow3.show()

    def open_second(self):
        MainWindow2 = QtWidgets.QMainWindow()
        self.windowList.append(MainWindow2)  ##注：没有这句，是不打开另一个主界面的！
        the_window = SecondWindow()
        the_window.setupui(MainWindow2)
        self.my_main.close()
        MainWindow2.show()


if __name__ == '__main__':
    import sys
    import numpy

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FirstWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
