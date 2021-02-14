from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 800, 500) # xpos, ypos, width, height
    win.setWindowTitle("Smart Refrige MK 2")

    win.show()
    sys.exit(app.exec_())

window()