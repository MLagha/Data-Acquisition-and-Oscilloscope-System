import threading
from threading import Thread

from pylab import *;

import RPi.GPIO as GPIO
import time

class Plot(Thread):
    def __init__(self, stop_request_plot):
        threading.Thread.__init__(self)
        self.stop_request_plot = stop_request_plot
        
    def run(self):
        
        GPIO.setmode(GPIO.BOARD)
        Pin = 7
        
        def RCtime (Pin):
            measurement = 0
            GPIO.setup(Pin, GPIO.OUT)
            GPIO.output(Pin, GPIO.LOW)
            time.sleep(0.0001)
    
            GPIO.setup(Pin, GPIO.IN)
    
            while (GPIO.input(Pin) == GPIO.LOW):
                measurement += 1
            return measurement


        plt.ion()
        fig=plt.figure(1)
        ax1=fig.add_subplot(111)
        l1,=ax1.plot(100,100,'r-')
    
        D=[]
        i=0.0
        while True:
            D.append((i,RCtime (Pin)))
            T=[x[0] for x in D]
            L=[x[1] for x in D]
            l1.set_xdata(T)
            l1.set_ydata(L)
            ax1.relim()
            ax1.autoscale_view()
            plt.draw()
            i+=0.10
            time.sleep(1/10.0)
            
        self.stop_request_plot.clear()