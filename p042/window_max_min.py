"""
@Time        : 2020/5/17
@Author      : KD_huhu
@File        : window_max_min
@Description : 
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WindowMaxMin(QWidget):

    # 构造函数
    def __init__(self, parent=None):
        # 调用父类构造函数
        super(WindowMaxMin, self).__init__(parent)
        self.resize(300,400)
        self.setWindowTitle("用代码控制窗口的最大化和最小化")
        # 设置窗口按钮
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        layout = QVBoxLayout()
        maxButton1 = QPushButton()
        maxButton1.setText('窗口最大化1')
        maxButton1.clicked.connect(self.maximized1)
        maxButton2 = QPushButton()
        maxButton2.setText('窗口最大化2')
        # 调用系统的槽方法实现窗口最大化,最大化过程中包含动画特效
        # 系统最大化函数不会覆盖标题栏
        maxButton2.clicked.connect(self.showMaximized)
        minButton = QPushButton()
        minButton.setText('窗口最小化')
        minButton.clicked.connect(self.showMinimized)
        layout.addWidget(maxButton1)
        layout.addWidget(maxButton2)
        layout.addWidget(minButton)
        self.setLayout(layout)

    # 设置窗口尺寸方法实现最大化
    def maximized1(self):
        # 实例化一个桌面对象类
        desktop = QApplication.desktop()
        # 获取桌面可用尺寸，包括标题栏，不包括工具栏
        rect = desktop.availableGeometry()
        self.setGeometry(rect)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowMaxMin()
    window.show()
    # 应用程序事件循环
    sys.exit(app.exec_())
