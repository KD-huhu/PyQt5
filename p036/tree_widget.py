import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt


class BasicTreeWidget(QMainWindow):

    def __init__(self, parent=None):
        super(BasicTreeWidget, self).__init__(parent)
        self.setWindowTitle('树控件（QTreeWidget）的基本用法')
        self.tree = QTreeWidget()                   # 创建树控件对象
        self.tree.setColumnCount(2)                 # 为树控件指定列数
        self.tree.setHeaderLabels(['Key','Value'])  # 指定列标
        root = QTreeWidgetItem(self.tree)           # 定义根节点
        root.setText(0,'根节点')
        root.setIcon(0,QIcon('../images/root.png'))
        self.tree.setColumnWidth(0,160)             # 设置列宽
        # 添加子节点1
        child1 = QTreeWidgetItem(root)              # 先生成子节点对象，参数为父节点
        child1.setText(0,'子节点1')
        child1.setText(1,'子节点1的数据')
        child1.setIcon(0,QIcon('../images/bao3.png'))
        child1.setCheckState(0,Qt.Checked)          # 添加复选框，并默认选中
        # 添加子节点2
        child2 = QTreeWidgetItem(root)              # 先生成子节点对象
        child2.setText(0,'子节点2')
        child2.setIcon(0,QIcon('../images/bao6.png'))
        # 为child2添加一个子节点
        child3 = QTreeWidgetItem(child2)            # 先生成子节点对象
        child3.setText(0,'子节点2-1')
        child3.setText(1,'新的值')
        child3.setIcon(0,QIcon('../images/music.png'))
        self.tree.expandAll()                       # 默认使所有节点展开
        self.setCentralWidget(self.tree)            # 设置树
        self.resize(500,400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = BasicTreeWidget()
    tree.show()
    sys.exit(app.exec_())
