import sys

#For PyQt5 :
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget
from PyQt5 import QtCore, QtGui

from AllPages.UserUIscreenPage1_home import Page1_WelcomeScreen 
from AllPages.UserUIscreenPage2_choosebottles import Page2_ChooseBottles
from AllPages.UserUIscreenPage3_facereg import Page3_FaceReg
from AllPages.UserUIscreenPage4_inforeceipt import Page4_InfoReceipt
from AllPages.UserUIscreenPage5_ensure import Page5_Ensure
from AllPages.UserUIscreenPage6_success import Page6_Success


class mainWin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        #self.setGeometry(50, 50, 400, 450)
        #self.setObjectName("MainWindow") # big MainWindow
        self.setFixedSize(800, 480)
        self.startFirst()

    def startFirst(self):
        self.firstPage = Page1_WelcomeScreen(self)
        self.setWindowTitle("Welcome Screen")

        # CentralWidget
        self.setCentralWidget(self.firstPage)

        # Go to next page if click
        self.firstPage.button1.clicked.connect(self.startSecond)
        self.show()

    def startSecond(self):
        self.secondPage = Page2_ChooseBottles(self)
        self.setWindowTitle("Choose Bottles")
        
        # CentralWidget
        self.setCentralWidget(self.secondPage)

        # Go to next page if click
        self.secondPage.nextpagebutton.clicked.connect(self.startThird)
        self.show()

    def startThird(self):
        self.thirdPage = Page3_FaceReg(self)
        self.setWindowTitle("Face Recognition")

        # CentralWidget
        self.setCentralWidget(self.thirdPage)

        # Go to previous page if click
        #self.thirdPage.cancelbutton.clicked.connect(self.startSecond)
        
        # Go to next page if face detection is valid  
        pass # working on it..
        
        #test go to page 4
        self.thirdPage.cancelbutton.clicked.connect(self.startFourth)
        
        self.show()

    def startFourth(self):
        self.fourthPage = Page4_InfoReceipt(self)
        self.setWindowTitle("Infomation Receipt")
        
        # CentralWidget
        self.setCentralWidget(self.fourthPage)

        # Go to previous page if click
        self.fourthPage.cancelbutton.clicked.connect(self.startThird)
        # Go to next page if click
        self.fourthPage.nextpagebutton.clicked.connect(self.startFifth)
        self.show()

    def startFifth(self):
        self.fifthPage = Page5_Ensure(self)
        self.setWindowTitle("Infomation Receipt")
        
        # CentralWidget
        self.setCentralWidget(self.fifthPage)

        # Go to previous page if click
        self.fifthPage.cancelbutton.clicked.connect(self.startFourth)
        # Go to next page if click
        self.fifthPage.nextpagebutton.clicked.connect(self.startSixth)
        self.show()

    def startSixth(self):
        self.sixthPage = Page6_Success(self)
        self.setWindowTitle("Success")
        
        # CentralWidget
        self.setCentralWidget(self.sixthPage)

        # Go to next page if click
        self.sixthPage.nextpagebutton.clicked.connect(self.startFirst)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainWin()
    sys.exit(app.exec_())