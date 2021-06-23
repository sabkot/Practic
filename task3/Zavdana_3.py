from tkinter import *
from tkinter import messagebox
from tkinter import ttk  
import math
import sys


win = Tk()
win['bg'] = '#33ffe6'
win.title("Калькулятор")

key_list = [

"C", "ln",
"%" ,"(", ")","√2", "bin",
 "П", "xⁿ", "/",
"ctg" ,"7", "8", "9", "*", 
"tg" , "4", "5", "6", "-", 
"cos", "1", "2", "3", "+",
"sin", ".", "0", "±", "="]
r = 1
c = 0


def calc(key):
    global memory
    if key == "=":
        
        str1 = "-+0123456789.*/)(" 
        if cal_in.get()[0] not in str1:
            cal_in.insert(END, "Перший символ - не цифра")
            messagebox.showerror( "Число не було введене")

        try:
            result = eval(cal_in.get())
            cal_in.insert(END, "=" + str(result))
        except:
            cal_in.insert(END, "Помилка")
            messagebox.showerror("Перевірте правильність введених даних")

    elif key == "C":
        cal_in.delete(0, END)
    elif key == "±":
        if "=" in cal_in.get():
            cal_in.delete(0, END)
        try:
            if cal_in.get()[0] == "-":
                cal_in.delete(0)
            else:
                cal_in.insert(0, "-")
        except IndexError:
            pass
    elif key == "П":
        cal_in.insert(END, math.pi)
    elif key == "sin":
        cal_in.insert(END, "=" + str(math.sin(int(cal_in.get()))))
    elif key == "(":
        cal_in.insert(END, "(")
    elif key == ")":
        cal_in.insert(END, ")")
    elif key == "xⁿ":
        cal_in.insert(END, "**")
    elif key == "ln":
        cal_in.insert(END, "=" + str(math.log(int(cal_in.get()))))    
    elif key == "cos":
        cal_in.insert(END, "=" + str(math.cos(int(cal_in.get()))))
    elif key == "tan":
        cal_in.insert(END, "=" + str(math.tan(int(cal_in.get()))))
    elif key == "ctg":
        cal_in.insert(END, "=" + str((math.cos(int(cal_in.get()))/(math.sin(int(cal_in.get()))))))
    elif key == "%":
        cal_in.insert(END, "=" + str(int(cal_in.get())*(int(cal_in.get())/100)))
    elif key == "√2":
        cal_in.insert(END, "=" + str(math.sqrt(int(cal_in.get()))))
    elif key == "bin":
        cal_in.insert(END, "=" + bin(int(cal_in.get())))
    else:
        if "=" in cal_in.get():
            cal_in.delete(0, END)
        cal_in.insert(END, key)
        win.mainloop()


for i in key_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(win, text=i, command = cmd, width = 7).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1
cal_in = Entry(win, width = 30)
cal_in.grid(row=0, column=0, columnspan=5)
