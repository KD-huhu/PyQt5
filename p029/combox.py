import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表控件演示')
        self.resize(300,100)
        layout = QVBoxLayout()                  # 设置垂直布局
        self.label = QLabel('请选择编程语言')    # 提示信息
        self.cb = QComboBox()                   # 创建下拉列表对象
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        self.cb.addItems(['Java','C#','Ruby'])  # 一次添加多个控件
        self.cb.currentIndexChanged.connect(self.selectionChange)   # 获取当前选中元素的索引
        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)

    def selectionChange(self,i):                # 默认传递两个参数 第二个当前选择的索引
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()
        for count in range(self.cb.count()):    # 获取所有的元素
            print('item' + str(count) + '=' + self.cb.itemText(count))
        print('current index',i,'selection changed', self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())