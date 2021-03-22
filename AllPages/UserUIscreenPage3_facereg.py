# Page 3 By Pop  
        # waiting for comment in future

from PyQt5 import QtCore, QtGui, QtWidgets


class Page3_FaceReg(QtWidgets.QWidget):
    
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
        self.face_label = QtWidgets.QLabel(self)
        self.face_label.setGeometry(QtCore.QRect(90, 10, 618, 47))
        self.face_label.setFont(font)
        self.face_label.setAutoFillBackground(False)
        self.face_label.setStyleSheet("QLabel{color: rgb(0, 0, 127);}")
        self.face_label.setScaledContents(False)
        self.face_label.setAlignment(QtCore.Qt.AlignCenter)
        self.face_label.setObjectName("face_label")

        self.camera_label = QtWidgets.QLabel(self)
        self.camera_label.setGeometry(QtCore.QRect(60, 70, 681, 321))
        self.camera_label.setStyleSheet("QLabel{background-color: rgb(255, 255, 255);}")
        self.camera_label.setText("")
        self.camera_label.setObjectName("camera_label")
        
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.cancelbutton = QtWidgets.QPushButton(self)
        self.cancelbutton.setGeometry(QtCore.QRect(330, 410, 150, 60))
        self.cancelbutton.setFont(font)
        self.cancelbutton.setStyleSheet("background-color: rgb(232, 232, 232); color: rgb(59, 59, 59);")
        self.cancelbutton.setObjectName("cancelbutton")
        
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

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.face_label.setText(_translate("MainWindow", "โปรดหันหน้าเข้าหากล้องเพื่อยืนยันตัวตน"))
        self.cancelbutton.setText(_translate("MainWindow", "ย้อนกลับ "))
        self.version_label.setText(_translate("MainWindow", "V.1.0.0  "))

