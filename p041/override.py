"""
@Time        : 2020/5/16
@Author      : KD_huhu
@File        : override
@Description : 
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class OverrideSlot(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Override（覆盖）槽函数")

    def keyPressEvent(self, e):  # 覆盖系统的keyPressEvent函数
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Alt:
            self.setWindowTitle("按下Alt键")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = OverrideSlot()
    form.show()
    sys.exit(app.exec_())
