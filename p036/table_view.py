from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class TableView(QWidget):

    def __init__(self, arg=None):
        super(TableView, self).__init__(arg)
        self.setWindowTitle("QTableView表格视图控件演示")
        self.resize(500, 300);
        self.model = QStandardItemModel(4, 3)  # 创建数据源对象
        self.model.setHorizontalHeaderLabels(['id', '姓名', '年龄'])  # 设置标题
        self.tableview = QTableView()
        self.tableview.setModel(self.model)    # 关联QTableView控件和Model
        item11 = QStandardItem('10')           # 创建数据
        item12 = QStandardItem('雷神')
        item13 = QStandardItem('2000')
        self.model.setItem(0, 0, item11)       # 添加数据
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)
        item31 = QStandardItem('30')
        item32 = QStandardItem('死亡女神')
        item33 = QStandardItem('3000')
        self.model.setItem(2, 0, item31)       # 添加数时可以有选择性添加，允许部分空白
        self.model.setItem(2, 1, item32)
        self.model.setItem(2, 2, item33)
        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = TableView()
    table.show()
    sys.exit(app.exec_())
