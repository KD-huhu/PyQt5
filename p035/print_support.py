from PyQt5 import QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import *
import sys


class PrintSupport(QMainWindow):
    def __init__(self):
        super(PrintSupport,self).__init__()
        self.setGeometry(500, 200, 300, 300)
        self.button = QPushButton('打印QTextEdit控件中的内容',self) # 创建按钮对象
        self.button.setGeometry(20,20,260,30)                       # 设置按钮位置
        self.editor = QTextEdit('默认文本',self)                    # 创建文本对象
        self.editor.setGeometry(20,60,260,200)
        self.button.clicked.connect(self.print)

    def print(self):
        printer = QtPrintSupport.QPrinter()                         # 创建打印机对象
        painter = QtGui.QPainter()                                  # 创建画布对象
        painter.begin(printer)                                      # 画布初始化，参数是将画板绘制的目标重定向到打印机
        screen = self.editor.grab()
        painter.drawPixmap(10,10,screen)                            # 绘制位置
        painter.end()                                               # 关闭画板
        print("print")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = PrintSupport()
    gui.show()
    app.exec_()