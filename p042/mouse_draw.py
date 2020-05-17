"""
@Time        : 2020/5/17
@Author      : KD_huhu
@File        : mouse_draw
@Description : 
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QPoint


class Drawing(QWidget):

    def __init__(self, parent=None):
        super(Drawing, self).__init__(parent)
        self.setWindowTitle("绘图应用")
        # 在该图像类的实例中绘图
        self.pix = QPixmap()
        # 获取绘图坐标点
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUi()

    def initUi(self):
        self.resize(600, 600)
        # 画布大小为600*600，背景为白色
        self.pix = QPixmap(600, 600)
        self.pix.fill(Qt.white)

    def paintEvent(self, event):
        # 实例化一个绘图类对象
        pp = QPainter(self.pix)
        # 根据鼠标指针前后两个位置绘制直线
        pp.drawLine(self.lastPoint, self.endPoint)
        # 让前一个坐标值等于后一个坐标值
        # 这样就能实现画出连续的线
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 获取鼠标的坐标点
            self.lastPoint = event.pos()
    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()
    def mouseReleaseEvent(self, event):
        # 鼠标左键释放
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # 进行重新绘制
            self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Drawing()
    form.show()
    sys.exit(app.exec_())
