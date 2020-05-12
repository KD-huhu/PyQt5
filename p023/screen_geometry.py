import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QHBoxLayout,QWidget

def ButtonOnClick():
    print('Button clicked!')

    # print("widget.x() = %d" % widget.x())             # window abscissa
    # print("widget.y() = %d" % widget.y())             # window ordinate
    # print("widget.width() = %d" % widget.width())     # Workspace width
    # print("widget.height() = %d" % widget.height())   # Workspace heignt
    '''
    widget.x() = 260
    widget.y() = 200
    widget.width() = 300
    widget.height() = 240
    '''

    # print("widget.geometry().x() = %d" % widget.geometry().x())             # Workspace abscissa
    # print("widget.geometry().y() = %d" % widget.geometry().y())             # Workspace ordinate
    # print("widget.geometry().width() = %d" % widget.geometry().width())     # Workspace width
    # print("widget.geometry().height() = %d" % widget.geometry().height())   # Workspace heignt
    '''
    widget.geometry().x() = 261
    widget.geometry().y() = 238
    widget.geometry().width() = 300
    widget.geometry().height() = 240
    '''
    print("widget.frameGeometry().x() = %d" % widget.frameGeometry().x())           # window abscissa
    print("widget.frameGeometry().y() = %d" % widget.frameGeometry().y())           # window ordinate
    print("widget.frameGeometry().width() = %d" % widget.frameGeometry().width() )  # window width
    print("widget.frameGeometry().height() = %d" % widget.frameGeometry().height()) # window heignt


app = QApplication(sys.argv)

widget = QWidget()
button = QPushButton(widget)
button.setText('Push')
button.clicked.connect(ButtonOnClick)

# set function erea size
widget.resize(300,240)
widget.move(260,200)
widget.setWindowTitle('Geometry')

button.move(130,110)

widget.show()
sys.exit(app.exec_())