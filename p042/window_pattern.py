"""
@Time        : 2020/5/17
@Author      : KD_huhu
@File        : window_pattern
@Description : 
"""
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *


class WindowPattern(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,260)
        self.setWindowTitle('设置窗口的样式')
        # 设置窗口样式
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        # 设置名字
        self.setObjectName("MainWindow")
        # 设置窗口背景，实现类似于JS语言
        self.setStyleSheet("#MainWindow{border-image:url(../images/python.jpg);}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WindowPattern()
    form.show()
    sys.exit(app.exec_())
