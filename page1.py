from tkinter import *
from PIL import Image, ImageTk

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
image = Image.open("depositphotos_82114924-stock-photo-slot-machine.png")
bg = ImageTk.PhotoImage(image)
background_label = Label(ws, image=bg)
background_label.place(relwidth=1, relheight=1)

f = ("Times bold", 14)
def nextPage():
    ws.destroy()
    import page2

def prevPage():
    ws.destroy()
    import page3
    
Label(
    ws,
    text="SLOT MACHINE!!!!",
    padx=10,
    pady=10,
    font=f
).place(relx=0.5, rely=0.05, anchor="center")

Button(
    ws, 
    text=" HOW TO PLAY", 
    font=f,
    command=nextPage
).place(relx=0.1, rely=0.99, anchor="sw")

Button(
    ws, 
    text="REGISTRATION", 
    font=f,
    command=prevPage
).place(relx=0.9, rely=0.99, anchor="se")

ws.mainloop()
