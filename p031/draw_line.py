import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle('设置Pen的样式')

    def paintEvent(self, event):
        painter = QPainter()                 # 创建画板
        painter.begin(self)
        pen = QPen(Qt.red, 3, Qt.SolidLine)  # 创建画笔，实现样式
        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)
        pen.setStyle(Qt.DashLine)            # 设置宽虚线样式
        painter.setPen(pen)                  # 设置完样式必须set才会生效
        painter.drawLine(20, 80, 250, 80)
        pen.setStyle(Qt.DashDotDotLine)      # 设置点划线样式
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)
        pen.setStyle(Qt.DotLine)  # 设置窄虚线
        painter.setPen(pen)
        painter.drawLine(20, 160, 250, 160)
        pen.setStyle(Qt.DashDotDotLine)      # 花式样式
        painter.setPen(pen)
        painter.drawLine(20, 200, 250, 200)
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 10, 5, 8])    # 自定义直线组合，[长度，间距，长度，间距...]
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)
        size = self.size()
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()
    sys.exit(app.exec_())