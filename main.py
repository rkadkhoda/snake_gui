import serial
import time
import serial.tools.list_ports as ports
from tkinter import *
com_ports = list(ports.comports()) # create a list of com ['COM1','COM2']
com_list=[]
for i in com_ports:
    print(i) # returns 'COMx'
    com_list.append(i.device)  # returns 'COMx'


LEFTcounter=0
RIGHTcounter=0
UPcounter=0
DOWNcounter=0

def com_selector(mailbox):
    global selected_com
    selected_com=mailbox[0]
    print(selected_com)
def btn_pushed_LEFT():
    print("LEFT clicked")
    global LEFTcounter
    LEFTcounter += 1
    LEFTbutton.configure(text="LEFT {} ".format(LEFTcounter))
    ser = serial.Serial(port=selected_com,baudrate = 9600, timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
    ser.write(('1').encode())
    ser.close()

def btn_pushed_RIGHT():
    print("RIGHT clicked")
    global RIGHTcounter
    RIGHTcounter += 1
    RIGHTbutton.configure(text="RIGHT {} ".format(RIGHTcounter))
    ser = serial.Serial(port=selected_com,baudrate = 9600, timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
    ser.write(('2').encode())
    ser.close()

def btn_pushed_UP():
    print("UP clicked")
    global UPcounter
    UPcounter += 1
    UPbutton.configure(text="UP {} ".format(UPcounter))
    ser = serial.Serial(port=selected_com,baudrate = 9600, timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
    ser.write(('3').encode())
    ser.close()


def btn_pushed_DOWN():
    print("DOWN clicked")
    global DOWNcounter
    DOWNcounter += 1
    DOWNbutton.configure(text="DOWN {} ".format(DOWNcounter))
    ser = serial.Serial(port=selected_com,baudrate = 9600, timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
    ser.write(('4').encode())
    ser.close()

def btn_pushed_LEFTT(event):
    print("LEFT clicked")
    global LEFTcounter
    LEFTcounter += 1
    LEFTbutton.configure(text="LEFT {} ".format(LEFTcounter))
    ser = serial.Serial(port=selected_com,baudrate = 9600, timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
    ser.write(('1').encode())
    ser.close()

def btn_pushed_RIGHTT(event):
    print("RIGHT clicked")
    global RIGHTcounter
    RIGHTcounter += 1
    RIGHTbutton.configure(text="RIGHT {} ".format(RIGHTcounter))
    ser = serial.Serial(port=selected_com,baudrate = 9600, timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
    ser.write(('2').encode())
    ser.close()

def btn_pushed_UPP(event):
    print("UP clicked")
    global UPcounter
    UPcounter += 1
    UPbutton.configure(text="UP {} ".format(UPcounter))
    ser = serial.Serial(port=selected_com,baudrate = 9600, timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
    ser.write(('3').encode())
    ser.close()


def btn_pushed_DOWNN(event):
    print("DOWN clicked")
    global DOWNcounter
    DOWNcounter += 1
    DOWNbutton.configure(text="DOWN {} ".format(DOWNcounter))
    ser = serial.Serial(port=selected_com,baudrate = 9600, timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
    ser.write(('4').encode())
    ser.close()

parent = Tk()
parent.title('snake')
menubar = Menu(parent )

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
for i in com_list:
    filemenu.add_command(label=i, command=lambda mbox=[i]:com_selector(mbox))
    filemenu.add_separator()
filemenu.add_command(label="Exit", command=parent.quit)
menubar.add_cascade(label="COM port!", menu=filemenu)

# create a toplevel menu

# menubar.add_command(label="COM port!")
menubar.add_command(label="Quit!", command=parent.quit)

# display the menu
parent.config(menu=menubar)


LEFTbutton = Button(parent, text="LEFT {} ".format(LEFTcounter), fg = "red",command=btn_pushed_LEFT)
LEFTbutton.pack( side = LEFT)

RIGHTbutton = Button(parent, text="RIGHT {} ".format(RIGHTcounter), fg = "black",command=btn_pushed_RIGHT)
RIGHTbutton.pack( side = RIGHT )

UPbutton = Button(parent,  text="UP {} ".format(UPcounter), fg = "blue",command=btn_pushed_UP)
UPbutton.pack( side = TOP )

DOWNbutton = Button(parent,  text="DOWN {} ".format(DOWNcounter), fg = "green",command=btn_pushed_DOWN)
DOWNbutton.pack( side = BOTTOM)

parent.bind('<Left>', btn_pushed_LEFTT)
parent.bind('<Right>', btn_pushed_RIGHTT)
parent.bind('<Up>', btn_pushed_UPP)
parent.bind('<Down>', btn_pushed_DOWNN)

parent.mainloop()
