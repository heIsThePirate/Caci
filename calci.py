# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk

class window(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        
        self.input = tk.Entry(self).grid(row=0,column=0,columnspan=4,pady=3)
        
        self.one = tk.Button(self,text='1',width=3).grid(row=4,column=1)
        
        self.two = tk.Button(self,text='2',width=3).grid(row=4,column=2)
        
        self.three = tk.Button(self,text='3',width=3).grid(row=4,column=3)
        
        self.four = tk.Button(self,text='4',width=3).grid(row=3,column=1)
        
        self.five = tk.Button(self,text='5',width=3).grid(row=3,column=2)
        
        self.six = tk.Button(self,text='6',width=3).grid(row=3,column=3)
        
        self.seven = tk.Button(self,text='7',width=3).grid(row=2,column=1)
        
        self.eight = tk.Button(self,text='8',width=3).grid(row=2,column=2)
        
        self.nine = tk.Button(self,text='9',width=3).grid(row=2,column=3)
        
        self.AC = tk.Button(self,text='AC',width=3).grid(row=1,column=3)
        
        self.backspace = tk.Button(self,text='back',width=10).grid(row=1,column=1,columnspan=2)
        
        self.percent = tk.Button(self,text='%',width=3).grid(row=5,column=1)
        
        self.decimal = tk.Button(self,text='.',width=3).grid(row=5,column=3)
        
        self.zero = tk.Button(self,text='0',width=3).grid(row=5,column=2)
        
        self.divide = tk.Button(self,text='/',width=3).grid(row=1,column=4)
        
        self.multiply = tk.Button(self,text='*',width=3).grid(row=2,column=4)
        
        self.subtract = tk.Button(self,text='-',width=3).grid(row=3,column=4)
        
        self.add = tk.Button(self,text='+',width=3).grid(row=4,column=4)
        
        self.equal = tk.Button(self,text='=',width=3).grid(row=5,column=4)
        
root = tk.Tk()
App = window(master=root)
App.mainloop()
