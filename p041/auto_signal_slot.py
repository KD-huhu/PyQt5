"""
@Time        : 2020/5/16
@Author      : KD_huhu
@File        : auto_signal_slot
@Description : 
"""
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys


class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot, self).__init__()
        self.okButton = QPushButton("ok", self)
        self.okButton.setObjectName("okButton")
        self.okButton1 = QPushButton("cancel", self)
        self.okButton1.setObjectName("cancelButton")
        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)
        self.resize(200, 100)
        QtCore.QMetaObject.connectSlotsByName(self)
        # 传统手动绑定槽
        # self.okButton.clicked.connect(self.on_okButton_clicked)

    # 定义该函数为槽函数
    @QtCore.pyqtSlot()
    # 定义槽函数
    def on_okButton_clicked(self):
        print("点击了ok按钮")
    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print("点击了cancel按钮")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = AutoSignalSlot()
    example.show()
    sys.exit(app.exec_())
