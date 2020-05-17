"""
@Time        : 2020/5/16
@Author      : KD_huhu
@File        : win_signal
@Description : 
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class WinSignal(QWidget):

    button_clicked_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("为窗口类添加信号")
        self.resize(300,100)
        btn = QPushButton('关闭窗口',self)
        btn.clicked.connect(self.btn_clicked)
        # 信号关联信号
        self.button_clicked_signal.connect(self.btn_close)

    def btn_clicked(self):
        # 触发一个信号
        self.button_clicked_signal.emit()
    def btn_close(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = WinSignal()
    example.show()
    sys.exit(app.exec_())
