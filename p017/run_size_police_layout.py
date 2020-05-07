import sys
import sizepolice_demo


from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    # 创建运行程序
    app = QApplication(sys.argv)
    # 创建主窗口
    mainwindow = QMainWindow()
    ui = sizepolice_demo.Ui_MainWindow()
    # 向主窗口中添加控件
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())