# pass verify advance

import sys

#For PyQt5 :
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget
from PyQt5 import QtCore, QtGui

class firstPage(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.firstBTN = QPushButton('first btn', self)
        self.firstBTN.move(50, 350)


class secondPage(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.secondBTN = QPushButton("second btn", self)
        self.secondBTN.move(100, 350)


class mainWin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        #self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(800, 480)
        self.startFirst()

    def startFirst(self):
        self.first = firstPage(self)
        self.setWindowTitle("FirstTab")
        self.setCentralWidget(self.first)
        self.first.firstBTN.clicked.connect(self.startSecond)
        self.show()

    def startSecond(self):
        self.second = secondPage(self)
        self.setWindowTitle("SecondTab")
        self.setCentralWidget(self.second)
        self.second.secondBTN.clicked.connect(self.startFirst)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainWin()
    sys.exit(app.exec_())