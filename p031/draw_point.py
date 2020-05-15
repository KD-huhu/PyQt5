import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class DrawPoints(QWidget):
    def __init__(self):
        super(DrawPoints, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle('在窗口上用像素点绘制2个周期的正弦曲线')

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)  # 设置画笔颜色
        size = self.size()
        for i in range(1000):    # 1000次循环，绘制1000个点
            # 计算绘图点的坐标
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            painter.drawPoint(x, y)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawPoints()
    main.show()
    sys.exit(app.exec_())