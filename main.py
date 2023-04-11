import os

from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import filedialog as fd
from tkinter import messagebox



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




window.mainloop()

