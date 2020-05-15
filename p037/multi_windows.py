"""
@Time        : 2020/5/15
@Author      : DELL
@File        : multi_windows
@Description : 
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MultiWindows(QMainWindow):

    count = 0  # 记录当前窗口数
    def __init__(self, parent=None):
        super(MultiWindows, self).__init__(parent)
        self.setWindowTitle("容纳多文档的窗口")
        self.mdi = QMdiArea()       # 容纳多文档对象
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("File")  # 创建菜单
        file.addAction("New")
        file.addAction("cascade")   # 设置层叠方式
        file.addAction("Tiled")     # 设置平铺方式
        file.triggered.connect(self.windowaction)

    def windowaction(self, q):
        print(q.text())
        if q.text() == "New":
            MultiWindows.count = MultiWindows.count + 1
            sub = QMdiSubWindow()   # 创建子窗口对象
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("子窗口" + str(MultiWindows.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == "cascade":
            self.mdi.cascadeSubWindows()
        elif q.text() == "Tiled":
            self.mdi.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MultiWindows()
    demo.show()
    sys.exit(app.exec_())