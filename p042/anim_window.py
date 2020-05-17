"""
@Time        : 2020/5/17
@Author      : KD_huhu
@File        : anim_window
@Description : 
"""
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class AnimWindow(QWidget):

    def __init__(self):
        super(AnimWindow, self).__init__()
        self.OrigHeight = 50
        self.ChangeHeight = 150
        self.setGeometry(QRect(500, 400, 150, self.OrigHeight))
        self.btn = QPushButton('展开', self)
        self.btn.setGeometry(10, 10, 60, 35)
        self.btn.clicked.connect(self.change)
    def change(self):
        currentHeight = self.height()
        if self.OrigHeight == currentHeight:
            startHeight = self.OrigHeight
            endHeight = self.ChangeHeight
            self.btn.setText('收缩')
        else:
            startHeight = self.ChangeHeight
            endHeight= self.OrigHeight
            self.btn.setText('展开')
        # 第一个参数移动对象
        # 第二个参数移动发生的坐标系
        self.animation = QPropertyAnimation(self,b'geometry')
        # 变化时间
        self.animation.setDuration(500)
        # 设置开始变化时尺寸
        self.animation.setStartValue(QRect(500,400,150,startHeight))
        # 设置结束变化时尺寸
        self.animation.setEndValue(QRect(500,400,150,endHeight))
        # 开始变化
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnimWindow()
    window.show()
    sys.exit(app.exec_())