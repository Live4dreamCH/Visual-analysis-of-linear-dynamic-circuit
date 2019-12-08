import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


################################################
#######创建主窗口
################################################
class FirstMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('主界面')

        ###### 创建界面 ######
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.Layout = QVBoxLayout(self.centralwidget)

        # 设置顶部三个按钮
        self.topwidget = QWidget()
        self.Layout.addWidget(self.topwidget)
        self.buttonLayout = QHBoxLayout(self.topwidget)

        self.pushButton1 = QPushButton()
        self.pushButton1.setText("打开主界面")
        self.buttonLayout.addWidget(self.pushButton1)

        # 设置中间文本
        self.label = QLabel()
        self.label.setText("第一个主界面")
        self.label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Roman times", 50, QFont.Bold))
        self.Layout.addWidget(self.label)

        # 设置状态栏
        self.statusBar().showMessage("当前用户：一心狮")

        # 窗口最大化
        self.showMaximized()

        ###### 三个按钮事件 ######
        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)

    # 按钮一：打开主界面
    windowList = []

    def on_pushButton1_clicked(self):
        the_window = SecondWindow()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


################################################
#######第二个主界面
################################################
class SecondWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('第二主界面')

        # 设置中间文本
        self.label = QLabel()
        self.label.setText("第二个主界面")
        self.label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Roman times", 50, QFont.Bold))
        self.setCentralWidget(self.label)

        # 设置状态栏
        self.statusBar().showMessage("当前用户：一心狮")

        # 窗口最大化
        self.showMaximized()

    ###### 重写关闭事件，回到第一界面
    windowList = []

    def closeEvent(self, event):
        the_window = FirstMainWindow()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        the_window.show()
        event.accept()


################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = FirstMainWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())
