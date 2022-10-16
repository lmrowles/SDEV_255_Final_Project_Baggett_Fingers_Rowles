import tkinter as tk 
from PIL import Image, ImageTk

root = tk.Tk()

#canavas size and grid for columns and rows
canvas = tk.Canvas(root, width=700, height=500)
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

#Text, input boxes and options 
entry1 = tk.Entry (root)
canvas.create_window(200, 140, window=entry1)

label1 = tk.Label(root, text="Age :")
label1.place(x=100, y=130)

entry2 = tk.Entry(root)
canvas.create_window(200, 190, window=entry2)

label2 = tk.Label(root, text="Height :")
label2.place(x=90, y=180)

entry3 = tk.Entry(root)
canvas.create_window(200, 240, window=entry3)

label3 = tk.Label(root, text="Weight :")
label3.place(x=90, y=230)

label4 = tk.Label(root, text="Gender :")
label4.place(x=85, y=272)

label5 = tk.Label(root, text="KG")
label5.place(x=270, y=230)

label6 = tk.Label(root, text="CM")
label6.place(x=270, y=180)

label7 = tk.Label(root, text="BMR :", font = 15)
label7.place(x=85, y=325)

label8 = tk.Label(root, text="Calories per meal :", font = 15)
label8.place(x=0, y=350)

label9 = tk.Label(root, text="BMR Calculator ",  font = ("Savana", 25))
label9.grid(columnspan=15, column=0, row=0,)







#Main code for the BMR

def getBMR_Male():
    
    Age = float(entry1.get())
    Height = float(entry2.get())
    Weight = float(entry3.get())
    number3 = 3

    AnswerMale = int((Weight)*10 + (Height)*6.25 - (Age)*5 + 5)
    BMR = tk.Label(root, text = AnswerMale, font = 15)
    canvas.create_window(150,338, window=BMR)
        
    result1 = int(AnswerMale/number3)
    divde3 = tk.Label(root, text = result1, font = 15)
    canvas.create_window(150,364, window=divde3)


def getBMR_Female():

    Age = float(entry1.get())
    Height = float(entry2.get())
    Weight = float(entry3.get())
    number3 = 3

    AnswerFemale = int((Weight)*10 + (Height)*6.25 - (Age)*5 - 161)
    BMRFEMALE = tk.Label(root, text = AnswerFemale)
    canvas.create_window(150,335, window=BMRFEMALE)

    result2 = int(AnswerFemale/number3)
    divde3 = tk.Label(root, text = result2)
    canvas.create_window(150,362, window=divde3)


htype=tk.IntVar()
R1=tk.Radiobutton(root,text="Male",variable=htype,value=1, command = getBMR_Male)
R1.place(x=150, y=272)

R2=tk.Radiobutton(root,text="Female",variable=htype,value=2, command = getBMR_Female)
R2.place(x=230, y=272)




root.mainloop()