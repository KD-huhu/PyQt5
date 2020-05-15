from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
import sys


class ListViewDemo(QWidget):

    def __init__(self, parent=None):
        super(ListViewDemo, self).__init__(parent)
        self.setWindowTitle("QListView 例子")
        self.resize(300, 270)
        layout = QVBoxLayout()
        listview = QListView()                  # 创建列数据对象
        listModel = QStringListModel()          # 创建列表数据源对象（为空）
        self.list = ["列表项1","列表项2", "列表项3"]
        listModel.setStringList(self.list)      # 列表数据源和数据关联
        listview.setModel(listModel)            # 列表数据源和列表对象关联
        listview.clicked.connect(self.clicked)  # 绑定槽
        layout.addWidget(listview)
        self.setLayout(layout)

    def clicked(self,item):
        QMessageBox.information(self,"QListView","您选择了：" + self.list[item.row()])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec_())
