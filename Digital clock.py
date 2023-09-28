#import window module
from tkinter import *
from tkinter.ttk import *

#form system matching time
from time import strftime

#creating tkinter window
root = Tk()
root.titlt = ('clock')

#to display the time 
def time():
    String = strftime('%H:%M:%S %p')
    lbl.config(text = String)
    lbl.after(1000,time)

#for clock colour and design
lbl = Label(root, font=('Candara',40,'bold'),background='black',foreground='white') 

#place the clock in center   
lbl.pack(anchor='center')
time()

mainloop()