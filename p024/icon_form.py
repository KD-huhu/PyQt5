import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QHBoxLayout,QWidget
from PyQt5.QtGui import QIcon
import ctypes


class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口
        self.setGeometry(300,300,250,250)
        # 设置窗口的标题
        self.setWindowTitle('窗口标题设置demo')
        # 设置窗口图标
        self.setWindowIcon(QIcon('../images/Basilisk.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../images/Dragon.ico'))
    # 在任务栏显示图标
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    main = IconForm()
    main.show()
    sys.exit(app.exec_())