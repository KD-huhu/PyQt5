import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Toolbar(QMainWindow):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("工具栏例子")
        self.resize(300, 200)
        tb1 = self.addToolBar("File")                           # 创建工具栏对象
        new = QAction(QIcon('../images/new.png'), "new", self)   # 创建action
        tb1.addAction(new)                                      # 添加action
        open = QAction(QIcon('../images/open.png'), "open", self)
        tb1.addAction(open)
        save = QAction(QIcon('../images/save.png'), "save", self)
        tb1.addAction(save)
        tb2 = self.addToolBar("File1")                          # 创建工具栏对象
        new1 = QAction(QIcon('../images/new.png'), "新建", self)  # 创建action
        tb2.addAction(new1)
        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)      # 设置图标和文本显示方式
        tb1.actionTriggered.connect(self.toolbtnpressed)        # 绑定槽
        tb2.actionTriggered.connect(self.toolbtnpressed)

    def toolbtnpressed(self, a):
        print("按下的工具栏按钮是", a.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Toolbar()
    main.show()
    sys.exit(app.exec_())