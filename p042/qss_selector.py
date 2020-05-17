"""
@Time        : 2020/5/17
@Author      : KD_huhu
@File        : qss_selector
@Description : 
"""
from PyQt5.QtWidgets import *
import sys
import qdarkstyle


class QSSSelector(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS样式")
        btn1 = QPushButton(self)
        # 为按钮设置属性，可以使用选择器来选择不同的按钮
        btn1.setText("按钮1")
        btn2 = QPushButton(self)
        btn2.setProperty('name', 'btn2')
        btn2.setText("按钮2")
        btn3 = QPushButton(self)
        btn3.setProperty('name', 'btn3')
        btn3.setText("按钮3")
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QSSSelector()
    # 选择器
    # 类名[属性名] 来筛选按钮
    qssStyle = '''
        QPushButton[name="btn2"] {
            background-color:red;
            color:yellow;
            height:120;
            font-size:60px;
        }
        QPushButton[name="btn3"] {
            background-color:blue;
            color:yellow;
            height:60;
            font-size:30px;
        }
    '''
    form.setStyleSheet(qssStyle)
    form.show()
    sys.exit(app.exec_())
