
import time
import ttk
from Tkinter import *
import sys
import glob
import serial
from Finder.Type_Definitions import column
import tkMessageBox

arduino = serial.Serial()

def serial_ports():
    """Lists serial ports

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of available serial ports
    """
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def connetti(event):
    try:
        global arduino
        arduino = serial.Serial(var.get(),9600,timeout=0)
    except (OSError, serial.SerialException):
        tkMessageBox.showerrore
        
    print("Connessione riuscita a %s ! \m/" % (var.get())) #Connesso
    StatusLabel["text"] = "Connected"
    StatusLabel["fg"] = "blue"
    PuAON["state"] = NORMAL
    PuAOff["state"] = NORMAL
    root.after(500, serialCTRL)

def ServoCTRL(servo,state):
    global arduino
    arduino.write(servo)
    arduino.write(state)
    print "Servo %s impostato a %s" % (servo,state)     
    return

def ServoCTRLPop():
    if tkMessageBox.askyesno:
        ServoCTRL('B','1')
    else:
        ServoCTRL('B','0')
  
def serialCTRL():
    print("OK")
    dati = arduino.read(1)
    if (dati=="P"):
        dati = arduino.read(1)
        if (dati !=0):
            dati2 = ord(dati)
            potValue.configure(text = dati2)
            PBar["value"] = dati2
            print(dati2)
            if (dati2 < 127):
                potValue.confiure(fg = "green")
            elif (dati2 > 127) and (dati2 < 200):
                potValue.configure(fg = "yellow")
            elif (dati2 > 200):
                potValue.configure(fg = "red")
#    root.after(300, serialCTRL)  
    
root = Tk()

var = StringVar()

#-----------GUI DESIGN--------------
#-------Here Comes The Pain---------

serialPort = serial_ports()
for name in serialPort: 
    var.set(name)

OptionMenu(root, var, *serial_ports(), command=connetti).grid(column = 1, row = 0)

label1 = Label(root)
label1.configure(text = "Serial Port", width = 10) 
label1.grid(column = 0, row = 0)

StatusLabel = Label(root)
StatusLabel.configure (text = "Disconnected", fg = "red") #Disconnesso
StatusLabel.grid(column = 2, row = 0)

quadro_servo = Frame(root,
                     borderwidth = 2,
                     relief = RIDGE,
                     height = 50,
                     bg = "orange",)
quadro_servo.grid(column = 0, row = 3)

laAct = Label(quadro_servo)
laAct.configure(text = "Servo",
                width = 10,
                background = "orange")
laAct.grid(column = 0, row = 0)

PuAON = Button(quadro_servo)
PuAON.configure(text = "Left", command= lambda: ServoCTRL('A','1'), state=DISABLED, background = "cyan") #lamba e' una magia che permette di passare i comandi alla funzione invocata
PuAON.grid(column = 0, row = 1) #Coordinate A (colonna=0 riga=1)

PuAOff = Button(quadro_servo)
PuAOff.configure(text = "Right", command = lambda: ServoCTRL('B','0'), state=DISABLED, background = "cyan")
PuAOff.grid(column = 1, row = 1) #Coordinate B (colonna=1 riga=1)

quadro_pot = Frame(root,
                     borderwidth = 2,
                     relief = RIDGE,
                     height = 50,
                     bg = "green")

quadro_pot.grid(column = 1, row = 3)
laPot = Label(quadro_pot)
laPot.configure(text = "Pot",
                width = 10,
                background = "blue",
                fg = "white")
laPot.grid(column = 0, row = 0)

potValue = Label(quadro_pot)
potValue.configure(text = "NC",
                   width = 10,
                   background = "blue",
                   fg = "white")
potValue.grid(column = 0, row = 1)


PBar = ttk.Progressbar(root, orient='horizontal', mode='determinate', max = 255)
PBar.grid(column = 2, row = 3)

root.mainloop() #lanci la finestra
