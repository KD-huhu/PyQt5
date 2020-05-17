"""
@Time        : 2020/5/17
@Author      : KD_huhu
@File        : window_opacity
@Description : 
"""
from PyQt5.Qt import *
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle('窗口的透明度设置')
    # 0到1，1表示不透明，0表示完全透明
    win.setWindowOpacity(0.6)
    button = QPushButton('我的按钮',win)
    # 控件的透明度会跟随窗口的透明度一起变化
    win.resize(400,200)
    win.show()
    sys.exit(app.exec())