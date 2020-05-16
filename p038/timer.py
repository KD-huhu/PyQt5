"""
@Time        : 2020/5/16
@Author      : DELL
@File        : timer
@Description : 
"""
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime
import sys


class ShowTime(QWidget):

    def __init__(self, parent=None):
        super(ShowTime, self).__init__(parent)
        self.setWindowTitle("动态显示当前时间")
        self.label = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')    # 开启定时器按钮
        self.endBtn = QPushButton('结束')      # 定制定时器按你牛
        layout= QGridLayout()                 # 使用网格布局
        self.timer = QTimer()                 # 创建定时器对象
        self.timer.timeout.connect(self.showTime)
        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)
        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.setLayout(layout)
        self.resize(400,300)

    def showTime(self):
        time = QDateTime.currentDateTime()  # 获取当前时间
        # 格式化时间
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)
    def startTimer(self):
        self.timer.start(1000)              # 开始定时，参数为定时时间间隔
        self.startBtn.setEnabled(False)     # 设置开始按钮不可用
        self.endBtn.setEnabled(True)        # 设置停止按钮可用
    def endTimer(self):
        self.timer.stop()                   # 结束定时
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ShowTime()
    form.show()
    sys.exit(app.exec_())