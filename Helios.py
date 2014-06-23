import sys
from Tkinter import *
import time
import threading
from multiprocessing import Process
#import Adafruit_BBIO.GPIO as GPIO
#import Adafruit_BBIO.ADC as ADC
from random import randint

mgui = Tk()
mgui.geometry("600x300")
mgui.title("Helios Suite")
    
class GUI:

    def __init__(self,mgui):        
        self.mgui = mgui
        print "First Func"
        self.createlabels()
        self.createentry()
        self.initpins()
        self.updategui()
        time.sleep(0.5)
            
        #Define Sensor and output  pins
        #Call display after defining
        #Put in loop of delay 1 sec to update values

    def initpins(self):

        print "Initialize pins"

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
        motrrpm = Label(frame1,text="Motor RPM :").grid(row=3,column=0,sticky=W)

        


        #Frame2 Labels

        panc = Label(frame2,text="Panel Current :").grid(row=0,column=0,sticky=W)
        motc = Label(frame2,text="Motor Current :").grid(row=1,column=0,sticky=W)
        batc = Label(frame2,text="Battery Current :").grid(row=2,column=0,sticky=W)
        panp = Label(frame2,text="Panel Power :").grid(row=3,column=0,sticky=W)
        motp = Label(frame2,text="Motor Power :").grid(row=4,column=0,sticky=W)
        batp = Label(frame2,text="Battery Power :").grid(row=5,column=0,sticky=W)
        auxp = Label(frame2,text="Aux Power :").grid(row=6,column=0,sticky=W)

        
        #Frame 3 - Speedometer, to be done later

        #Frame 4 - Strategy

        chglft = Label(frame4,text="Charge Left :").grid(row=0,column=0,sticky=W)
        dstleft = Label(frame4,text="Distance Left :").grid(row=1,column=0,sticky=W)
        dsttrv = Label(frame4,text="Dist Travelled :").grid(row=2,column=0,sticky=W)

        #Sensor Pins
        #Allot values of sensor pins to different variables and display thier data in the GUI    
        #pantemppin = "P9_40"
        #ADC.setup()
        #pttxtvar = ((ADC.read(pantemppin)*1800)-500)/10


        

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

        #Frame4 Values

        cltxt = Entry(frame4,bg="White",textvariable=clvar).grid(row=0,column=1,sticky=W)
        dltxt = Entry(frame4,bg="White",textvariable=dlvar).grid(row=1,column=1,sticky=W)
        dttxt = Entry(frame4,bg="White",textvariable=dtvar).grid(row=2,column=1,sticky=W)

        #Sensor Pins
        #Allot values of sensor pins to different variables and display thier data in the GUI    
        #pantemppin = "P9_40"
        #ADC.setup()
        #pttxtvar = ((ADC.read(pantemppin)*1800)-500)/10
        


    def updategui(self):

        global mgui

        print "Update GUI"
        pttxtvar = str(randint(1,20))
        mttxtvar = str(randint(1,20))
        mptxtvar = str(randint(1,20))
        mrtxtvar = str(randint(1,20))
        pttxtvar = StringVar(value=pttxtvar)
        mttxtvar = StringVar(value=mttxtvar)
        mptxtvar = StringVar(value=mptxtvar)
        mrtxtvar = StringVar(value=mrtxtvar)
        pttxt = Entry(frame1,bg="White",textvariable=pttxtvar).grid(row=0,column=1,sticky=W)
        mttxt = Entry(frame1,bg="White",textvariable=mttxtvar).grid(row=1,column=1,sticky=W)
        mptxt = Entry(frame1,bg="White",textvariable=mptxtvar).grid(row=2,column=1,sticky=W)
        mrtxt = Entry(frame1,bg="White",textvariable=mrtxtvar).grid(row=3,column=1,sticky=W)
        self.mgui.after(500, self.updategui)


class toggles:

    def __init__(self,mgui):
        
        frame5 = Frame(mgui,bd=4,padx=2,pady=2,relief=GROOVE,width=200,height=125)
        frame5.grid_propagate(0)
        frame5.grid(row=0,column=2)

        
        #Frame 5 Labels

        auxfan = Label(frame5,text="Aux Fan :").grid(row=0,column=0,stick=W)
        mpptfan = Label(frame5,text="MPPT Fan :").grid(row=1,column=0,stick=W)
        pancool = Label(frame5,text="Panel Cooling :").grid(row=2,column=0,stick=W)
        driverfan = Label(frame5,text="Driver Fan :").grid(row=3,column=0,stick=W)

        #Frame 5 Check boxes
        auxvar = IntVar()
        mpptvar = IntVar()
        panvar = IntVar()
        drivervar = IntVar()
        auxcheck = Checkbutton(frame5, text="Toggle", variable=auxvar).grid(row=0,column=1)
        mpptcheck = Checkbutton(frame5, text="Toggle", variable=mpptvar).grid(row=1,column=1)
        pancheck = Checkbutton(frame5, text="Toggle", variable=panvar).grid(row=2,column=1)
        drivercheck = Checkbutton(frame5, text="Toggle", variable=drivervar).grid(row=3,column=1)
        
        #Allot Values of Checkbox variables to Outputs on BeagleBone to turn them on and off via relays.
        #Add fields for Frame 6. Suggest some.

        

    

app = GUI(mgui)
mgui.mainloop()
