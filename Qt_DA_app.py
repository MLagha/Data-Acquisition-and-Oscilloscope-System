from PyQt4 import QtCore, QtGui
import sys
import time
from threading import Event, Thread

from mainwindow import Ui_MainWindow
from savedialog import Ui_saveDialog
from aboutdialog import Ui_aboutDialog
from plot import Plot

from temp import Sensor_Temp

####
from PyQt4.Qt import QString, QFileDialog
####

from pylab import *

class dataAcquisition(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(dataAcquisition, self).__init__(parent)
        self.setupUi(self)

        self.startButton.clicked.connect(self.startButton_clicked)
        self.stop_request = Event()
        self.popSave = saveDialog()
        
        #self.popSave = saveDialog()
        #self.stop_request = Event()

        self.stopButton.clicked.connect(self.stopButton_clicked)

        self.startplotButton.clicked.connect(self.startplotButton_clicked)
        self.stop_request_plot = Event()
        
        self.actionAbout.triggered.connect(self.actionAbout_triggered)
        self.popAboutDialog = aboutDialog()

        self.status = False
        self.temp = Sensor_Temp()
        self.th = Thread(target = self.runValue)
        
    def runValue(self):
        Fs = 8000
        N = 256
        f = linspace(-Fs/2, Fs/2, N)
        
        ax1 = subplot(2, 1, 1)
        Line1 = plot(0,0,'r-')[0]
        
        ax2 = subplot(2, 1, 2)
        Line2 = plot(f,0*f,'r-')[0]
        
        self.status = True
        while (self.status):
            self.temp.Temp(ax1, Line1, ax2, Line2)
  
            self.lcdNumber_value.display(self.temp.Value)
            self.lcdNumber_MaxValue.display(self.temp.MaxValue)
            self.lcdNumber_MinValue.display(self.temp.MinValue)

    def gpioButton_clicked(self):
        self.popGPIO.show()

        
    def startButton_clicked(self):
        self.popSave.show()        
        self.th.start()
        
        
    def stopButton_clicked(self):
        self.status = False

    def startplotButton_clicked(self):
        self.plot = Plot(self.stop_request_plot)
        self.plot.start()  
        
    def stopplotButton_clicked(self):
        self.stop_request_plot.set()
                
    def actionAbout_triggered(self):
        self.popAboutDialog.show()

class saveDialog(QtGui.QDialog, Ui_saveDialog):
    def __init__(self, parent=None):
        super(saveDialog, self).__init__(parent)
        
        flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.setupUi(self)

        self.checkBox.stateChanged.connect(self.Unlimited_NOVs)
        
        self.saveOkButton.clicked.connect(self.acceptOKButtonClicked)
        
        self.NOVs = 0.0
        
        self.temp = Sensor_Temp()
        
    def Unlimited_NOVs (self, state):
        if state == QtCore.Qt.Checked:
            self.NOVs = 10
        else:
            ValueBox = self.spinBox
            self.NOVs = ValueBox
####

    def acceptOKButtonClicked(self):
        i = 1
        
        print self.temp.Value
        
        Name = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.text')
        self.fName = open(Name, 'w')
        i += 1 
        c = 1
        while c <= self.NOVs:
            c += 1
            self.fName.write(str(self.temp.Value))
            self.fName.write("\n")
       
        else:
            self.fName.close()



class aboutDialog(QtGui.QDialog, Ui_aboutDialog):
    def __init__(self, parent=None):
        super(aboutDialog, self).__init__(parent)
        
        flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.acceptOKButtonClicked)
        
    def acceptOKButtonClicked(self):
        self.close()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    MainWindow = dataAcquisition()
    MainWindow.show()
    sys.exit(app.exec_())