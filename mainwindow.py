# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jan 20 19:46:54 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))
        MainWindow.setMaximumSize(QtCore.QSize(700, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gpioButton = QtGui.QToolButton(self.centralwidget)
        self.gpioButton.setGeometry(QtCore.QRect(40, 110, 181, 61))
        self.gpioButton.setObjectName(_fromUtf8("gpioButton"))
        self.procButton = QtGui.QPushButton(self.centralwidget)
        self.procButton.setGeometry(QtCore.QRect(40, 190, 181, 61))
        self.procButton.setObjectName(_fromUtf8("procButton"))
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(380, 190, 131, 51))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 20, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setEnabled(True)
        self.saveButton.setGeometry(QtCore.QRect(20, 430, 211, 31))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.startplotButton = QtGui.QPushButton(self.centralwidget)
        self.startplotButton.setEnabled(True)
        self.startplotButton.setGeometry(QtCore.QRect(340, 420, 131, 51))
        self.startplotButton.setObjectName(_fromUtf8("startplotButton"))
        self.stopplotButton = QtGui.QPushButton(self.centralwidget)
        self.stopplotButton.setEnabled(True)
        self.stopplotButton.setGeometry(QtCore.QRect(530, 420, 131, 51))
        self.stopplotButton.setObjectName(_fromUtf8("stopplotButton"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(380, 120, 131, 51))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.lcdNumber_value = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_value.setGeometry(QtCore.QRect(580, 160, 64, 23))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber_value.setFont(font)
        self.lcdNumber_value.setObjectName(_fromUtf8("lcdNumber_value"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 200, 67, 21))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.lcdNumber_MaxValue = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_MaxValue.setGeometry(QtCore.QRect(580, 230, 64, 23))
        self.lcdNumber_MaxValue.setObjectName(_fromUtf8("lcdNumber_MaxValue"))
        self.lcdNumber_MinValue = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_MinValue.setGeometry(QtCore.QRect(580, 280, 64, 23))
        self.lcdNumber_MinValue.setObjectName(_fromUtf8("lcdNumber_MinValue"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Acquisition System", None))
        self.gpioButton.setText(_translate("MainWindow", "GPIO Number of inputs", None))
        self.procButton.setText(_translate("MainWindow", "Processing", None))
        self.stopButton.setText(_translate("MainWindow", "Stop Acquiring", None))
        self.label_2.setText(_translate("MainWindow", "Data Acquisition System", None))
        self.saveButton.setText(_translate("MainWindow", "Save this session\'s data", None))
        self.startplotButton.setText(_translate("MainWindow", "Start Live Plot", None))
        self.stopplotButton.setText(_translate("MainWindow", "Stop Live Plot", None))
        self.startButton.setText(_translate("MainWindow", "Start Acquiring", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionAbout.setText(_translate("MainWindow", "About Data Acquisition System", None))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About Data Acquisition System", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

