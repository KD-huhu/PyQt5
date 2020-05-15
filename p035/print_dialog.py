from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QFileDialog, QDialog
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrintDialog, QPrinter
import sys


class PrintDialog(QWidget):
    def __init__(self):
        super(PrintDialog, self).__init__()
        self.printer = QPrinter()  # 创建打印机对象
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('打印对话框')
        self.editor = QTextEdit(self)                   # 创建文本对象
        self.editor.setGeometry(20, 20, 300, 270)
        self.openButton = QPushButton('打开文件', self)  # 创建按钮对象
        self.openButton.move(350, 20)
        self.settingsButton = QPushButton('打印设置', self)
        self.settingsButton.move(350, 50)
        self.printButton = QPushButton('打印文档', self)
        self.printButton.move(350, 80)
        self.openButton.clicked.connect(self.openFile)  # 绑定槽
        self.settingsButton.clicked.connect(self.showSettingsDialog)
        self.printButton.clicked.connect(self.showPrintDialog)

    def openFile(self):  # 打开文件
        fname = QFileDialog.getOpenFileName(self, '打开文本文件', './')  # 打开文件对话框
        if fname[0]:
            with open(fname[0], 'r', encoding='utf-8', errors='ignore') as f:
                self.editor.setText(f.read())  # 读取文件
    def showSettingsDialog(self):                           # 显示打印设置对话框
        printDialog = QPageSetupDialog(self.printer, self)  # 创建打印设置对话框对象
        printDialog.exec()                                  # 退出
    def showPrintDialog(self):                              # 显示打印对话框
        printdialog = QPrintDialog(self.printer, self)      # 创建打印对话框
        if QDialog.Accepted == printdialog.exec():
            self.editor.print(self.printer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = PrintDialog()
    gui.show()
    sys.exit(app.exec_())