"""
@Time        : 2020/5/17
@Author      : KD_huhu
@File        : back_ground_draw_1
@Description : 
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Background1(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("直接绘制背景")
        self.resize(350, 250)
    def paintEvent(self, event):
        painter = QPainter(self)
        # 通过直接绘制动态修改窗口的背景颜色
        painter.setBrush(Qt.yellow)
        painter.drawRect(self.rect())
        # 通过直接绘制动态修改窗口的背景图片
        pixmap = QPixmap('../images/python.jpg')
        painter.drawPixmap(self.rect(), pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Background1()
    form.show()
    sys.exit(app.exec_())
