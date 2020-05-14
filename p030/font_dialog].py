import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Font Dialog例子')
        layout = QVBoxLayout()
        self.fontButton = QPushButton('选择字体')  # 点击按钮弹出字体对话框
        self.fontButton.clicked.connect(self.getFont)
        layout.addWidget(self.fontButton)
        self.fontLabel = QLabel('Hello，测试字体例子')  # 使用标签显示字体变化
        layout.addWidget(self.fontLabel)
        self.setLayout(layout)
        self.resize(300,200)

    def getFont(self):
        # 第一个参数是选中的元素，第二个参数是是否点击退出
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontLabel.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())