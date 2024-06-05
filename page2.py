from tkinter import *

ws = Tk()
ws.geometry('600x400')
ws.title('PythonGuides')
ws['bg']='#ffbf00'

f = ("Times bold", 18)
g= ("Times bold",14)

def nextPage():
    ws.destroy()
    import page3  

Label(
    ws,
    text="RULES!!",
    padx=10,
    pady=10,
    font= f
).pack(expand=True, anchor="center", pady=(10, 10))

Label(
    ws,
    text="""You will deposit some money into it and then click on spin button
if the two symbols match your amount is doubled. If all three match,
your bet is ten times, if none match you lose everything""",
    padx=20,
    pady=20,
    bg='#ffbf00',
    font=g
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="CONTINUE TO REGISTRATION", 
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
