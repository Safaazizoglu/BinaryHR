import tkinter
from tkinter import *
from tkinter import ttk
from masstrack import Mass
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import math

window = Tk()
window.title('Binary HR')
window.geometry("850x600")

mass = Mass()

list_colour = ["green", "blue", "yellow", "magenta", "orange", "purple", "brown", "pink", "gray", "olive", "cyan"]

box = ttk.Combobox()
box["values"] = ("0004", "0001", "004")

box_metallicity = tkinter.Label(text="Choose Metallicity:", font=("Ariel", 10, "bold"))
box_metallicity.place(x=5, y=30)
box_teff1 = tkinter.Label(text="Teff for star 1:", font=("Ariel", 10, "bold"))
box_teff1.place(x=5, y=85)
box_l1 = tkinter.Label(text="Limunosity for star 1:", font=("Ariel", 10, "bold"))
box_l1.place(x=5, y=135)
box_teff2 = tkinter.Label(text="Teff2 for star 2:", font=("Ariel", 10, "bold"))
box_teff2.place(x=5, y=185)
box_l2 = tkinter.Label(text="Limunosity for star2:", font=("Ariel", 10, "bold"))
box_l2.place(x=5, y=235)
box.place(x=5, y=55)
input1 = Entry()
input2 = Entry()
input3 = Entry()
input4 = Entry()
input1.place(x=5, y=105)
input2.place(x=5, y=155)
input3.place(x=5, y=205)
input4.place(x=5, y=255)

fig = plt.figure()
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().place(x=155, y=100)
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas.get_tk_widget().place(x=155, y=55)


def button_clicked():
    plt.clf()
    mass.selectz = box.get()

    mass.opencsv()
    mass.zams()
    mass.tams()
    mass.masstracker()

    binaryt1 = int(input1.get())
    binaryl1 = float(input2.get())
    binaryt2 = int(input3.get())
    binaryl2 = float(input4.get())

    binary1t = math.log(binaryt1, 10)
    binary1l = math.log(binaryl1, 10)
    binary2t = math.log(binaryt2, 10)
    binary2l = math.log(binaryl2, 10)

    plt.plot(mass.zamsT, mass.zamsL)
    plt.plot(mass.tamsT, mass.tamsL, "r")
    plt.plot(mass.mass1T, mass.mass1L, random.choice(list_colour), label="0.8M" u"\u2609")
    plt.plot(mass.mass2T, mass.mass2L, random.choice(list_colour), label="1M" u"\u2609")
    plt.plot(mass.mass3T, mass.mass3L, random.choice(list_colour), label="1.2M" u"\u2609")
    plt.plot(mass.mass4T, mass.mass4L, random.choice(list_colour), label="1.4M" u"\u2609")
    plt.plot(mass.mass5T, mass.mass5L, random.choice(list_colour), label="1.6M" u"\u2609")
    plt.plot(mass.mass6T, mass.mass6L, random.choice(list_colour), label="1.8M" u"\u2609")
    plt.plot(mass.mass7T, mass.mass7L, random.choice(list_colour), label="2M" u"\u2609")
    plt.plot(mass.mass8T, mass.mass8L, random.choice(list_colour), label="2.2M" u"\u2609")
    plt.plot(mass.mass9T, mass.mass9L, random.choice(list_colour), label="2.5M" u"\u2609")
    plt.plot(mass.mass10T, mass.mass10L, random.choice(list_colour), label="3M" u"\u2609")
    plt.plot(mass.mass11T, mass.mass11L, random.choice(list_colour), label="3.5M" u"\u2609")
    plt.plot(mass.mass12T, mass.mass12L, random.choice(list_colour), label="4M" u"\u2609")
    plt.scatter(binary1t, binary1l, s=80, marker="*", c="yellow", edgecolors="black")
    plt.scatter(binary2t, binary2l, s=80, marker="*", c="yellow", edgecolors="black")
    plt.legend()
    plt.gca().invert_xaxis()

    canvas.draw()
    print(binary1t)


button = Button(master=window,  command=button_clicked, height=2,  width=10, text="Plot")

button.place(x=25, y=305)

window.mainloop()
