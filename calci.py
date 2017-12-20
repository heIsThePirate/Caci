#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:46:52 2017
@author: mohit
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calci")
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = "N S W E")
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

num = StringVar()

def update(a):
    try:
        num.set(str(num.get())+a)
    except:
        pass

def calculate():
    try:
        num.set(eval(str(num.get())))
    except:
        num.set('Syntax Error')

def back():
    try:
        num.set(num.get()[:-1])
    except:
        pass

num_entry = ttk.Entry(mainframe, width = 40, textvariable = num)
num_entry.grid(column = 1, row = 1, columnspan = 4, pady = 5)

ttk.Button(mainframe, text = "(", command = lambda: update('(')).grid(column = 1, row = 2)
ttk.Button(mainframe, text = ")", command = lambda: update(')')).grid(column = 2, row = 2)
ttk.Button(mainframe, text = "AC", command = lambda: num.set('')).grid(column = 3, row = 2)
ttk.Button(mainframe, text = "/", command = lambda: update('/')).grid(column = 4, row = 2)
ttk.Button(mainframe, text = "7", command = lambda: update('7')).grid(column = 1, row = 3)
ttk.Button(mainframe, text = "8", command = lambda: update('8')).grid(column = 2, row = 3)
ttk.Button(mainframe, text = "9", command = lambda: update('9')).grid(column = 3, row = 3)
ttk.Button(mainframe, text = "*", command = lambda: update('*')).grid(column = 4, row = 3)
ttk.Button(mainframe, text = "4", command = lambda: update('4')).grid(column = 1, row = 4)
ttk.Button(mainframe, text = "5", command = lambda: update('5')).grid(column = 2, row = 4)
ttk.Button(mainframe, text = "6", command = lambda: update('6')).grid(column = 3, row = 4)
ttk.Button(mainframe, text = "-", command = lambda: update('-')).grid(column = 4, row = 4)
ttk.Button(mainframe, text = "1", command = lambda: update('1')).grid(column = 1, row = 5)
ttk.Button(mainframe, text = "2", command = lambda: update('2')).grid(column = 2, row = 5)
ttk.Button(mainframe, text = "3", command = lambda: update('3')).grid(column = 3, row = 5)
ttk.Button(mainframe, text = "+", command = lambda: update('+')).grid(column = 4, row = 5)
ttk.Button(mainframe, text = "BACK", command = lambda: back()).grid(column = 1, row = 6)
ttk.Button(mainframe, text = "0", command = lambda: update('0')).grid(column = 2, row = 6)
ttk.Button(mainframe, text = ".", command = lambda: update('.')).grid(column = 3, row = 6)
equal_to = ttk.Button(mainframe, text = "=", command = calculate).grid(column = 4, row = 6)

num_entry.focus()
root.mainloop()