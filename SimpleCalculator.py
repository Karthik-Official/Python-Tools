from tkinter import *
from tkinter import font
from tkinter import messagebox

def button_click(number):
    input.insert(END,number)
    
def button_clear():
    input.delete(0, END)
    
def button_back():
    current_number = input.get()
    if current_number:
        new_number = current_number[:-1]    # Removing the last character
        input.delete(0, END)                # Clearing the input widget
        input.insert(0, new_number)         # Inserting new number

def button_enter():
    try:
        output = eval(input.get())          # Getting the Expression and calculating result using eval funtion
        input.delete(0, END)                # Clearing the input widget
        input.insert(0,output)              # To display the output
    except:
        messagebox.showinfo("error","Enter correct expression")  
        
if __name__ == "__main__":
   
    # Creating GUI Window
    mainscreen = Tk()
    
    # Title of the Window
    mainscreen.title("Simple Calculator")   
     
    # Background colour of the window 
    mainscreen.configure(background="#BFC3C6")
    
    #
    EntryFont = font.Font(family="Helvetica", size=10)    
    
    # Input and Output Box
    input = Entry(mainscreen, width=50, borderwidth=5, font=EntryFont)
    input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    #Button Definition
    button_clear = Button(mainscreen, text="C", bg="#BFC3C9", activebackground="#D5D9DC",padx=39, pady=20, command=button_clear)
    button_back = Button(mainscreen, text="<-", bg="#BFC3C9", activebackground="#D5D9DC", padx=37, pady=20, command=button_back)
    button_mod = Button(mainscreen, text="%", bg="#BFC3C9", activebackground="#D5D9DC", padx=38, pady=20, command=lambda: button_click("%"))
    button_div = Button(mainscreen, text="/", bg="#BFC3C9", activebackground="#D5D9DC", padx=40, pady=20, command=lambda: button_click("/"))

    button_7 = Button(mainscreen, text="7", bg="#BFC3C9", activebackground="#D5D9DC", padx=40, pady=20, command=lambda: button_click("7"))
    button_8 = Button(mainscreen, text="8", bg="#BFC3C9", activebackground="#D5D9DC", padx=40, pady=20, command=lambda: button_click("8"))
    button_9 = Button(mainscreen, text="9", bg="#BFC3C9", activebackground="#D5D9DC", padx=40, pady=20, command=lambda: button_click("9"))
    button_mul = Button(mainscreen, text="*", bg="#BFC3C9", activebackground="#D5D9DC", padx=40, pady=20, command=lambda: button_click("*"))

    button_4 = Button(mainscreen, text="4", bg="#BFC3C9", activebackground="#D5D9DC", padx=40, pady=20, command=lambda: button_click("4"))
    button_5 = Button(mainscreen, text="5", bg="#BFC3C9", activebackground="#D5D9DC", padx=40, pady=20, command=lambda: button_click("5"))
    button_6 = Button(mainscreen, text="6", bg="#BFC3C9", activebackground="#D5D9DC", padx=40, pady=20, command=lambda: button_click("6"))
    button_sub = Button(mainscreen, text="-", bg="#BFC3C9", activebackground="#D5D9DC", padx=40, pady=20, command=lambda: button_click("-"))

    button_1 = Button(mainscreen, text="1", bg="#BFC3C9", activebackground="#D5D9DC", padx=40, pady=20, command=lambda: button_click("1"))
    button_2 = Button(mainscreen, text="2", bg="#BFC3C9", activebackground="#D5D9DC", padx=40, pady=20, command=lambda: button_click("2"))
    button_3 = Button(mainscreen, text="3", bg="#BFC3C9", activebackground="#D5D9DC", padx=40, pady=20, command=lambda: button_click("3"))
    button_add = Button(mainscreen, text="+", bg="#BFC3C9", activebackground="#D5D9DC", padx=39, pady=20, command=lambda: button_click("+"))

    button_0 = Button(mainscreen, text="0", bg="#BFC3C9", activebackground="#D5D9DC", padx=90, pady=20, command=lambda: button_click("0"))
    button_dot = Button(mainscreen, text=".", bg="#BFC3C9", activebackground="#D5D9DC", padx=41, pady=20, command=lambda: button_click("."))
    button_enter = Button(mainscreen, text="=", bg="#BFC3C9", activebackground="#D5D9DC", padx=39, pady=20, command=button_enter)

    #Button to on Screen
    button_clear.grid(row=1, column=0)
    button_back.grid(row=1, column=1)
    button_mod.grid(row=1, column=2)
    button_div.grid(row=1, column=3)

    button_7.grid(row=2, column=0)
    button_8.grid(row=2, column=1)
    button_9.grid(row=2, column=2)
    button_mul.grid(row=2, column=3)

    button_4.grid(row=3, column=0)
    button_5.grid(row=3, column=1)
    button_6.grid(row=3, column=2)
    button_sub.grid(row=3, column=3)

    button_1.grid(row=4, column=0)
    button_2.grid(row=4, column=1)
    button_3.grid(row=4, column=2)
    button_add.grid(row=4, column=3)

    button_0.grid(row=5, column=0, columnspan=2)
    button_dot.grid(row=5, column=2)
    button_enter.grid(row=5, column=3)


    mainscreen.mainloop()