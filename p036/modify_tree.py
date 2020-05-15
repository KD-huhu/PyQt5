import sys
from PyQt5.QtWidgets import *


class ModifyTree(QWidget):

    def __init__(self, parent=None):
        super(ModifyTree, self).__init__(parent)
        self.setWindowTitle('TreeWidget 例子')
        operatorLayout = QHBoxLayout()
        addBtn = QPushButton('添加节点')
        updateBtn = QPushButton('修改节点')
        deleteBtn = QPushButton('删除节点')
        operatorLayout.addWidget(addBtn)
        operatorLayout.addWidget(updateBtn)
        operatorLayout.addWidget(deleteBtn)
        addBtn.clicked.connect(self.addNode)        # 绑定槽
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)
        self.tree = QTreeWidget()                   # 生成树
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Key','Value'])
        root  = QTreeWidgetItem(self.tree)
        root.setText(0,'root')
        root.setText(1, '0')
        child1 = QTreeWidgetItem(root)
        child1.setText(0,'child1')
        child1.setText(1,'1')
        child2 = QTreeWidgetItem(root)
        child2.setText(0,'child2')
        child2.setText(1,'2')
        child3 = QTreeWidgetItem(child2)
        child3.setText(0,'child3')
        child3.setText(1,'3')
        self.tree.clicked.connect(self.onTreeClicked)
        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)
        self.setLayout(mainLayout)

    def onTreeClicked(self,index):
        item = self.tree.currentItem()
        print(index.row())
        print('key=%s,value=%s' % (item.text(0),item.text(1)))
    def addNode(self):                          # 添加节点
        print('添加节点')
        item = self.tree.currentItem()          # 获取当前节点
        print(item)
        node = QTreeWidgetItem(item)            # 创建节点对象，为当前节点添加子节点
        node.setText(0,'新节点')
        node.setText(1,'新值')
    def updateNode(self):
        print('修改节点')
        item = self.tree.currentItem()          # 对当前节点进行修改
        item.setText(0,'修改节点')
        item.setText(1, '值已经被修改')
    def deleteNode(self):
        print('删除节点')
        item = self.tree.currentItem()          # 当前节点
        root = self.tree.invisibleRootItem()    # 当根节点的父节点
        for item in self.tree.selectedItems():  # 要从父节点中删除
            (item.parent() or root).removeChild(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = ModifyTree()
    tree.show()
    sys.exit(app.exec_())
