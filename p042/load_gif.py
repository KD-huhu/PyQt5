"""
@Time        : 2020/5/17
@Author      : KD_huhu
@File        : load_gif
@Description : 
"""
import sys
from PyQt5.QtWidgets import QApplication,  QLabel  ,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie


class LoadingGif(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("",self)
        self.setFixedSize(128,128)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie = QMovie('../images/loading.gif')
        # 在label标签中设置动画
        self.label.setMovie(self.movie)
        self.movie.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = LoadingGif()
    form.show()
    sys.exit(app.exec_())