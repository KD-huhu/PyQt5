import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll, self).__init__()
        self.resize(300, 600)
        self.setWindowTitle('绘制各种图形')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(Qt.blue)
        rect = QRect(0, 10, 100, 100)                   # 绘制弧，弧是圆的特殊形式，定义弧绘制区域
        qp.drawArc(rect, 0, 50 * 16)                    # alen: 1个alen等于1/16度，45度 = 45 * 16alen
        qp.setPen(Qt.red)                               # 通过弧绘制圆
        qp.drawArc(120, 10, 100, 100, 0, 360 * 16)      # 360度的弧就是圆
        qp.drawChord(10, 120, 100, 100, 12, 130 * 16)   # 绘制带弦的弧，弧的两个端点相连，参数和弧相同
        qp.drawPie(10, 240, 100, 100, 12, 130 * 16)     # 绘制扇形，弧的两个端点和圆心相连
        qp.drawEllipse(120, 120, 150, 100)              # 椭圆，长宽相等时就是圆
        point1 = QPoint(140, 380)                       # 绘制5边形
        point2 = QPoint(270, 420)
        point3 = QPoint(290, 512)
        point4 = QPoint(290, 588)
        point5 = QPoint(200, 533)
        polygon = QPolygon([point1, point2, point3, point4, point5])  # 创建多边形对象，将顶点坐标传入
        qp.drawPolygon(polygon)
        image = QImage('../images/book.png')                           # 绘制图像，读入图像
        rect = QRect(10, 400, image.width() / 3, image.height() / 3)  # 图像绘制的区域，图像的大小
        # image.save('./images/book1.png')                            # 保存图像
        qp.drawImage(rect, image)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawAll()
    main.show()
    sys.exit(app.exec_())