"""
@Time        : 2020/5/15
@Author      : DELL
@File        : dock_widget
@Description : 
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DockDemo(QMainWindow):

    def __init__(self, parent=None):
        super(DockDemo, self).__init__(parent)
        self.setWindowTitle("停靠控件（QDockWidget）")
        self.resize(400,300)
        layout = QHBoxLayout()
        self.items = QDockWidget('Dockable',self)   # 创建悬浮停靠对象
        self.listWidget = QListWidget()
        self.listWidget.addItem('item1')            # 添加控件
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')
        self.items.setWidget(self.listWidget)
        self.setCentralWidget(QLineEdit())
        # 修改默认为悬浮
        self.items.setFloating(True)
        # 添加停靠窗口，默认停靠位置是右侧
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DockDemo()
    demo.show()
    sys.exit(app.exec_())
