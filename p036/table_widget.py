import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView)


class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget演示")
        self.resize(430, 230);
        layout = QHBoxLayout()
        tablewidget = QTableWidget()    # 创建表格对象
        tablewidget.setRowCount(4)      # 设置行数
        tablewidget.setColumnCount(3)   # 设置列数
        layout.addWidget(tablewidget)
        # 设置水平label
        tablewidget.setHorizontalHeaderLabels(['姓名','年龄','籍贯'])
        nameItem = QTableWidgetItem("小明")  # 创建QTableWidgetItem对象
        tablewidget.setItem(0,0,nameItem)    # 将item放置在表格中
        ageItem = QTableWidgetItem("24")
        tablewidget.setItem(0,1,ageItem)
        jgItem = QTableWidgetItem("北京")
        tablewidget.setItem(0,2,jgItem)
        # 禁止编辑，默认表格时可以编辑的
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 整行选择，选中时只能够按照行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        tablewidget.resizeColumnsToContents()               # 调整列和行
        tablewidget.resizeRowsToContents()
        tablewidget.horizontalHeader().setVisible(False)    # 设置水平表格头不可见
        # tablewidget.verticalHeader().setVisible(False)
        tablewidget.setVerticalHeaderLabels(["a","b"])      # 设置竖直label
        tablewidget.setShowGrid(False)                      # 隐藏表格线
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TableWidgetDemo()
    example.show()
    sys.exit(app.exec_())
