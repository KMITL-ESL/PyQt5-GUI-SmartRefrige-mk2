# Page 2 By Pop  
        # waiting for comment in future

from PyQt5 import QtCore, QtGui, QtWidgets


class Page2_ChooseBottles(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.bg_label = QtWidgets.QLabel(self)
        self.bg_label.setEnabled(True)
        self.bg_label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.bg_label.setMinimumSize(QtCore.QSize(800, 480))
        self.bg_label.setMaximumSize(QtCore.QSize(800, 480))
        self.bg_label.setText("")
        self.bg_label.setPixmap(QtGui.QPixmap("QT_resource/bgsky.jpg"))
        self.bg_label.setScaledContents(True)
        self.bg_label.setObjectName("bg_label")

        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.AddStuff_label = QtWidgets.QLabel(self)
        self.AddStuff_label.setGeometry(QtCore.QRect(90, 10, 618, 47))
        self.AddStuff_label.setFont(font)
        self.AddStuff_label.setAutoFillBackground(False)
        self.AddStuff_label.setStyleSheet("QLabel{color: rgb(0, 0, 127);}")
        self.AddStuff_label.setScaledContents(False)
        self.AddStuff_label.setAlignment(QtCore.Qt.AlignCenter)
        self.AddStuff_label.setObjectName("AddStuff_label")

        self.bottle_label = QtWidgets.QLabel(self)
        self.bottle_label.setGeometry(QtCore.QRect(330, 150, 131, 131))
        self.bottle_label.setText("")
        self.bottle_label.setPixmap(QtGui.QPixmap("QT_resource/water.png"))
        self.bottle_label.setScaledContents(True)
        self.bottle_label.setObjectName("bottle_label")

        self.whitebg_label = QtWidgets.QLabel(self)
        self.whitebg_label.setGeometry(QtCore.QRect(60, 70, 671, 331))
        self.whitebg_label.setStyleSheet("QLabel{background-color: rgb(255, 255, 255);}")
        self.whitebg_label.setText("")
        self.whitebg_label.setObjectName("whitebg_label")

        self.horizontalScrollBar = QtWidgets.QScrollBar(self)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(70, 380, 651, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")

        self.digitWidget = QtWidgets.QWidget(self)
        self.digitWidget.setGeometry(QtCore.QRect(290, 300, 221, 55))
        self.digitWidget.setObjectName("digitWidget")

        # horizontal Layout Start
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.minusbutton = QtWidgets.QPushButton(self.digitWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minusbutton.sizePolicy().hasHeightForWidth())
        self.minusbutton.setSizePolicy(sizePolicy)
        self.minusbutton.setFont(font)
        self.minusbutton.setStyleSheet("background-color: rgb(232, 232, 232); color: rgb(59, 59, 59)")
        self.minusbutton.setObjectName("minusbutton")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.digitWidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(80, 0))
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.plusbutton = QtWidgets.QPushButton(self.digitWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusbutton.sizePolicy().hasHeightForWidth())
        self.plusbutton.setSizePolicy(sizePolicy)
        self.plusbutton.setFont(font)
        self.plusbutton.setStyleSheet("background-color: rgb(9, 115, 227);color: rgb(255, 255, 255);")
        self.plusbutton.setObjectName("plusbutton")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.digitWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.minusbutton)
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.horizontalLayout.addWidget(self.plusbutton)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        # horizontal Layout End
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.waterbrand_label = QtWidgets.QLabel(self)
        self.waterbrand_label.setGeometry(QtCore.QRect(330, 100, 111, 32))
        self.waterbrand_label.setFont(font)
        self.waterbrand_label.setAutoFillBackground(False)
        self.waterbrand_label.setStyleSheet("QLabel{color: rgb(0, 0, 127);}")
        self.waterbrand_label.setScaledContents(False)
        self.waterbrand_label.setAlignment(QtCore.Qt.AlignCenter)
        self.waterbrand_label.setObjectName("waterbrand_label")
       
        self.subbg_label = QtWidgets.QLabel(self)
        self.subbg_label.setGeometry(QtCore.QRect(250, 80, 301, 291))
        self.subbg_label.setStyleSheet("QLabel{background-color: rgba(85, 170, 255, 100);}")
        self.subbg_label.setText("")
        self.subbg_label.setObjectName("subbg_label")
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.nextpagebutton = QtWidgets.QPushButton(self)
        self.nextpagebutton.setGeometry(QtCore.QRect(330, 410, 150, 60))
        self.nextpagebutton.setFont(font)
        self.nextpagebutton.setStyleSheet("background-color: rgb(9, 115, 227); color: rgb(255, 255, 255);")
        self.nextpagebutton.setObjectName("nextpagebutton")
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.version_label = QtWidgets.QLabel(self)
        self.version_label.setGeometry(QtCore.QRect(717, 440, 81, 41))
        self.version_label.setFont(font)
        self.version_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.version_label.setStyleSheet("")
        self.version_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version_label.setObjectName("version_label")
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.waterbrand_label_5 = QtWidgets.QLabel(self)
        self.waterbrand_label_5.setGeometry(QtCore.QRect(430, 90, 41, 51))
        self.waterbrand_label_5.setFont(font)
        self.waterbrand_label_5.setAutoFillBackground(False)
        self.waterbrand_label_5.setStyleSheet("QLabel{color: rgb(0, 0, 127);}")
        self.waterbrand_label_5.setScaledContents(False)
        self.waterbrand_label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.waterbrand_label_5.setObjectName("waterbrand_label_5")

        self.bg_label.raise_()
        self.whitebg_label.raise_()
        self.subbg_label.raise_()
        self.AddStuff_label.raise_()
        self.horizontalScrollBar.raise_()
        self.digitWidget.raise_()
        self.waterbrand_label.raise_()
        self.nextpagebutton.raise_()
        self.version_label.raise_()
        self.waterbrand_label_5.raise_()
        self.bottle_label.raise_()
        
        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AddStuff_label.setText(_translate("MainWindow", "เพิ่มจำนวนสินค้าที่ท่านต้องการ"))
        self.minusbutton.setText(_translate("MainWindow", "-"))
        self.plusbutton.setText(_translate("MainWindow", "+"))
        self.waterbrand_label.setText(_translate("MainWindow", "น้ำดื่ม"))
        self.nextpagebutton.setText(_translate("MainWindow", "ยืนยัน"))
        self.version_label.setText(_translate("MainWindow", "V.1.0.0  "))
        self.waterbrand_label_5.setText(_translate("MainWindow", "฿5 "))

