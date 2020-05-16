"""
@Time        : 2020/5/16
@Author      : KD_huhu
@File        : sinle_shot
@Description : 
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('<font color=red size=140><b>Hello World，窗口在5秒后自动关闭!</b></font>')
    # 设置窗口样式
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()
    QTimer.singleShot(5000,app.quit)    # 定时器定时5s只执行一次
    sys.exit(app.exec_())