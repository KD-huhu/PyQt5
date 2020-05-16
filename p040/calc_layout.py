"""
@Time        : 2020/5/16
@Author      : KD_huhu
@File        : calc_layout
@Description : 
"""
import math, sys
from PyQt5.QtWidgets import *


class Calc(QWidget) :
    def __init__(self):
        super(Calc,self).__init__()
        self.setWindowTitle("栅格布局")
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Cls','Back','','Close',
                 '7','8','9','/',
                 '4','5','6','*',
                 '1','2','3','-',
                 '0','.','=','+']
        positions = [(i,j) for i in range(5) for j in range(4)]
        print(positions)
        # zip将多个可迭代对象合并成为一个可迭代对象
        for position,name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            # *方法可以将元组打开
            grid.addWidget(button,*position)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Calc()
    main.show()
    sys.exit(app.exec_())
