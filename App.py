#----IMPORTED LIBRARIES----
from tkinter import *
import pandas as pd
import time
import numpy as np

#----GUI CONFIG----
root = Tk()
root.configure(background="#D3D3D3")
root.geometry("900x400")
root.title("TSA Check 1.0.0")

#----USER INPUT BOXES---
fn_entry = Entry(root, width=30, bg='gray')
ln_entry = Entry(root, width=30, bg="gray")

fn_entry.insert(0, "First Name")
ln_entry.insert(0, "Last Name")

fn_entry.grid(row=0, column=0,pady=10,padx=10)
ln_entry.grid(row=1, column=0,pady=2,padx=100)

#----USER INPUT FETCH----
fn_input = fn_entry.get()
ln_input = ln_entry.get()

#----NO FLY DATAFRAME----
nofly = 'lists/NOFLYTESTFILE.csv'
df1 = pd.read_csv(nofly)

#----SELECTEE DATAFRAME----
selectee = 'lists/SELECTEES.csv'

#----SUBMIT BUTTON----
def userClick():
    fn_return = df1[df1['FIRSTNAME'].str.contains(fn_entry.get())]
    ln_return = fn_return[fn_return['LASTNAME'].str.contains(ln_entry.get())]
    userFeedback = Label(root,text=f'Searching No Fly list for {ln_entry.get()}, {fn_entry.get()}',bg='#D3D3D3',fg='black',pady=50)
    userFeedback.grid(row=6,column=1)
    if ln_return.empty == True:
        negResult()
    else: userResults()

def negResult():
    negResultfeed = Label(root,text="No Matches Found!")
    negResultfeed.grid(row=6,column=0)

def userResults():
    fn_return = df1[df1['FIRSTNAME'].str.contains(fn_entry.get())]
    ln_return = fn_return[fn_return['LASTNAME'].str.contains(ln_entry.get())]
    userResultfeed = Label(root, text=(ln_return[['FIRSTNAME','LASTNAME','MIDDLENAME','DOB']]),bg="white",fg='black',pady=10,width=50)
    userResultfeed.grid(row=10,column=0)

submitButton = Button(root, text="Search", command=userClick,width=20,pady=20)
submitButton.grid(row=5, column=1,pady=20)


root.mainloop()
