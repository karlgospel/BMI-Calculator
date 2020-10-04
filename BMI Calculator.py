#!/usr/bin/env python3
#from tkinter import *
import tkinter as tk
from tkinter import messagebox

#Create a window and set title
window = tk.Tk()
window.title("Welcome")

#IMPORTANT!!! -- Calls for the endless loop of the window so
#the window will wait for user to interact
#- MUST USE AT END!!!
#window.mainloop()

###----LABELS----###



#Adjust the font size, style and/or decoration
lbl = tk.Label(window, text="BMI Calculator", font = ("Arial Bold", 16))

#Position label using the grid function
#Without grid function - no label shows up
lbl.grid(column=0, row=0, columnspan=3)

###---WINDOWS---###

#Set size of the window - (widthxheight)
window.geometry('230x350')

##Create a textbox

weightLabel = tk.Label(window, text= "Weight (kg) = ")
weightLabel.grid(column=0, row =2)
weight = tk.Entry(window,width=10)
weight.grid(column=1, row=2, pady=10)

heightLabel = tk.Label(window, text= "Height (m) = ")
heightLabel.grid(column=0, row =3)
height = tk.Entry(window,width=10)
height.grid(column=1, row=3,pady=10)




#BUTTON CLICK EVENT

#Create a function that executes when button is clicked
def clicked(self):
    category = ""
    colour=""
    try:
        weightInput = float(weight.get())
    except:
        tk.messagebox.askretrycancel('Missing Entry','You missed something')
        return
    try:
        heightInput = float(height.get())
    except:
        tk.messagebox.askretrycancel('Missing Entry','You missed something')
        return
    result = round(weightInput / heightInput **2,2)
        
    if result <= 18.5:
        category = "Underweight"
        colour = "yellow"
    elif result > 18.5 and result < 25:
        category = "Healthy Weight"
        colour = "green"
    elif result > 25 and result < 30:
        category = "Overweight"
        colour = "orange"
    elif result >= 30:
        category = "Obese"
        colour = "red"
    resultLabel.config(text = "Your BMI is " + str(result))
    catLabel.config(text = ("Weight Status: " + category),bg=colour, relief='groove')
    

#Add a button to the window 
btn = tk.Button(window, text='Calculate', command = clicked)

#Set position of button
#Make sure it's on seprerate row/column to other items
btn.grid(column=1, row = 4)
btn.bind("<Return>",clicked)

resultLabel = tk.Label(window, text="", font = ("Arial", 12))
resultLabel.grid(column=0, row=5, columnspan =3, padx=5, pady=5)

catLabel = tk.Label(window, text="", font = ("Arial", 12))
catLabel.grid(column=0, row=6, columnspan =3, padx=5, pady=5)


####  BMI GUIDE

BMI_Title = tk.Label(text='Body Mass Index(BMI) Guide', font = ("Arial Bold", 10))
BMI_Title.grid(column=0,row=7, columnspan = 3, pady=5)
BMI_Info_Pane = tk.Label(text='Below 18.5 = Underweight \n18.5 to 24.9 = Normal or Healthy Weight \n25.0 to 29.9 = Overweight \n30.0 /and Above = Obese')

#BMI	Weight Status
#Below 18.5	= Underweight
#18.5 to 24.9	= Normal or Healthy Weight
#25.0 to 29.9	= Overweight
#30.0 /and Above	= Obese")
BMI_Info_Pane.grid(column=0, row=8, columnspan=3, pady=5)

window.mainloop()


