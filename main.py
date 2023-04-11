#Organizador de Arquivo

import os

from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import filedialog as fd
from tkinter import messagebox

from PIL import Image, ImageTk

################# colors ###############

co0 = "#2e2d2b"  # Black
co1 = "#feffff"  # White
co2 = "#4fa882"  # Green
co3 = "#38576b"  # Value
co4 = "#403d3d"  # Letter
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # Blue
co7 = "#3fbfb9"  # Green
co8 = "#263238"  # + green
co9 = "#e9edf5"  # + green

colors = ['#1f77b4', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555','#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b','#e377c2' ,'#7f7f7f','#bcbd22','#17becf',]
['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b','#e377c2' ,'#7f7f7f','#bcbd22','#17becf','#ff9896','#98df8a','#aec7e8','#ffbb78' ,'#c5b0d5','#c49c94','#f7b6d2','#dbdb8d','#9edae5','#393b79']


################# creating window ###############

window = Tk ()
window.title ("")
window.geometry('700x350')
window.configure(background=co9)
window.resizable(width=FALSE, height=FALSE)

# Definindo o Estilo da Janela
style = ttk.Style(window)
style.theme_use("clam")


################# Creating Frames ####################

frameUp = Frame(window, width=700, height=50, bg=co1,  relief="flat",)
frameUp.grid(row=0, column=0)

frameMiddle = Frame(window,width=700, height=300,bg=co1)
frameMiddle.grid(row=1, column=0,sticky=NSEW)


# opening image

app_img = Image.open('imagens/icon.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameUp, image=app_img, text="File Organizer App", width=700, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg= co1, fg=co4 )
app_logo.place(x=0, y=0)

#Trabalhando no Frame meio

#Dividindo o Frame meio em Operações (lado Esquerdo) e Gráfico (Lado Direito)

frame_operations = Frame(frameMiddle, width=300, height=350,bg=co1)
frame_operations.grid(row=0,column=0)

frame_graphic = Frame(frameMiddle, width=400, height=350,bg=co1)
frame_graphic.place(x=170,y=0)

frame_operations.lift()

#criando botões e entradas

# Select Folder -----------------------------------

l_app = Label(frame_operations, text="Select Folder", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_app.place(x=10, y=10)

window.mainloop()
