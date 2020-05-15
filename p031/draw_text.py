import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(500, 400)
        self.text = "Python从菜鸟到高手"

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QColor(150, 43, 5))    # 设置画笔
        painter.setFont(QFont('SimSun', 25))  # 设置字体
        # 第一个参数为绘制区域 第二个参数是绘制方式 第三个参数是绘制的内容
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawText()
    main.show()
    sys.exit(app.exec_())
