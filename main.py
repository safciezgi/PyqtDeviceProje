from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("PyqtDesign1.ui", self)
        self.connect_btn.clicked.connect(self.ConnectButtonClicked)


    def ConnectButtonClicked(self):
        print("Hello")

#main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(350)
widget.setFixedWidth(760)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Existing")
