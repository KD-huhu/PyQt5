import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    win = QWidget()
    # 设置窗口的尺寸
    win.resize(600,300)
    # 移动窗口,设置窗口初始位置
    win.move(300,300)

    # 设置窗口的标题
    win.setWindowTitle('First demo！')
    # 显示窗口
    win.show()

    # 进入程序的主循环
    # 并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())