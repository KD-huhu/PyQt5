import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QColor, QFont

class CellSize(QWidget):

    def __init__(self):
        super(CellSize,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(530, 300);
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])
        tableWidget.setRowHeight(0, 150)         # 设置行高
        tableWidget.setColumnWidth(2, 300)      # 设置列宽
        tableWidget.setRowHeight(2,100)
        newItem = QTableWidgetItem('雷神')
        newItem.setFont(QFont('Times',40,QFont.Black))
        newItem.setForeground(QBrush(QColor(255,0,0)))
        tableWidget.setItem(0,0,newItem)
        newItem = QTableWidgetItem('女')
        newItem.setForeground(QBrush(QColor(255,255,0)))
        newItem.setBackground(QBrush(QColor(0,0,255)))
        tableWidget.setItem(0,1,newItem)
        newItem = QTableWidgetItem('160')
        newItem.setFont(QFont('Times',60,QFont.Black))
        newItem.setForeground(QBrush(QColor(0,0,255)))
        tableWidget.setItem(0,2,newItem)
        self.setLayout(layout)
        self.resize(500,400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = CellSize()
    example.show()
    sys.exit(app.exec_())