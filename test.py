from dis import Instruction
import tkinter as tk
from tkinter.tix import COLUMN
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=900, height=600)
canvas.grid(columnspan=15, rowspan=25)

#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=13, row=3)

#instructions
instructions = tk.Label(root, text="Insert details to the left.")
instructions.grid(columnspan=15, column=0, row=25)

#Text boxes and options 
entry1 = tk.Entry (root)
canvas.create_window(200, 140, window=entry1)

label1 = tk.Label(root, text="Age :")
label1.place(x=100, y=130)

entry2 = tk.Entry(root)
canvas.create_window(200, 190, window=entry2)

label2 = tk.Label(root, text="Height :")
label2.place(x=90, y=180)

entry3 = tk.Entry(root)
canvas.create_window(360, 190, window=entry3)

label3 = tk.Label(root, text="Weight :")
label3.place(x=90, y=230)

entry4 = tk.Entry(root)
canvas.create_window(200, 240, window=entry4)

htype=tk.IntVar()
R1=tk.Radiobutton(root,text="Male",variable=htype,value=1)
R1.grid(column=3, row=4)

R2=tk.Radiobutton(root,text="Female",variable=htype,value=2)
R2.grid(column=4, row=4)

label4 = tk.Label(root, text="Gender :")
label4.place(x=85, y=272)

root.mainloop()