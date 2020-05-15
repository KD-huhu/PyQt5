import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QBrush


class DataLocation(QWidget):

    def __init__(self):
        super(DataLocation,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(600, 800);
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(40)
        tableWidget.setColumnCount(4)
        layout.addWidget(tableWidget)
        for i in range(40):             # 在表格中添加数据
            for j in range(4):
                itemContent = '(%d,%d)' %(i,j)
                tableWidget.setItem(i,j,QTableWidgetItem(itemContent))
        self.setLayout(layout)
        text = '(13'                     # 搜索满足条件的Cell
        # 第三个参数为匹配的方式，有多种匹配方式可选
        items = tableWidget.findItems(text,QtCore.Qt.MatchStartsWith)
        if len(items) > 0:
            item = items[0]
            item.setBackground(QBrush(QColor(0,255,0))) # 设置背景颜色
            item.setForeground(QBrush(QColor(255,0,0))) # 设置字体颜色
            row = item.row()                            # 获得元素行数
            # 定位到指定的行，滚动条滚动到对应位置
            tableWidget.verticalScrollBar().setSliderPosition(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = DataLocation()
    example.show()
    sys.exit(app.exec_())


