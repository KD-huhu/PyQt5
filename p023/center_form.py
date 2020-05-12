import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterWindow(QMainWindow):
    '''
    inhrent QMainWindow
    '''
    def __init__(self):
        super(CenterWindow,self).__init__()
        # set window title
        self.setWindowTitle('My first main window!')
        # set window size
        self.resize(400,300)

    def center(self):
        # get screen coordinate system
        screen = QDesktopWidget().screenGeometry()
        # get window coordinate system
        window = self.geometry()
        # calculate the site
        new_left = (screen.width() - window.width()) / 2
        new_top = (screen.top() - window.top()) / 2
        # move the window
        self.move(new_left,new_top)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../images/Dragon.ico'))
    # Instantiation class
    main = CenterWindow()
    main.show()
    sys.exit(app.exec_())