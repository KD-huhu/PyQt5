"""
@Time        : 2020/5/17
@Author      : KD_huhu
@File        : back_ground_qss
@Description : 
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("背景图片")
win.resize(350,250)
win.setObjectName("MainWindow")
# 通过QSS动态修改窗口的背景图片
win.setStyleSheet("#MainWindow{border-image:url(../images/python.jpg);}")
# 通过QSS动态修改窗口的背景颜色
# win.setStyleSheet("#MainWindow{background-color:yellow}")
win.show()
sys.exit(app.exec())
