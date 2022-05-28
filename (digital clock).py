#WAP in python to make a digital clock


# importing whole module 

from tkinter import *

from tkinter.ttk import * 


# importing strftime function to 

# retrieve system's time 

from time import strftime 



# creating tkinter window 

root = Tk() 

root.title('Clock') 



# This function is used to  

# display time on the label 

def time(): 

    string = strftime('%H:%M:%S %p') 
    label.config(text=string)
    label.after(1000, time) 

# Styling the label widget so that clock 

# will look more attractive 

label = Label(root, font =("times", 60,),

  background = "black", foreground = "cyan")
  
label.grid(row=0, column=0)


# Placing clock at the centre 

# of the tkinter window 

label.pack(anchor = "center")

time()

mainloop()