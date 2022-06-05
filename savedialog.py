# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'savedialog.ui'
#
# Created: Sat Jan 21 19:20:10 2017
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

class Ui_saveDialog(object):
    def setupUi(self, saveDialog):
        saveDialog.setObjectName(_fromUtf8("saveDialog"))
        saveDialog.resize(527, 285)
        saveDialog.setMinimumSize(QtCore.QSize(339, 149))
        self.label_2 = QtGui.QLabel(saveDialog)
        self.label_2.setGeometry(QtCore.QRect(90, 30, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.saveOkButton = QtGui.QPushButton(saveDialog)
        self.saveOkButton.setGeometry(QtCore.QRect(180, 230, 101, 31))
        self.saveOkButton.setObjectName(_fromUtf8("saveOkButton"))
        self.IgnoreButton = QtGui.QPushButton(saveDialog)
        self.IgnoreButton.setGeometry(QtCore.QRect(180, 70, 101, 31))
        self.IgnoreButton.setObjectName(_fromUtf8("IgnoreButton"))
        self.checkBox = QtGui.QCheckBox(saveDialog)
        self.checkBox.setGeometry(QtCore.QRect(420, 180, 99, 26))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label = QtGui.QLabel(saveDialog)
        self.label.setGeometry(QtCore.QRect(280, 140, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBox = QtGui.QSpinBox(saveDialog)
        self.spinBox.setGeometry(QtCore.QRect(280, 170, 121, 33))
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_4 = QtGui.QLabel(saveDialog)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(saveDialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 170, 161, 33))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(saveDialog)
        QtCore.QObject.connect(self.IgnoreButton, QtCore.SIGNAL(_fromUtf8("clicked()")), saveDialog.hide)
        QtCore.QObject.connect(self.saveOkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), saveDialog.hide)
        QtCore.QMetaObject.connectSlotsByName(saveDialog)

    def retranslateUi(self, saveDialog):
        saveDialog.setWindowTitle(_translate("saveDialog", "Dialog", None))
        self.label_2.setText(_translate("saveDialog", "Do you want to save this session? ", None))
        self.saveOkButton.setText(_translate("saveDialog", "OK", None))
        self.IgnoreButton.setText(_translate("saveDialog", "NO", None))
        self.checkBox.setText(_translate("saveDialog", "Unlimited", None))
        self.label.setText(_translate("saveDialog", "Number of values in each file:", None))
        self.label_4.setText(_translate("saveDialog", "Filename to save to: ", None))
        self.lineEdit.setText(_translate("saveDialog", "sessionData.txt", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    saveDialog = QtGui.QDialog()
    ui = Ui_saveDialog()
    ui.setupUi(saveDialog)
    saveDialog.show()
    sys.exit(app.exec_())

