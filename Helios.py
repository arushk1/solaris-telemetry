#!/usr/bin/env python

import sys
from Tkinter import *
import time, os
import RPi.GPIO as GPIO
from random import randint
from gps import *
from time import *
import threading

mgui = Tk()
mgui.geometry("600x300")
mgui.title("Helios Suite")

gpsd = None #seting the global variable
DEBUG = 1
GPIO.setmode(GPIO.BCM)
SPICLK = 18
SPIMOSI = 24
SPIMISO = 23
SPICS = 25
        

class GUI:

    def __init__(self,mgui):        
        self.mgui = mgui
        print "First Func"
        self.initpins()
        self.createlabels()
        self.createentry()
        self.updategui()
        time.sleep(0.5)
            
        #Define Sensor and output  pins
        #Call display after defining
        #Put in loop of delay 1 sec to update values

    def initpins(self):

        print "Initialize pins"

        GPIO.setup(SPIMOSI, GPIO.OUT)
        GPIO.setup(SPIMISO, GPIO.IN)
        GPIO.setup(SPICLK, GPIO.OUT)
        GPIO.setup(SPICS, GPIO.OUT)

    def createlabels(self):

        print "Creates GUI"
            
        #Frame Information
        global frame1
        global frame2
        global frame3
        global frame4
        global frame5
        
        frame1 = Frame(mgui,bd=4,padx=2,pady=2,relief=GROOVE,width=200,height=125)
        frame2 = Frame(mgui,bd=4,padx=2,pady=2,relief=GROOVE,width=200,height=175)
        frame3 = Frame(mgui,bd=4,padx=2,pady=2,relief=GROOVE,width=200,height=125)
        frame4 = Frame(mgui,bd=4,padx=2,pady=2,relief=GROOVE,width=200,height=175)
        frame5 = Frame(mgui,bd=4,padx=2,pady=2,relief=GROOVE,width=200,height=125)
        frame6 = Frame(mgui,bd=4,padx=2,pady=2,relief=GROOVE,width=200,height=175)
        frame1.grid_propagate(0)
        frame1.grid(row=0,column=0,sticky=W)
        frame2.grid_propagate(0)
        frame2.grid(row=1,column=0,sticky=W)
        frame3.grid_propagate(0)
        frame3.grid(row=0,column=1)
        frame4.grid_propagate(0)
        frame4.grid(row=1,column=1)
        frame5.grid_propagate(0)
        frame5.grid(row=0,column=2,sticky=E)
        frame6.grid_propagate(0)
        frame6.grid(row=1,column=2,sticky=E)


        #Frame 1 Labels
        pantemp = Label(frame1,text="Panel Temperature :").grid(row=0,column=0,sticky=W)
        mottemp = Label(frame1,text="Motor Temperature :").grid(row=1,column=0,sticky=W)
        mpptemp = Label(frame1,text="MPPT Temperature :").grid(row=2,column=0,sticky=W)
        motrrpm = Label(frame1,text="Cabin Temperature :").grid(row=3,column=0,sticky=W)

        


        #Frame2 Labels

        panc = Label(frame2,text="Aux Current :").grid(row=0,column=0,sticky=W)
        motc = Label(frame2,text="Motor Current :").grid(row=1,column=0,sticky=W)
        batc = Label(frame2,text="Battery Current :").grid(row=2,column=0,sticky=W)
        panp = Label(frame2,text="MPPT 1 :").grid(row=3,column=0,sticky=W)
        motp = Label(frame2,text="MPPT 2 :").grid(row=4,column=0,sticky=W)
        batp = Label(frame2,text="MPPT 3 :").grid(row=5,column=0,sticky=W)

        
        #Frame 3 - Speedometer, to be done later

        speed = Label(frame3, text="Speed :").grid(row=0,column=0,sticky=W)
        lat = Label(frame3, text="Latitude :").grid(row=0,column=0,sticky=W)
        longitude = Label(frame3, text="Longitude :").grid(row=0,column=0,sticky=W)

        #Frame 4 - Strategy

        chglft = Label(frame4,text="Charge Left :").grid(row=0,column=0,sticky=W)
        dstleft = Label(frame4,text="Distance Left :").grid(row=1,column=0,sticky=W)
        dsttrv = Label(frame4,text="Dist Travelled :").grid(row=2,column=0,sticky=W)


        

    def createentry(self):

        
        #Initialise values
        #Using Random Values to test
        #Replace Random variables with BBB inputs
        pttxtvar = str(randint(1,20))
        mttxtvar = str(randint(1,20))
        mptxtvar = str(randint(1,20))
        mrtxtvar = str(randint(1,20))
        pttxtvar = StringVar(value=pttxtvar)
        mttxtvar = StringVar(value=mttxtvar)
        mptxtvar = StringVar(value=mptxtvar)
        mrtxtvar = StringVar(value=mrtxtvar)
        #Frame1 Values
        pttxt = Entry(frame1,bg="White",textvariable=pttxtvar).grid(row=0,column=1,sticky=W)
        mttxt = Entry(frame1,bg="White",textvariable=mttxtvar).grid(row=1,column=1,sticky=W)
        mptxt = Entry(frame1,bg="White",textvariable=mptxtvar).grid(row=2,column=1,sticky=W)
        mrtxt = Entry(frame1,bg="White",textvariable=mrtxtvar).grid(row=3,column=1,sticky=W)


        #Initialise Values

        pcsns = ""
        mcsns = ""
        bcsns = ""
        ppsns = ""
        mpcsns = ""
        bpsns = ""
        apsns = ""
        pctxtvar = StringVar(value=pcsns)
        mctxtvar = StringVar(value=mcsns)
        bctxtvar = StringVar(value=bcsns)
        pptxtvar = StringVar(value=ppsns)
        mptxtvar = StringVar(value=mpcsns)
        bptxtvar = StringVar(value=bpsns)
        aptxtvar = StringVar(value=apsns)

        #Frame2 Values

        pctxt = Entry(frame2,bg="White",textvariable=pctxtvar).grid(row=0,column=1)
        mctxt = Entry(frame2,bg="White",textvariable=mctxtvar).grid(row=1,column=1)
        bctxt = Entry(frame2,bg="White",textvariable=bctxtvar).grid(row=2,column=1)
        pptxt = Entry(frame2,bg="White",textvariable=pptxtvar).grid(row=3,column=1)
        mptxt = Entry(frame2,bg="White",textvariable=mptxtvar).grid(row=4,column=1)
        bptxt = Entry(frame2,bg="White",textvariable=bptxtvar).grid(row=5,column=1)
        aptxt = Entry(frame2,bg="White",textvariable=aptxtvar).grid(row=6,column=1)

        #Initialise Values

        clsns = ""
        dlsns = ""
        dtsns = ""
        clvar = StringVar(value=clsns)
        dlvar = StringVar(value=dlsns)
        dtvar = StringVar(value=dtsns)

        #Initialise Frame3 Values

        speedtxt = ""
        lattxt = ""
        longtxt = ""
        speedtxtvar = StringVar(value=speedtxt)
        lattxtvar = StringVar(value=lattxt)
        longtxtvar = StringVar(value=longtxt)
        
        #Frame3 Values
        
        speedtext = Entry(frame3,bg="White",textvariable=speedtxtvar).grid(row=0,column=1)
        lattext = Entry(frame3,bg="White",textvariable=lattxtvar).grid(row=1,column=1)
        longtext = Entry(frame3,bg="White",textvariable=longtxtvar).grid(row=2,column=1)
        
        #Frame4 Values

        cltxt = Entry(frame4,bg="White",textvariable=clvar).grid(row=0,column=1,sticky=W)
        dltxt = Entry(frame4,bg="White",textvariable=dlvar).grid(row=1,column=1,sticky=W)
        dttxt = Entry(frame4,bg="White",textvariable=dtvar).grid(row=2,column=1,sticky=W)
        


    def updategui(self):

        global mgui
        global gpsd

        #Frame 1

        print "Update GUI"
        pttxtvar = (readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)/1023.0)*33
        mttxtvar = (readadc(1, SPICLK, SPIMOSI, SPIMISO, SPICS)/1023.0)*33
        mptxtvar = (readadc(2, SPICLK, SPIMOSI, SPIMISO, SPICS)/1023.0)*33
        mrtxtvar = (readadc(3, SPICLK, SPIMOSI, SPIMISO, SPICS)/1023.0)*33
        pttxtvar = StringVar(value=pttxtvar)
        mttxtvar = StringVar(value=mttxtvar)
        mptxtvar = StringVar(value=mptxtvar)
        mrtxtvar = StringVar(value=mrtxtvar)
        pttxt = Entry(frame1,bg="White",textvariable=pttxtvar).grid(row=0,column=1,sticky=W)
        mttxt = Entry(frame1,bg="White",textvariable=mttxtvar).grid(row=1,column=1,sticky=W)
        mptxt = Entry(frame1,bg="White",textvariable=mptxtvar).grid(row=2,column=1,sticky=W)
        mrtxt = Entry(frame1,bg="White",textvariable=mrtxtvar).grid(row=3,column=1,sticky=W)
        print gpsd.fix.latitude
        print gpsd.fix.longitude








        
        self.mgui.after(500, self.updategui)


class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next()


def readadc(adcnum, clockpin, mosipin, misopin, cspin):
	if ((adcnum > 7) or (adcnum < 0)):
		return -1
	GPIO.output(cspin, True)

	GPIO.output(clockpin, False)  # start clock low
	GPIO.output(cspin, False)     # bring CS low

	commandout = adcnum
	commandout |= 0x18  # start bit + single-ended bit
	commandout <<= 3    # we only need to send 5 bits here
	for i in range(5):
		if (commandout & 0x80):
			GPIO.output(mosipin, True)
		else:
   			GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

	adcout = 0
	# read in one empty bit, one null bit and 10 ADC bits
	for i in range(12):
		GPIO.output(clockpin, True)
		GPIO.output(clockpin, False)
		adcout <<= 1
		if (GPIO.input(misopin)):
			adcout |= 0x1

	GPIO.output(cspin, True)

	adcout /= 2       # first bit is 'null' so drop it
	return adcout


        

    

app = GUI(mgui)
mgui.mainloop()
gpsc = GpsPoller()
gpsc.start()
