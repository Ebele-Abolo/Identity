# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:07:21 2021

@author: joyab
"""

from tkinter import*

root = Tk()
root.title("Identity Card")
root.geometry("300x400")

label_id = ()
label_name = ()
label_dob = ()
label_pin= ()
label_address=()
label_vehicle=()
def function_identity():
    label_id = ("ID: 1973725837, Drivers license: yes")
    print(label_id)
    label_name = ("Name: Hank J. Wimbleton")
    print(label_name)
    label_dob=("DOB: 09,22,1996")
    print(label_dob)
    label_pin=("Pin #: 092296")
    print(label_pin)
    label_address=("Address: 92296, Nevada")
    print(label_address)
    label_vehicle=("Vehicle: Four Wheeler")
    print(label_vehicle)
    
btn1 =Button(root)
btn1 = Button(root, text="Who are you?", command = function_identity)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()