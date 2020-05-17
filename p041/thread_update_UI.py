"""
@Time        : 2020/5/16
@Author      : KD_huhu
@File        : thread_update_UI
@Description : 
"""
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
import time
import sys


class BackendThread(QThread):
    # 定义子线程
    # 使用信号实现通信
    update_date = pyqtSignal(str)   # 创建信号
    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currentTime))     # 发出信号
            time.sleep(1)


class ThreadUpdateUI(QDialog):
    # 主进程
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('多线程更新UI数据')
        self.resize(400, 100)
        self.input = QLineEdit(self)
        self.input.resize(400, 100)
        self.initUI()
    def initUI(self):
        self.backend = BackendThread()  # 实例化线程类
        self.backend.update_date.connect(self.handleDisplay)    # 绑定槽
        self.backend.start()
    def handleDisplay(self, data):
        self.input.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = ThreadUpdateUI()
    example.show()
    sys.exit(app.exec_())
