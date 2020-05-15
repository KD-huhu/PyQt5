import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DateTimeEdit(QWidget):
    def __init__(self):
        super(DateTimeEdit, self).__init__()
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        dateTimeEdit1 = QDateTimeEdit()                         # 创建日期对象
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))     # 设置最小日期，当前日期回退
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))      # 设置最大日期，当前日期向后
        self.dateTimeEdit = dateTimeEdit1
        dateTimeEdit2.setCalendarPopup(True)                    # 设置下拉模块
        dateEdit = QDateTimeEdit(QDate.currentDate())           # 获取日期
        timeEdit = QDateTimeEdit(QTime.currentTime())
        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd  HH:mm:ss")  # 设置显示风格
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:ss")
        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)
        vlayout.addWidget(dateTimeEdit1)
        vlayout.addWidget(dateTimeEdit2)
        vlayout.addWidget(dateEdit)
        vlayout.addWidget(timeEdit)
        self.btn = QPushButton('获取日期和时间')
        self.btn.clicked.connect(self.onButtonClick)
        vlayout.addWidget(self.btn)
        self.setLayout(vlayout)
        self.resize(300, 90)
        self.setWindowTitle("设置不同风格的日期和时间")

    def onDateChanged(self, date):          # 仅日期变化
        print(date)
    def onTimeChanged(self, time):          # 仅时间变化
        print(time)
    def onDateTimeChanged(self, datetime):  # 日期和时间变化
        print(datetime)
    def onButtonClick(self):                # 通过按钮获取设置的时间
        datetime = self.dateTimeEdit.dateTime()
        print(datetime)
        print(self.dateTimeEdit.maximumDate())      # 最大日期
        print(self.dateTimeEdit.maximumDateTime())  # 最大日期和时间
        print(self.dateTimeEdit.minimumDateTime())  # 最小日期


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DateTimeEdit()
    main.show()
    sys.exit(app.exec_())
