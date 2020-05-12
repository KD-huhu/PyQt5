import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QHBoxLayout,QWidget


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('quit_app')

        # add push button
        self.button1 = QPushButton('Quit APP')
        # Associate signal with slot
        self.button1.clicked.connect(self.ButtonOnClick)

        # set layout form
        layout = QHBoxLayout()
        # add button1 to the layout
        layout.addWidget(self.button1)

        # creat new frame
        mainframe = QWidget()
        # add my layout to the frame
        mainframe.setLayout(layout)

        self.setCentralWidget(mainframe)


    # Custom slot
    # Button click event method
    def ButtonOnClick(self):
        sender = self.sender()
        print(sender.text() + ' button is clicked!')
        app = QApplication.instance()
        # quit app
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())