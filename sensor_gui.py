# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver8.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys, threading, time
import serial
from PyQt4 import QtCore, QtGui

red = '192, 57, 43'
blue = '34, 167, 240'
green = '0, 177, 106'
yellow = '244, 208, 63'

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def __init__(self, Mainwindow, port):
        port = '/dev/ttyUSB' + port
        self.ser = serial.Serial(port, 115200, timeout=.1)
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.readData)
        self.timer.start(10)

        self.setupUi(MainWindow)

        self.sensorNum = 4
        self.sensorList = {
            "1": [self.sensorStatusBox_1, self.sensorMsg_1, self.sensorContainer_1],
            "2": [self.sensorStatusBox_2, self.sensorMsg_2, self.sensorContainer_2],
            "3": [self.sensorStatusBox_3, self.sensorMsg_3, self.sensorContainer_3],
            "4": [self.sensorStatusBox_4, self.sensorMsg_4, self.sensorContainer_4],
        }

    def readData(self):
        msg = self.ser.readline()
        if msg:
            print msg
            self.msg_dispatcher(msg)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(988, 650)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("#sensorMapFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: white;\n"
"}\n"
"\n"
"#idleLegendBox {\n"
"background-color: rgb(34, 167, 240);\n"
"}\n"
"\n"
"#sensingLegendBox {\n"
"background-color: rgb(0, 177, 106);\n"
"}\n"
"\n"
"#offLegendBox {\n"
"background-color: rgb(192, 57, 43);\n"
"}\n"
"\n"
"#initLegendBox {\n"
"background-color: rgb(244, 208, 63);\n"
"}\n"
"\n"
"#sensorContainer_1 {\n"
"padding: 10px;\n"
"border: 3px solid gray;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#sensorContainer_2 {\n"
"padding: 10px;\n"
"border: 3px solid gray;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#sensorContainer_3 {\n"
"padding: 10px;\n"
"border: 3px solid gray;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#sensorContainer_4 {\n"
"padding: 10px;\n"
"border: 3px solid gray;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(790, 490, 181, 101))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.btnLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.btnLayout.setObjectName(_fromUtf8("btnLayout"))
        self.initBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.initBtn.setObjectName(_fromUtf8("initBtn"))
        self.btnLayout.addWidget(self.initBtn)
        self.startBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        self.btnLayout.addWidget(self.startBtn)
        self.sensorMapFrame = QtGui.QFrame(self.centralwidget)
        self.sensorMapFrame.setGeometry(QtCore.QRect(19, 19, 731, 561))
        self.sensorMapFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sensorMapFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.sensorMapFrame.setObjectName(_fromUtf8("sensorMapFrame"))
        self.sensorContainer_1 = QtGui.QWidget(self.sensorMapFrame)
        self.sensorContainer_1.setGeometry(QtCore.QRect(100, 80, 211, 131))
        self.sensorContainer_1.setObjectName(_fromUtf8("sensorContainer_1"))
        self.sensorStatusBox_1 = QtGui.QFrame(self.sensorContainer_1)
        self.sensorStatusBox_1.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.sensorStatusBox_1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sensorStatusBox_1.setFrameShadow(QtGui.QFrame.Raised)
        self.sensorStatusBox_1.setObjectName(_fromUtf8("sensorStatusBox_1"))
        self.label = QtGui.QLabel(self.sensorContainer_1)
        self.label.setGeometry(QtCore.QRect(80, 30, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.sensorMsg_1 = QtGui.QTextEdit(self.sensorContainer_1)
        self.sensorMsg_1.setGeometry(QtCore.QRect(10, 80, 191, 41))
        self.sensorMsg_1.setObjectName(_fromUtf8("sensorMsg_1"))
        self.sensorContainer_2 = QtGui.QWidget(self.sensorMapFrame)
        self.sensorContainer_2.setGeometry(QtCore.QRect(440, 80, 211, 131))
        self.sensorContainer_2.setObjectName(_fromUtf8("sensorContainer_2"))
        self.sensorStatusBox_2 = QtGui.QFrame(self.sensorContainer_2)
        self.sensorStatusBox_2.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.sensorStatusBox_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sensorStatusBox_2.setFrameShadow(QtGui.QFrame.Raised)
        self.sensorStatusBox_2.setObjectName(_fromUtf8("sensorStatusBox_2"))
        self.label_2 = QtGui.QLabel(self.sensorContainer_2)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.sensorMsg_2 = QtGui.QTextEdit(self.sensorContainer_2)
        self.sensorMsg_2.setGeometry(QtCore.QRect(10, 80, 191, 41))
        self.sensorMsg_2.setObjectName(_fromUtf8("sensorMsg_2"))
        self.sensorContainer_3 = QtGui.QWidget(self.sensorMapFrame)
        self.sensorContainer_3.setGeometry(QtCore.QRect(100, 320, 211, 131))
        self.sensorContainer_3.setObjectName(_fromUtf8("sensorContainer_3"))
        self.sensorStatusBox_3 = QtGui.QFrame(self.sensorContainer_3)
        self.sensorStatusBox_3.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.sensorStatusBox_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sensorStatusBox_3.setFrameShadow(QtGui.QFrame.Raised)
        self.sensorStatusBox_3.setObjectName(_fromUtf8("sensorStatusBox_3"))
        self.label_3 = QtGui.QLabel(self.sensorContainer_3)
        self.label_3.setGeometry(QtCore.QRect(80, 30, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.sensorMsg_3 = QtGui.QTextEdit(self.sensorContainer_3)
        self.sensorMsg_3.setGeometry(QtCore.QRect(10, 80, 191, 41))
        self.sensorMsg_3.setObjectName(_fromUtf8("sensorMsg_3"))
        self.sensorContainer_4 = QtGui.QWidget(self.sensorMapFrame)
        self.sensorContainer_4.setGeometry(QtCore.QRect(450, 320, 211, 131))
        self.sensorContainer_4.setObjectName(_fromUtf8("sensorContainer_4"))
        self.sensorStatusBox_4 = QtGui.QFrame(self.sensorContainer_4)
        self.sensorStatusBox_4.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.sensorStatusBox_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sensorStatusBox_4.setFrameShadow(QtGui.QFrame.Raised)
        self.sensorStatusBox_4.setObjectName(_fromUtf8("sensorStatusBox_4"))
        self.label_4 = QtGui.QLabel(self.sensorContainer_4)
        self.label_4.setGeometry(QtCore.QRect(80, 30, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.sensorMsg_4 = QtGui.QTextEdit(self.sensorContainer_4)
        self.sensorMsg_4.setGeometry(QtCore.QRect(10, 80, 191, 41))
        self.sensorMsg_4.setObjectName(_fromUtf8("sensorMsg_4"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(790, 180, 131, 131))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.legendLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.legendLayout.setObjectName(_fromUtf8("legendLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.sensingLegendBox = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.sensingLegendBox.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sensingLegendBox.setFrameShadow(QtGui.QFrame.Raised)
        self.sensingLegendBox.setObjectName(_fromUtf8("sensingLegendBox"))
        self.horizontalLayout_2.addWidget(self.sensingLegendBox)
        self.sensingLagendLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.sensingLagendLabel.setObjectName(_fromUtf8("sensingLagendLabel"))
        self.horizontalLayout_2.addWidget(self.sensingLagendLabel)
        self.legendLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.offLegendBox = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.offLegendBox.setFrameShape(QtGui.QFrame.StyledPanel)
        self.offLegendBox.setFrameShadow(QtGui.QFrame.Raised)
        self.offLegendBox.setObjectName(_fromUtf8("offLegendBox"))
        self.horizontalLayout_3.addWidget(self.offLegendBox)
        self.offLegendLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.offLegendLabel.setObjectName(_fromUtf8("offLegendLabel"))
        self.horizontalLayout_3.addWidget(self.offLegendLabel)
        self.legendLayout.addLayout(self.horizontalLayout_3)
        self.syncNodeMsg = QtGui.QTextEdit(self.centralwidget)
        self.syncNodeMsg.setGeometry(QtCore.QRect(790, 320, 181, 161))
        self.syncNodeMsg.setObjectName(_fromUtf8("syncNodeMsg"))
        self.verticalLayoutWidget.raise_()
        self.sensorMapFrame.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.syncNodeMsg.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        """
        Add actions
        """
        self.startTime = time.time()

        self.initBtn.clicked.connect(self.init)
        self.startBtn.clicked.connect(self.start)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def init(self):
        # send init msg
        for num in range(self.sensorNum):
            # self.sensorList[str(num+1)][0].setStyleSheet("background-color: rgb(244, 208, 63);")
            # self.sensorList[str(num+1)][1].append("%.2f: Init button pushed." % (time.time() - self.startTime))
            pass
 
        self.statusbar.showMessage("initializing...")
        self.send_msg('a')


    def start(self):
        # send start msg
        self.statusbar.showMessage("start!")
        self.send_msg('s')

    def msg_dispatcher(self, msg):
        # parse msg
        self.syncNodeMsg.append(msg)

        if msg[0] == '1':
            self.sensorList['1'][2].setStyleSheet("#sensorContainer_1 {border: 3px solid rgb(244, 208, 63);}")
        elif msg[0] == '2':
            self.sensorList['2'][2].setStyleSheet("#sensorContainer_2 {border: 3px solid rgb(244, 208, 63);}")
        elif msg[0] == '3':
            self.sensorList['3'][2].setStyleSheet("#sensorContainer_3 {border: 3px solid rgb(244, 208, 63);}")
        elif msg[0] == '4':
            self.sensorList['4'][2].setStyleSheet("#sensorContainer_4 {border: 3px solid rgb(244, 208, 63);}")


    def send_msg(self, msg):
        if msg == 'a':
            self.ser.write(chr(97))
            self.ser.write(chr(10))
        elif msg == 's':
            self.ser.write(chr(115))
            self.ser.write(chr(10))

            self.sensorList['1'][2].setStyleSheet("#sensorContainer_1 {border: 3px solid rgb(34, 167, 240);}")
            self.sensorList['2'][2].setStyleSheet("#sensorContainer_2 {border: 3px solid rgb(34, 167, 240);}")
            self.sensorList['3'][2].setStyleSheet("#sensorContainer_3 {border: 3px solid rgb(34, 167, 240);}")
            self.sensorList['4'][2].setStyleSheet("#sensorContainer_4 {border: 3px solid rgb(34, 167, 240);}")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sensor GUI", None))
        self.initBtn.setText(_translate("MainWindow", "Init", None))
        self.startBtn.setText(_translate("MainWindow", "Start", None))
        self.label.setText(_translate("MainWindow", "Sensor 1", None))
        self.label_2.setText(_translate("MainWindow", "Sensor 2", None))
        self.label_3.setText(_translate("MainWindow", "Sensor 3", None))
        self.label_4.setText(_translate("MainWindow", "Sensor 4", None))
        self.sensingLagendLabel.setText(_translate("MainWindow", "OK", None))
        self.offLegendLabel.setText(_translate("MainWindow", "Not OK", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

if __name__ == "__main__":
    app = QtGui.QApplication([])
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow(MainWindow, '1')

    MainWindow.show()
    sys.exit(app.exec_())