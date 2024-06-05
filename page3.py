from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as sql
import random

conn = sql.connect(host='localhost', user='root', passwd='charansingh', database='python')
c1 = conn.cursor()
total_amount = 0

def input_data(name, contact, amount):
    insert_query_user = "INSERT INTO user (name, contact, deposited) VALUES (%s, %s, %s)"
    user_data = (name, contact, amount)
    c1.execute(insert_query_user, user_data)
    conn.commit()

def next_page():
    global total_amount
    ws.withdraw()  
    total_amount += int(amount_entry.get())  
    main()    

def deposit():
    name = name_entry.get()
    contact = contact_entry.get()
    amount = amount_entry.get()
    
    if amount.isdigit():
        amount = int(amount)
    else:
        messagebox.showerror("Error", "Enter a valid amount!")
        return
    
    if amount <= 0:
        messagebox.showerror("Error", "Entered amount should be greater than zero!")
        return
    
    input_data(name, contact, amount)
    messagebox.showinfo("Deposit Successful", "You can now continue to the game.")

def reveal_text(button, label):
    ab = ["❤️", "♠️", "♦️"]
    x = random.choice(ab)  
    if label.cget("text") == "":
        label.config(text=x)
        button.config(text=x)
    else:
        label.config(text="")
        button.config(text="Reveal Text")


def main():
    global total_amount
    
    def spin():
        global total_amount
    
        emoji_symbols = ["❤️", "♠️", "♦️"]
        chosen_symbols = [random.choice(emoji_symbols) for _ in range(3)]

        button1.config(text=chosen_symbols[0])
        button2.config(text=chosen_symbols[1])
        button3.config(text=chosen_symbols[2])
        
        
        if chosen_symbols[0] == chosen_symbols[1] == chosen_symbols[2]:
            messagebox.showinfo("Congratulations!", "All three symbols are the same! Your money has been doubled.")
            total_amount *= 2  
        #elif chosen_symbols[0] == chosen_symbols[0] or chosen_symbols[1] == chosen_symbols[1]:
          #  messagebox.showinfo("Congratulations!", "Two symbols are the same! You win something!")
         #   total_amount *= 2
                                                                        
        else :
            chosen_symbols[0]!= chosen_symbols[1]!= chosen_symbols[2]
            messagebox.showinfo("YOU LOST EVERYTHING","YOU LOST ALL YOUR AMOUNT")
            total_amount=0
            exit                                                
                             
        
        update_query = "UPDATE user SET deposited = %s WHERE name = %s"
        c1.execute(update_query, (total_amount, name_entry.get()))
        conn.commit()
        
        
        messagebox.showinfo("Total Amount", f"Total amount left: {total_amount}")

        
        spin_again = messagebox.askyesno("Spin Again", "Do you want to spin again?")
        
        
        if spin_again:
            button1.config(text="")
            button2.config(text="")
            button3.config(text="")
        else:
            root.destroy()  
    
    root = Toplevel()
    root.title("Slot Machine")
    root.geometry("700x400")
    root.configure(background="seagreen")
    
    intro = """Welcome to the game...
    Click on the buttons to reveal the symbols. If all three symbols are the same, your bet will be doubled."""
    
    
    nameLabel = Label(root, text="SLOT MACHINE", font=('Cambria', 60))
    nameLabel.pack()
    lbl = Label(root, text=intro, background='seagreen', font=('Cambria', 12))
    lbl.pack()
    
    
    button_frame = Frame(root)
    button_frame.pack(pady=30)  

    label = Label(root, text="", font=("Arial", 20), bg="red")
    label.pack()

    
    button1 = Button(button_frame, text="Reveal Text", command=lambda: reveal_text(button1, label), width=17, height=5, bg="red")
    button1.pack(side="left", padx=15)

    button2 = Button(button_frame, text="Reveal Text", command=lambda: reveal_text(button2, label), width=17, height=5, bg="red")
    button2.pack(side="left", padx=15)

    button3 = Button(button_frame, text="Reveal Text", command=lambda: reveal_text(button3, label), width=17, height=5, bg="red")
    button3.pack(side="left", padx=15)
    
    
    spin_button = Button(root, text="SPIN", command=spin, width=20, height=2, bg="green")
    spin_button.pack(pady=20)
    
ws = Tk()
ws.geometry('400x300')
ws.title('Registration Form')
ws['bg']='#CCCCCC'

f = ("Times bold", 14)

deposit_frame = Frame(ws)
deposit_frame.pack(pady=10)

name_label = Label(deposit_frame, text="Name:")
name_label.grid(row=1, column=0, pady=10)

name_entry = Entry(deposit_frame)
name_entry.grid(row=1, column=1, padx=10)

contact_label = Label(deposit_frame, text="Contact:")
contact_label.grid(row=3, column=0 , pady=20)

contact_entry = Entry(deposit_frame)
contact_entry.grid(row=3, column=1, pady=20)

amount_label = Label(deposit_frame, text="Amount:")
amount_label.grid(row=7, column=0, pady=20)

amount_entry = Entry(deposit_frame)
amount_entry.grid(row=7, column=1, pady=20)
deposit_button = Button(deposit_frame, text="Deposit", command=deposit)
deposit_button.grid(row=9, columnspan=2, pady=10)
continue_button = Button(ws, text="CONTINUE TO GAME", font=f, command=next_page)
continue_button.pack(fill=X, expand=TRUE, side=BOTTOM)
ws.mainloop()
