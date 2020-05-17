"""
@Time        : 2020/5/17
@Author      : KD_huhu
@File        : picture_scale
@Description : 
"""
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import sys


class ScaleImage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图片大小缩放例子")
        filename = '../images/Cloudy_72px.png'
        # 创建一个图片类的实例
        img = QImage(filename)
        label1 = QLabel(self)
        label1.setFixedWidth(200)
        label1.setFixedHeight(200)
        # Qt.IgnoreAspectRati属性是忽略长宽比
        # Qt.SmoothTransformation属性是是图像尽量平滑显示
        result = img.scaled(label1.width(),label1.height(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        # 将图形显示在label中
        label1.setPixmap(QPixmap.fromImage(result))
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ScaleImage()
    win.show()
    sys.exit(app.exec_())

