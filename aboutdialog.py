# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialog.ui'
#
# Created: Fri Oct 28 18:52:53 2016
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

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName(_fromUtf8("aboutDialog"))
        aboutDialog.resize(292, 250)
        aboutDialog.setMinimumSize(QtCore.QSize(292, 250))
        aboutDialog.setMaximumSize(QtCore.QSize(292, 250))
        self.aboutOKButton = QtGui.QPushButton(aboutDialog)
        self.aboutOKButton.setGeometry(QtCore.QRect(100, 200, 101, 31))
        self.aboutOKButton.setObjectName(_fromUtf8("aboutOKButton"))
        self.textLabel = QtGui.QLabel(aboutDialog)
        self.textLabel.setGeometry(QtCore.QRect(10, 20, 271, 161))
        self.textLabel.setObjectName(_fromUtf8("textLabel"))
        self.verticalLayoutWidget = QtGui.QWidget(aboutDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 2, 2))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.retranslateUi(aboutDialog)
        QtCore.QObject.connect(self.aboutOKButton, QtCore.SIGNAL(_fromUtf8("clicked()")), aboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About", None))
        self.aboutOKButton.setText(_translate("aboutDialog", "OK", None))
        self.textLabel.setText(_translate("aboutDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">This Data Acquisition System is crated by:</span><br/></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Mohamed Lagha &amp; Ahmed Aljatlawy</span><br/></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Faculty of Engineering - Misurata University, Libya</span></p><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">2016/2017</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    aboutDialog = QtGui.QDialog()
    ui = Ui_aboutDialog()
    ui.setupUi(aboutDialog)
    aboutDialog.show()
    sys.exit(app.exec_())

