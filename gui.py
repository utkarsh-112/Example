from cProfile import label
from distutils.command.upload import upload
import tkinter as tk
from tkinter import END, Text, filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
top = tk.Tk()
top.geometry("400x300")
top.title("Example")
b1 = tk.Button(top, text='Upload file', width=20,
               command=lambda: upload_file())
b1.grid(row=1, column=1)
T = Text(top, height=1, width=30)
T.grid(row=2, column=1)


def upload_file():
    global img
    file = filedialog.askopenfilename(initialdir='F:\\Study\\Python\\drdo project',filetypes=[
                                                 ('Text doc',
                                                  '*.txt'), ('CSV files', '.csv'),
                                                 ])
    fob = open(file, 'r')
    s = fob.read()
    T.insert(END, s)
    


top.mainloop()
