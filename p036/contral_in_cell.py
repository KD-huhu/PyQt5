import sys
from PyQt5.QtWidgets import *


class PlaceControlInCell(QWidget):

    def __init__(self):
        super(PlaceControlInCell,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在单元格中放置控件")
        self.resize(430, 300);
        layout = QHBoxLayout()
        tableWidget = QTableWidget()        # 创建表格对象
        tableWidget.setRowCount(4)          # 设置行数
        tableWidget.setColumnCount(3)       # 设置列数
        layout.addWidget(tableWidget)
        # 设置表格水平label
        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])
        textItem = QTableWidgetItem('小明')
        tableWidget.setItem(0,0,textItem)   # 第一第二是item位置，第三个参数是item
        combox = QComboBox()                # 下拉列表
        combox.addItem('男')
        combox.addItem('女')
        # QSS Qt StyleSheet
        # 使用类似CSS的语法来设置控件的样式
        combox.setStyleSheet('QComboBox{margin:3px};')
        tableWidget.setCellWidget(0,1,combox)
        modifyButton = QPushButton('修改')
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton{margin:3px};')
        tableWidget.setCellWidget(0,2,modifyButton)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = PlaceControlInCell()
    example.show()
    sys.exit(app.exec_())