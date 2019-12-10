import RPi.GPIO as GPIO
from time import sleep
from tkinter import *

GPIO.setmode(GPIO.BCM)
led = 26   #set chan cho led , xem o datasheet roi noi day
GPIO.setup(led, GPIO.OUT)
button = 23  #set chan cho button, xem o datasheet roi noi day
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def AND():
    num1 = int(e.get())
    num2 = int(f.get())
    res = num1 & num2
    GPIO.output(led,res)

def OR():
    num1 = int(e.get())
    num2 = int(f.get())
    res = num1 | num2
    GPIO.output(led,res)

master = Tk()
master.title('and or')
e = Entry(master)
f = Entry(master)
a = Label(master, text='A')
a.pack()
e.pack()
b = Label(master, text='B')
b.pack()
f.pack()
btnAND = Button(master, text='AND', width=10, command=AND)
btnAND.pack()
btnOR = Button(master, text='OR', width=10, command=OR)
btnOR.pack()
mainloop()
