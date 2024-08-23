from tkinter import *
root = Tk()

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        calculate()
    elif text == "AC":
        uservalue.set("") 
    else:
        uservalue.set(uservalue.get() + text)

def calculate():
    try:
        result = eval(uservalue.get())
        uservalue.set(result)
    except Exception as e:
        uservalue.set("Error")

def backscapce():
    current_text = uservalue.get()
    new_text = current_text[:-1]
    uservalue.set(new_text)

def enter(event):
    calculate()

uservalue = StringVar()
userentry = Entry(root, textvariable=uservalue, font="Times 24 bold", relief=RIDGE, bg="black", fg="white", justify=RIGHT, bd=6)
userentry.grid(row=0, columnspan=4, ipadx=5)
userentry.bind("<Return>", enter)

b = Button(root, text="AC", font="Times 24", width=3, bg="cyan", bd=12.5, relief=FLAT)
b.grid(row=1, column=0)
b.bind("<Button-1>", click)
b = Button(root, text="(", font="Times 24", width=3, bg="cyan", bd=12.5, relief=FLAT)
b.grid(row=1, column=1)
b.bind("<Button-1>", click)
b = Button(root, text=")", font="Times 24", width=3, bg="cyan", bd=12.5, relief=FLAT)
b.grid(row=1, column=2)
b.bind("<Button-1>", click)
b = Button(root, text="/", font="Times 24", width=3, bg="cyan", bd=12.5, relief=FLAT)
b.grid(row=1, column=3)
b.bind("<Button-1>", click)

b = Button(root, text="7", font="Times 24", width=3, bg="#041f60", fg="white", bd=12.5, relief=FLAT)
b.grid(row=2, column=0)
b.bind("<Button-1>", click)
b = Button(root, text="8", font="Times 24", width=3, bg="#041f60", fg="white", bd=12.5, relief=FLAT)
b.grid(row=2, column=1)
b.bind("<Button-1>", click)
b = Button(root, text="9", font="Times 24", width=3, bg="#041f60", fg="white", bd=12.5, relief=FLAT)
b.grid(row=2, column=2)
b.bind("<Button-1>", click)
b = Button(root, text="*", font="Times 24", width=3, bg="cyan", bd=12.5, relief=FLAT)
b.grid(row=2, column=3)
b.bind("<Button-1>", click)

b = Button(root, text="4", font="Times 24", width=3, bg="#041f60", fg="white", bd=12.5, relief=FLAT)
b.grid(row=3, column=0)
b.bind("<Button-1>", click)
b = Button(root, text="5", font="Times 24", width=3, bg="#041f60", fg="white", bd=12.5, relief=FLAT)
b.grid(row=3, column=1)
b.bind("<Button-1>", click)
b = Button(root, text="6", font="Times 24", width=3, bg="#041f60", fg="white", bd=12.5, relief=FLAT)
b.grid(row=3, column=2)
b.bind("<Button-1>", click)
b = Button(root, text="-", font="Times 24", width=3, bg="cyan", bd=12.5, relief=FLAT)
b.grid(row=3, column=3)
b.bind("<Button-1>", click)

b = Button(root, text="1", font="Times 24", width=3, bg="#041f60", fg="white", bd=12.5, relief=FLAT)
b.grid(row=4, column=0)
b.bind("<Button-1>", click)
b = Button(root, text="2", font="Times 24", width=3, bg="#041f60", fg="white", bd=12.5, relief=FLAT)
b.grid(row=4, column=1)
b.bind("<Button-1>", click)
b = Button(root, text="3", font="Times 24", width=3, bg="#041f60", fg="white", bd=12.5, relief=FLAT)
b.grid(row=4, column=2)
b.bind("<Button-1>", click)
b = Button(root, text="+", font="Times 24", width=3, bg="cyan", bd=12.5, relief=FLAT)
b.grid(row=4, column=3)
b.bind("<Button-1>", click)

b = Button(root, text="0", font="Times 24", width=3, bg="#041f60", fg="white", bd=12.5, relief=FLAT)
b.grid(row=5, column=1)
b.bind("<Button-1>", click)
b = Button(root, text=".", font="Times 24", width=3, bg="#041f60", bd=12.5, fg="white", relief=FLAT)
b.grid(row=5, column=0)
b.bind("<Button-1>", click)
b = Button(root, text="=", font="Times 24", width=3, bg="cyan", bd=12.5, relief=FLAT)
b.grid(row=5, column=3)
b.bind("<Button-1>", click)

b = Button(root, text="BS", font="Times 24", width=3, bg="#041f60", fg="white", bd=12.5, relief=FLAT, command=backscapce)
b.grid(row=5, column=2)

root.wm_iconbitmap("cal.ico")
root.configure(background="black")
root.title("Avinash Calculator")
root.geometry("342x475")
root.resizable(0,0)
root.mainloop()
