from tkinter import *

# window
win = Tk()
win.title("Calculator")

# box
e = Entry(win, width=41, borderwidth=10, font=500)
e.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
eq = e.get()


# funcs
def button_click(num):
    global eq
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))
    eq = e.get()


def button_clr():
    global eq
    e.delete(0, END)
    eq = e.get()


def button_backspace():
    global eq
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)[:-1])
    eq = e.get()


def button_eq():
    global eq
    e.delete(0, END)
    e.insert(0, str(eval(eq)))
    eq = e.get()


def button_sq():
    global eq
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(eval(str(current) + '*' + str(current))))
    eq = e.get()


# Define buttons
button_backs = Button(win, text="← ", padx=15, pady=0, command=button_backspace, fg="#FF0000", font=500, borderwidth=2)

button_1 = Button(win, text="1", padx=42, pady=20, command=lambda: button_click(1), bg="#D9D9D9", font=500)
button_2 = Button(win, text="2", padx=42, pady=20, command=lambda: button_click(2), bg="#D9D9D9", font=500)
button_3 = Button(win, text="3", padx=42, pady=20, command=lambda: button_click(3), bg="#D9D9D9", font=500)
button_4 = Button(win, text="4", padx=42, pady=20, command=lambda: button_click(4), bg="#D9D9D9", font=500)
button_5 = Button(win, text="5", padx=42, pady=20, command=lambda: button_click(5), bg="#D9D9D9", font=500)
button_6 = Button(win, text="6", padx=42, pady=20, command=lambda: button_click(6), bg="#D9D9D9", font=500)
button_7 = Button(win, text="7", padx=42, pady=20, command=lambda: button_click(7), bg="#D9D9D9", font=500)
button_8 = Button(win, text="8", padx=42, pady=20, command=lambda: button_click(8), bg="#D9D9D9", font=500)
button_9 = Button(win, text="9", padx=42, pady=20, command=lambda: button_click(9), bg="#D9D9D9", font=500)
button_0 = Button(win, text="0", padx=42, pady=20, command=lambda: button_click(0), bg="#D9D9D9", font=500)

button_sqr = Button(win, text='^2', padx=38, pady=20, command=button_sq, font=500)
button_dot = Button(win, text='‧', padx=42, pady=20, command=lambda: button_click('.'), font=500)
button_mul = Button(win, text="X", padx=39, pady=20, command=lambda: button_click('*'), font=500)
button_div = Button(win, text="/", padx=42, pady=20, command=lambda: button_click('/'), font=500)
button_sub = Button(win, text="-", padx=42, pady=20, command=lambda: button_click('-'), font=500)
button_add = Button(win, text="+", padx=41, pady=20, command=lambda: button_click('+'), font=500)
button_equals = Button(win, text="   =   ", padx=81, pady=20, command=button_eq, fg="#000000", font=500)
button_clr = Button(win, text="CLEAR", padx=72, pady=20, command=button_clr, fg="#FF0000", font=500)

# pos
button_backs.grid(row=0, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_0.grid(row=5, column=0)

button_dot.grid(row=5, column=1)
button_equals.grid(row=5, column=2, columnspan=2)
button_sqr.grid(row=1, column=2)
button_clr.grid(row=1, column=0, columnspan=2)
button_div.grid(row=1, column=3)

# main
win.mainloop()