"""
@Time        : 2020/5/16
@Author      : KD_huhu
@File        : hbox_layout
@Description : 
"""
import sys,math
from PyQt5.QtWidgets import *


class HBoxLayout(QWidget) :
    def __init__(self):
        super(HBoxLayout,self).__init__()
        self.setWindowTitle("水平盒布局")
        hlayout = QHBoxLayout() # 创建水平盒布局类的实例
        hlayout.addWidget(QPushButton('按钮1'))
        hlayout.addWidget(QPushButton('按钮2'))
        hlayout.addWidget(QPushButton('按钮3'))
        hlayout.addWidget(QPushButton('按钮4'))
        hlayout.addWidget(QPushButton('按钮5'))
        hlayout.setSpacing(40)  # 设置间距
        self.setLayout(hlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HBoxLayout()
    main.show()
    sys.exit(app.exec_())