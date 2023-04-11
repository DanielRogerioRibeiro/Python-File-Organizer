#Organizador de Arquivo

import os
import shutil

from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import filedialog as fd
from tkinter import messagebox

from PIL import Image, ImageTk

#Importando a parte Gráfica
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure



#Importando a Aba View.py
from view import *

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

janela = Tk ()
janela.title ("")
janela.geometry('700x350')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

################# Creating Frames ####################

frameUp = Frame(janela, width=700, height=50, bg=co1,  relief="flat",)
frameUp.grid(row=0, column=0)

frameMiddle = Frame(janela,width=700, height=300,bg=co1)
frameMiddle.grid(row=1, column=0,sticky=NSEW)


# ------------- Creating individual frames -------------------------

frame_operations = Frame(frameMiddle, width=300, height=350,bg=co1)
frame_operations.grid(row=0,column=0)

frame_graph = Frame(frameMiddle, width=400, height=350,bg=co1)
frame_graph.place(x=170,y=0)

frame_operations.lift()

# opening image

app_img = Image.open('imagens/icon.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameUp, image=app_img, text="File organizer App", width=700, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg= co1, fg=co4 )
app_logo.place(x=0, y=0)
 

# pie chart function ------------------------
def chart_pie(list_1, list_2):
     # make figure and assign axis objects
     figure = plt.Figure(figsize=(5, 3), dpi=100)
     ax = figure.add_subplot(111)

     list_values = list_1
     extension_list = list_2

     ax.pie(list_values, wedgeprops=dict(width=0.3), colors=colors,shadow=True, startangle=90)

     ax.legend(extension_list, loc="center right", bbox_to_anchor=(1.55, 0.50))

     canva = FigureCanvasTkAgg(figure, frame_graph)
     canva.get_tk_widget().grid(row=0,column=0,sticky=NSEW)

# Select Folder -----------------------------------

l_app = Label(frame_operations, text="Select Folder", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_app.place(x=10, y=10)


# defining global the folder variable
global folder


# function to choose the folder
def choose_folder():
     global folder
    
     folder = fd.askdirectory()

     # creating the list of extensions
     extension_list = ['.txt','.csv','.xlsx','.pdf','.zip','.jpg','.png','.mp3','.mp4','. py','.html','.css','.js']
     combobox_extension_list = []
     list_extension_counted = []
     list_extension_values = []

     number_of_folders = 0

     for i in extension_list:
         folder_path = folder
         extension = i
         num_files, num_folders = count_files_and_folders(folder_path, extension)

         if num_files<=0:
             pass
         else:
             list_extension_counted.append(i + ": " + str(num_files))
             combobox_extension_list.append(i)
             list_extension_values.append(num_files)
             number_of_folders = num_folders


     # added the total number of folders
     list_extension_counted.append('folders: ' + str(number_of_folders))
     list_extension_values.append(number_of_folders)

     # passing extensions to the combobox
     combo_extension ['values'] = (combobox_extension_list)
     combo_extension_move ['values'] = (combobox_extension_list)

     # sending the values to the graph by calling the graph function
     chart_pie(list_extension_values, list_extension_counted)


b_choose = Button(frame_operations,command=choose_folder, text="Choose ",width=15, overrelief=RIDGE, font=('ivy 8'),bg=co1, fg=co4 )
b_choose.place(x=10, y=40)


# Copying Files -----------------------------------

l_app = Label(frame_operations, text="Copy Files", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_app.place(x=10, y=91)


def copy():
     global folder

     # getting extension
     extension = combo_extension.get()

     print(folder)

     # picking up destination
     destination = fd.askdirectory()

     # calling function copy files
     copy_files(folder,destination,extension)

     # inform
     messagebox.showinfo('Copy', "The files were successfully copied")

     # clear field
     combo_extension.delete(0,END)

    
combo_extension = ttk.Combobox(frame_operations, width=5,font=('Ivy 10'))
combo_extension.place(x=110, y=91)

# copy button
img_copy = Image.open('imagens/copiar.png')
img_copy = img_copy.resize((17,17))
img_copy = ImageTk.PhotoImage(img_copy)

b_copy = Button(frame_operations,command=copy,image=img_copy, compound=LEFT, anchor=NW, text="Choose Destination ",width=110, overrelief=RIDGE, font=('ivy 8'),bg=co1, fg=co4)
b_copy.place(x=171, y=90)


# Move Files -----------------------------------

l_app = Label(frame_operations, text="Move Files", height=1,anchor=NW,relief="flat", font=('Ivy 10'), bg=co1, fg=co4)
l_app.place(x=10, y=141)

def move():
     global folder

     # getting extension
     extension = combo_extension_move.get()

     # picking up destination
     destination = fd.askdirectory()

     source_folder = folder
     destination_folder = destination
     file_extension = extension

     # calling the function to move the files
     move_files_by_extension(source_folder, destination_folder, file_extension)

     # inform
     messagebox.showinfo('Move', "The files were successfully moved")

     # clear field
     combo_extension_move.delete(0,END)

combo_extension_move = ttk.Combobox(frame_operations, width=5,font=('Ivy 10'))
combo_extension_move.place(x=110, y=141)

# move button
img_move = Image.open('imagens/mover.png')
img_move = img_move.resize((17,17))
img_move = ImageTk.PhotoImage(img_move)

b_move = Button(frame_operations,command=move,image=img_move, compound=LEFT, anchor=NW, text="Choose destination ",width=110, overrelief=RIDGE, font=('ivy 8'),bg=co1, fg=co4)
b_move.place(x=171, y=140)

# Excluir Arquivos -----------------------------------

l_app = Label(frame_operations, text="Delete Files", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_app.place(x=10, y=191)


# Delete button
img_delete = Image.open('imagens/delete.png')
img_delete = img_delete.resize((17,17))
img_delete = ImageTk.PhotoImage(img_delete)

b_mover = Button(frame_operations,image=img_delete, compound=LEFT, anchor=NW, text="Delete files ",width=110, overrelief=RIDGE, font=('ivy 8'),bg=co1, fg=co4 )
b_mover.place(x=171, y=190)

janela.mainloop ()