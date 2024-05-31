from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("BMI Calculator")
root.geometry("350x580+300+200") #470
root.resizable(False, False)
root.configure(bg="#f0f1f5")

def BMI():
    h=float(Height.get())
    w=float(Weight.get())

    # convert height into meter
    m=h/100
    bmi=round(float(w/m**2), 1)
    
    label1.config(text=bmi)

    #you can change value because different countries have different bmi index
    if bmi <= 18.5:
        label2.config(text="Underweigth!")
        label3.config(text="lower weight than normal body!")
        
    elif bmi > 18.5 and bmi <=25:
        label2.config(text="Normal")
        label3.config(text="You are Healthy!")
        
    elif bmi > 25 and bmi <=30:
        label2.config(text="Overweight!")
        label3.config(text="Slightly Overweight!")
        
    else:
        label2.config(text="Obes!")
        label3.config(text="health may be at risk!")

#icon
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)

#top
top = PhotoImage(file="Images/top.png")
top_image=Label(root,image=top,background="#f0f1f5")
top_image.place(x=10,y=-10) # x=10

# bottom box
Label  (root, width= 72, height= 18, bg="lightblue").pack(side=BOTTOM)

#TWO BOXES
box = PhotoImage(file="Images/box.png")
Label(root, image=box).place(x=20, y=100)
Label(root,image=box).place(x=190,y=100)

# scale
scale = PhotoImage(file="Images/scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=350)

######################Slider########################

current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())

    size=int(float(get_current_value()))
    img=(Image.open("Images/man.png"))
    resized_image=img.resize((50,10+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=50, y=520-size)
    secondimage.image=photo2


# command to change background color of scale
style = ttk.Style()
style.configure("TSale",bg="white")
slider =tk.Scale(root,from_=0, to=220, orient="horizontal", command=slider_changed, variable=current_value) #, style="TScale"
slider.place(x=40, y=180)


#####################################################
#@@@@@@@@@@@@@@@@@@@@@@@@@@SLIDER2@@@@@@@@@@@@@@@@@@@

current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())



# command to change background color of scale
style2 = ttk.Style()
style2.configure("TSale",bg="white")
slider2 =tk.Scale(root,from_=0, to=200, orient="horizontal", command=slider_changed2, variable=current_value2) #, style="TScale"
slider2.place(x=210, y=180)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#Entry box
Height=StringVar()
Weight=StringVar()
height = Entry(root,textvariable=Height, width=5, font='arial 30', bg="#000", fg="#fff", bd=0, justify=CENTER)
height.place(x=35, y=110)
Height.set(get_current_value())

weight = Entry(root,textvariable=Weight, width=5, font='arial 30', bg="#000", fg="#fff", bd=0, justify=CENTER)
weight.place(x=207, y=110)
Weight.set(get_current_value2())

# main image
secondimage = Label(root, bg="lightblue")
secondimage.place(x=70, y=530)

Button(root,text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=200,y=320)

label1 =Label(root, font="arial 30 bold", bg="lightblue", fg="#fff")
label1.place(x=50, y=320)

label2 =Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=240, y=440)

label3 =Label(root, font="arial 10 bold", bg="lightblue")
label3.place(x=200, y=500)


root.mainloop()
