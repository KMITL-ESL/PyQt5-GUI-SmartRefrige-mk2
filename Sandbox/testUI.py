from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow): # inherit from QMainWindow
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 800, 500) # xpos, ypos, width, height
        self.setWindowTitle("SMART REFRIGERATOR MK II")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.move(50,50)
        self.label.setText("Welcome to Smart Refrige MK II")
        self.update()

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())