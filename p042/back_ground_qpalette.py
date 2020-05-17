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
palette = QPalette()
# 通过palette动态修改窗口的背景图片
palette.setBrush(QPalette.Background,QBrush(QPixmap("../images/python.jpg")))
# 通过palette动态修改窗口的背景颜色
# palette.setColor(QPalette.Background,Qt.red)
win.setPalette(palette)
win.show()
sys.exit(app.exec())
