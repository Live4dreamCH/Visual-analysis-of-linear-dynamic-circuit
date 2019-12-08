from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class FirstWindow(object):
    my_main = None

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
        self.my_main.hide()
        windowList[2].show()

    def open_second(self):
        self.my_main.hide()
        windowList[1].show()


class SecondWindow(object):
    # def __init__(self, *args, **kwargs):
    #     super.__init__(*args, **kwargs)

    my_main = None

    def __init__(self):
        self.LC = 0
        self.R = 0
        self.LCv = 0
        self.U0 = 0
        self.Uoo = 0

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
        infomation = ["电容C", "电感L"]
        self.LCchoose.addItems(infomation)
        self.LCchoose.activated[int].connect(self.setLC)

        self.draw = QtWidgets.QPushButton(self.splitter_4)
        self.draw.setObjectName("draw")
        self.draw.clicked.connect(self.read)

        self.clear = QtWidgets.QPushButton(self.splitter_4)
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.clearfun)

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

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(15, 140, 771, 411))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

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

    def goback(self):
        self.my_main.hide()
        self.clearfun()
        windowList[0].show()

    def read(self):
        self.R = float(self.Rin.text())
        self.LCv = float(self.LCin.text())
        self.U0 = float(self.U0in.text())
        self.Uoo = float(self.Uooin.text())
        self.drawpic()

    def setLC(self, ind):
        self.LC = ind

    def clearfun(self):
        self.LC = 0
        self.R = 0
        self.LCv = 0
        self.U0 = 0
        self.Uoo = 0

        self.LCin.clear()
        self.Rin.clear()
        self.U0in.clear()
        self.Uooin.clear()

    def drawpic(self):
        # 清屏
        plt.cla()
        # 获取绘图并绘制
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.set_xlim([-1, 6])
        ax.set_ylim([-1, 6])
        ax.plot([0, 1, 2, 3, 4, 5], 'o--')
        cavans = FigureCanvas(fig)
        # QtCore.QRect(15, 140, 771, 411)
        cavans.draw()
        cavans.show()
        # 将绘制好的图像设置为中心 Widget
        self.my_main


class ThirdWindow(object):
    my_main = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_9 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_9.setGeometry(QtCore.QRect(440, 10, 251, 121))
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
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 10, 20, 121))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.return_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.return_2.setGeometry(QtCore.QRect(720, 10, 71, 41))
        self.return_2.setObjectName("return_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(700, 10, 20, 121))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.splitter_14 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_14.setGeometry(QtCore.QRect(10, 10, 391, 121))
        self.splitter_14.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_14.setObjectName("splitter_14")
        self.splitter_12 = QtWidgets.QSplitter(self.splitter_14)
        self.splitter_12.setOrientation(QtCore.Qt.Vertical)
        self.splitter_12.setObjectName("splitter_12")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_12)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_7 = QtWidgets.QLabel(self.splitter_5)
        self.label_7.setObjectName("label_7")
        self.Rin_2 = QtWidgets.QLineEdit(self.splitter_5)
        self.Rin_2.setObjectName("Rin_2")
        self.splitter_10 = QtWidgets.QSplitter(self.splitter_12)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName("splitter_10")
        self.label_8 = QtWidgets.QLabel(self.splitter_10)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.U0in_2 = QtWidgets.QLineEdit(self.splitter_10)
        self.U0in_2.setObjectName("U0in_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_12)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        self.label_4.setObjectName("label_4")
        self.LCin = QtWidgets.QLineEdit(self.splitter)
        self.LCin.setObjectName("LCin")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_12)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.U0in = QtWidgets.QLineEdit(self.splitter_2)
        self.U0in.setObjectName("U0in")
        self.splitter_13 = QtWidgets.QSplitter(self.splitter_14)
        self.splitter_13.setOrientation(QtCore.Qt.Vertical)
        self.splitter_13.setObjectName("splitter_13")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_13)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_3 = QtWidgets.QLabel(self.splitter_4)
        self.label_3.setObjectName("label_3")
        self.Rin = QtWidgets.QLineEdit(self.splitter_4)
        self.Rin.setObjectName("Rin")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_13)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_2 = QtWidgets.QLabel(self.splitter_3)
        self.label_2.setObjectName("label_2")
        self.Uooin = QtWidgets.QLineEdit(self.splitter_3)
        self.Uooin.setObjectName("Uooin")
        self.splitter_11 = QtWidgets.QSplitter(self.splitter_13)
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName("splitter_11")
        self.draw = QtWidgets.QPushButton(self.splitter_11)
        self.draw.setObjectName("draw")
        self.clear = QtWidgets.QPushButton(self.splitter_11)
        self.clear.setObjectName("clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.menu.addAction(self.actionhelp)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.return_2.clicked.connect(self.goback)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "时间t："))
        self.label_6.setText(_translate("MainWindow", "电压U："))
        self.return_2.setText(_translate("MainWindow", "返回"))
        self.label_7.setText(_translate("MainWindow", "C"))
        self.label_8.setText(_translate("MainWindow", "I0"))
        self.label_4.setText(_translate("MainWindow", "L"))
        self.label.setText(_translate("MainWindow", "U0"))
        self.label_3.setText(_translate("MainWindow", "R"))
        self.label_2.setText(_translate("MainWindow", "Uoo"))
        self.draw.setText(_translate("MainWindow", "二阶电路分析"))
        self.clear.setText(_translate("MainWindow", "清空"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.actionhelp.setText(_translate("MainWindow", "help"))
        self.my_main = MainWindow

    def goback(self):
        self.my_main.hide()
        windowList[0].show()


if __name__ == '__main__':
    import sys
    import cgitb

    cgitb.enable()

    # import numpy

    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    MainWindow2 = QtWidgets.QMainWindow()
    MainWindow3 = QtWidgets.QMainWindow()
    windowList = [MainWindow1, MainWindow2, MainWindow3]

    ui1 = FirstWindow()
    ui1.setupUi(MainWindow1)

    ui2 = SecondWindow()
    ui2.setupui(MainWindow2)

    ui3 = ThirdWindow()
    ui3.setupUi(MainWindow3)

    MainWindow1.show()
    sys.exit(app.exec_())
