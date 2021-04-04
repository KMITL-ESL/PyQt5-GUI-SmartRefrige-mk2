# Page 3 By Pop  
        # waiting for comment in future

from PyQt5 import QtCore, QtGui, QtWidgets

# import Opencv module
import cv2

import os

import face_recognition 
# https://github.com/ageitgey/face_recognition

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
        self.camera_label.setGeometry(QtCore.QRect(79, 70, 640, 321))          # size of camera image            
        self.camera_label.setStyleSheet("QLabel{background-color: rgb(60, 60, 60);}")
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

        # Camera Start

        # create a timer
        self.timer = QtCore.QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.cameraFeature)
        # set control_bt callback clicked  function
        self.cancelbutton.clicked.connect(self.controlTimer)
        
        # create video capture
        self.cap = cv2.VideoCapture(0)  
        self.cap.set(3, 640)    # width # ratio 3:4
        self.cap.set(4, 480)    # height

        # start timer
        self.timer.start(20) # default is 20 milliseconds for 1 frame
        self.frame_count = 40   # how many frame to trigger 1 encoding face regconition

        # time per frame * self.frame_count = 20 * 40 = 800 millisec / 1 encoding face reg 
                                                    # can change if it to slow maybe to 500 millisec response? 
        self.process_frame_count = 0 

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.face_label.setText(_translate("MainWindow", "โปรดหันหน้าเข้าหากล้องเพื่อยืนยันตัวตน"))
        self.cancelbutton.setText(_translate("MainWindow", "ย้อนกลับ "))
        self.version_label.setText(_translate("MainWindow", "V.1.0.0  "))


    # view camera
    def cameraFeature(self):

        image = self.initCam()
        self.displayImage(image)

    def initCam(self):  # for capture and face recognition
        # read image in BGR format
        ret, image = self.cap.read()

        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Resize frame of video to 1/4 size for faster face recognition processing
        scale = 4 # 4, 10
        small_frame = cv2.resize(image, (0, 0), fx=1.0/scale, fy=1.0/scale)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        #rgb_small_frame = small_frame[:, :, ::-1]
        # Not working ^
    
        try:
            # location detect where face is ?
            face_locations = face_recognition.face_locations(small_frame)

            # optimal time of encoding because it take to long ... 
            if self.process_frame_count % self.frame_count == 0: 
                image_encoding = face_recognition.face_encodings(small_frame, face_locations)[0]    # very slow ! 
                self.process_frame_count = 0
            self.process_frame_count += 1

            # set green rectangle 
            y1, x2, y2, x1 = face_locations[0]
            cv2.rectangle(image, (x1*scale, y1*scale), (x2*scale, y2*scale), (0, 255, 0), 2)

            print('Detect New Person')
            #print('\nStart')
            #print(image_encoding)  # too slow (not recommend)
            #print('End')
        except IndexError:
            print('No Face Detection')
        except Exception as e:
            print(e)
            
        return image
    
    def displayImage(self, image):
        
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QtGui.QImage(image.data, width, height, step, QtGui.QImage.Format_RGB888)
        # show image in img_label
        self.camera_label.setPixmap(QtGui.QPixmap.fromImage(qImg))

        # incase of save pictures in folder TempPicture
        #image = face_recognition.load_image_file(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'TempPhoto', 'pic1.jpg'))


        # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if self.timer.isActive():
            # stop timer
            self.timer.stop()
            # release video capture (freeze picture)
            # self.cap.release()



