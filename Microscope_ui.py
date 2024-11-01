# Form implementation generated from reading ui file 'c:\Users\camil\OneDrive\Documentos\GitHub\PyQT_functions_test\Holo_camera\Microscope.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1242, 833)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        icon = QtGui.QIcon.fromTheme("weather-clear-night")
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setDockNestingEnabled(False)
        self.main = QtWidgets.QWidget(parent=MainWindow)
        self.main.setObjectName("main")
        self.start = QtWidgets.QPushButton(parent=self.main)
        self.start.setEnabled(False)
        self.start.setGeometry(QtCore.QRect(420, 620, 151, 161))
        self.start.setObjectName("start")
        self.name1 = QtWidgets.QLabel(parent=self.main)
        self.name1.setEnabled(True)
        self.name1.setGeometry(QtCore.QRect(10, 20, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.name1.setFont(font)
        self.name1.setMouseTracking(False)
        self.name1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.name1.setObjectName("name1")
        self.name3 = QtWidgets.QLabel(parent=self.main)
        self.name3.setGeometry(QtCore.QRect(830, 20, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.name3.setFont(font)
        self.name3.setObjectName("name3")
        self.name2 = QtWidgets.QLabel(parent=self.main)
        self.name2.setGeometry(QtCore.QRect(420, 29, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.name2.setFont(font)
        self.name2.setObjectName("name2")
        self.Holoprop = QtWidgets.QGroupBox(parent=self.main)
        self.Holoprop.setGeometry(QtCore.QRect(10, 500, 391, 281))
        self.Holoprop.setObjectName("Holoprop")
        self.wavelength = QtWidgets.QLineEdit(parent=self.Holoprop)
        self.wavelength.setEnabled(False)
        self.wavelength.setGeometry(QtCore.QRect(190, 30, 113, 21))
        self.wavelength.setObjectName("wavelength")
        self.holo_size = QtWidgets.QLineEdit(parent=self.Holoprop)
        self.holo_size.setEnabled(False)
        self.holo_size.setGeometry(QtCore.QRect(190, 60, 113, 21))
        self.holo_size.setObjectName("holo_size")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.Holoprop)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.setGeometry(QtCore.QRect(200, 180, 111, 20))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.z0 = QtWidgets.QLabel(parent=self.Holoprop)
        self.z0.setGeometry(QtCore.QRect(50, 30, 141, 16))
        self.z0.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.z0.setWordWrap(False)
        self.z0.setObjectName("z0")
        self.h_holo = QtWidgets.QLabel(parent=self.Holoprop)
        self.h_holo.setGeometry(QtCore.QRect(50, 60, 141, 16))
        self.h_holo.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.h_holo.setWordWrap(False)
        self.h_holo.setObjectName("h_holo")
        self.z0_3 = QtWidgets.QLabel(parent=self.Holoprop)
        self.z0_3.setGeometry(QtCore.QRect(310, 30, 31, 16))
        self.z0_3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.z0_3.setWordWrap(False)
        self.z0_3.setObjectName("z0_3")
        self.z0_4 = QtWidgets.QLabel(parent=self.Holoprop)
        self.z0_4.setGeometry(QtCore.QRect(310, 60, 31, 16))
        self.z0_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.z0_4.setWordWrap(False)
        self.z0_4.setObjectName("z0_4")
        self.z0_6 = QtWidgets.QLabel(parent=self.Holoprop)
        self.z0_6.setGeometry(QtCore.QRect(170, 180, 31, 16))
        self.z0_6.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.z0_6.setWordWrap(False)
        self.z0_6.setObjectName("z0_6")
        self.z0_7 = QtWidgets.QLabel(parent=self.Holoprop)
        self.z0_7.setGeometry(QtCore.QRect(50, 150, 271, 16))
        self.z0_7.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.z0_7.setWordWrap(False)
        self.z0_7.setObjectName("z0_7")
        self.distance = QtWidgets.QLineEdit(parent=self.Holoprop)
        self.distance.setEnabled(False)
        self.distance.setGeometry(QtCore.QRect(190, 90, 113, 21))
        self.distance.setObjectName("distance")
        self.z0_8 = QtWidgets.QLabel(parent=self.Holoprop)
        self.z0_8.setGeometry(QtCore.QRect(310, 90, 31, 16))
        self.z0_8.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.z0_8.setWordWrap(False)
        self.z0_8.setObjectName("z0_8")
        self.z0_9 = QtWidgets.QLabel(parent=self.Holoprop)
        self.z0_9.setGeometry(QtCore.QRect(50, 90, 141, 16))
        self.z0_9.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.z0_9.setWordWrap(False)
        self.z0_9.setObjectName("z0_9")
        self.pos_value = QtWidgets.QLabel(parent=self.Holoprop)
        self.pos_value.setGeometry(QtCore.QRect(50, 180, 121, 20))
        self.pos_value.setText("")
        self.pos_value.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.pos_value.setWordWrap(False)
        self.pos_value.setObjectName("pos_value")
        self.im_resol = QtWidgets.QLineEdit(parent=self.Holoprop)
        self.im_resol.setEnabled(False)
        self.im_resol.setGeometry(QtCore.QRect(190, 120, 113, 21))
        self.im_resol.setObjectName("im_resol")
        self.z0_10 = QtWidgets.QLabel(parent=self.Holoprop)
        self.z0_10.setGeometry(QtCore.QRect(310, 120, 31, 16))
        self.z0_10.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.z0_10.setWordWrap(False)
        self.z0_10.setObjectName("z0_10")
        self.z0_11 = QtWidgets.QLabel(parent=self.Holoprop)
        self.z0_11.setGeometry(QtCore.QRect(50, 120, 141, 16))
        self.z0_11.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.z0_11.setWordWrap(False)
        self.z0_11.setObjectName("z0_11")
        self.savePhoto = QtWidgets.QPushButton(parent=self.main)
        self.savePhoto.setEnabled(False)
        self.savePhoto.setGeometry(QtCore.QRect(750, 620, 151, 161))
        self.savePhoto.setObjectName("savePhoto")
        self.raw_image = QtWidgets.QLabel(parent=self.main)
        self.raw_image.setEnabled(True)
        self.raw_image.setGeometry(QtCore.QRect(10, 80, 400, 400))
        self.raw_image.setLineWidth(1)
        self.raw_image.setText("")
        self.raw_image.setObjectName("raw_image")
        self.im_amp = QtWidgets.QLabel(parent=self.main)
        self.im_amp.setGeometry(QtCore.QRect(420, 80, 400, 400))
        self.im_amp.setText("")
        self.im_amp.setScaledContents(False)
        self.im_amp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.im_amp.setWordWrap(False)
        self.im_amp.setObjectName("im_amp")
        self.im_ph = QtWidgets.QLabel(parent=self.main)
        self.im_ph.setGeometry(QtCore.QRect(830, 80, 400, 400))
        self.im_ph.setText("")
        self.im_ph.setObjectName("im_ph")
        self.stop = QtWidgets.QPushButton(parent=self.main)
        self.stop.setEnabled(False)
        self.stop.setGeometry(QtCore.QRect(580, 620, 151, 161))
        self.stop.setObjectName("stop")
        self.startRec = QtWidgets.QPushButton(parent=self.main)
        self.startRec.setEnabled(False)
        self.startRec.setGeometry(QtCore.QRect(910, 680, 141, 101))
        self.startRec.setObjectName("startRec")
        self.time = QtWidgets.QLabel(parent=self.main)
        self.time.setGeometry(QtCore.QRect(1030, 610, 171, 31))
        self.time.setText("")
        self.time.setObjectName("time")
        self.stopRec = QtWidgets.QPushButton(parent=self.main)
        self.stopRec.setEnabled(False)
        self.stopRec.setGeometry(QtCore.QRect(1060, 680, 141, 101))
        self.stopRec.setObjectName("stopRec")
        self.time_label = QtWidgets.QLabel(parent=self.main)
        self.time_label.setGeometry(QtCore.QRect(910, 610, 101, 31))
        self.time_label.setObjectName("time_label")
        self.name_video = QtWidgets.QLineEdit(parent=self.main)
        self.name_video.setGeometry(QtCore.QRect(1030, 550, 171, 21))
        self.name_video.setObjectName("name_video")
        self.time_label_2 = QtWidgets.QLabel(parent=self.main)
        self.time_label_2.setGeometry(QtCore.QRect(910, 550, 101, 21))
        self.time_label_2.setObjectName("time_label_2")
        self.fps = QtWidgets.QLineEdit(parent=self.main)
        self.fps.setGeometry(QtCore.QRect(1030, 580, 171, 21))
        self.fps.setObjectName("fps")
        self.time_label_3 = QtWidgets.QLabel(parent=self.main)
        self.time_label_3.setGeometry(QtCore.QRect(910, 580, 101, 21))
        self.time_label_3.setObjectName("time_label_3")
        self.connectCam = QtWidgets.QPushButton(parent=self.main)
        self.connectCam.setGeometry(QtCore.QRect(420, 510, 151, 61))
        self.connectCam.setObjectName("connectCam")
        self.cam_number = QtWidgets.QLineEdit(parent=self.main)
        self.cam_number.setGeometry(QtCore.QRect(630, 530, 171, 21))
        self.cam_number.setObjectName("cam_number")
        self.time_label_4 = QtWidgets.QLabel(parent=self.main)
        self.time_label_4.setGeometry(QtCore.QRect(590, 530, 51, 21))
        self.time_label_4.setObjectName("time_label_4")
        MainWindow.setCentralWidget(self.main)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1242, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hologram miscrocopy"))
        self.start.setText(_translate("MainWindow", "Preview"))
        self.name1.setText(_translate("MainWindow", "Image RAW"))
        self.name3.setText(_translate("MainWindow", "Phase reconstruction"))
        self.name2.setText(_translate("MainWindow", "Amplitude reconstruction"))
        self.Holoprop.setTitle(_translate("MainWindow", "Hologram parameters"))
        self.wavelength.setText(_translate("MainWindow", "405"))
        self.holo_size.setText(_translate("MainWindow", "6"))
        self.z0.setText(_translate("MainWindow", "Wavelength"))
        self.h_holo.setText(_translate("MainWindow", "Hologram size"))
        self.z0_3.setText(_translate("MainWindow", "nm"))
        self.z0_4.setText(_translate("MainWindow", "mm"))
        self.z0_6.setText(_translate("MainWindow", "um"))
        self.z0_7.setText(_translate("MainWindow", "Soft Distance (from 0.635 to 0.645 mm)"))
        self.distance.setText(_translate("MainWindow", "15"))
        self.z0_8.setText(_translate("MainWindow", "mm"))
        self.z0_9.setText(_translate("MainWindow", "Distance from detector"))
        self.im_resol.setText(_translate("MainWindow", "720"))
        self.z0_10.setText(_translate("MainWindow", "px"))
        self.z0_11.setText(_translate("MainWindow", "Image resolution"))
        self.savePhoto.setText(_translate("MainWindow", "Save frame"))
        self.stop.setText(_translate("MainWindow", "Stop preview"))
        self.startRec.setText(_translate("MainWindow", "Start Record"))
        self.stopRec.setText(_translate("MainWindow", "Stop and Save"))
        self.time_label.setText(_translate("MainWindow", "Frames saved:"))
        self.name_video.setText(_translate("MainWindow", "Video_01"))
        self.time_label_2.setText(_translate("MainWindow", "File name"))
        self.fps.setText(_translate("MainWindow", "20"))
        self.time_label_3.setText(_translate("MainWindow", "Frames per second"))
        self.connectCam.setText(_translate("MainWindow", "Connect camera"))
        self.cam_number.setText(_translate("MainWindow", "0"))
        self.time_label_4.setText(_translate("MainWindow", "USB"))
