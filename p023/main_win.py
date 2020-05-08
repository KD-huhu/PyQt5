import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon


class FirstWindow(QMainWindow):
    '''
    inhrent QMainWindow
    '''
    def __init__(self):
        super(FirstWindow,self).__init__()
        # set window title
        self.setWindowTitle('My first main window!')
        # set window size
        self.resize(400,300)
        # get statuBar
        self.statue = self.statusBar()
        # show the message lasting 5 s
        self.statue.showMessage('This wil last 5 s!',5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../images/Dragon.ico'))
    # Instantiation class
    main = FirstWindow()
    main.show()
    sys.exit(app.exec_())