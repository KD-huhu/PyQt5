import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        bar = self.menuBar()          # 获取当前窗口菜单栏
        file = bar.addMenu("文件")    # 添加菜单内容
        file.addAction("新建")        # 添加带有动作的菜单
        save = QAction("保存", self)
        save.setShortcut("Ctrl + S")  # 设置快捷键
        file.addAction(save)
        save.triggered.connect(self.process)
        quit = QAction("退出", self)
        file.addAction(quit)
        edit = bar.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")
        self.resize(300,200)

    def process(self, a):
        print(self.sender().text())  # 获取点击文本内容


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec_())