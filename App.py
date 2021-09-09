from tkinter import *
import pandas as pd
import time
import numpy as np

pd.set_option("display.max_rows",None,"display.max_columns",None)
root = Tk()
#Global Variables
programname = 'No Fly Check'
version = '1.0.0'
nofly = 'lists/NOFLYTESTFILE.csv'
selectee = 'lists/SELECTEES.csv'

#dob_input = input("DOB")
fn_entry = Entry(root, width=30, bg='gray')
#my_entry.grid(row=0, column=0, pady=20, padx=5)
ln_entry = Entry(root, width=30, bg="gray")
fn_entry.insert(0, "First Name")
ln_entry.insert(0, "Last Name")
fn_entry.grid(row=0, column=0,pady=90,padx=10)
ln_entry.grid(row=0, column=1,pady=90,padx=100)
#userSearch= f'{ln_entry.get()}, {fn_entry.get()}'
    
root.configure(background="#D3D3D3")
root.geometry("800x500")
root.title("TSA Check 1.0.0")
root.iconbitmap('c:/desktop')

fn_input = fn_entry.get()
ln_input = ln_entry.get()

#No Fly List Series Creation
df1 = pd.read_csv(nofly)
#Line 12 defines the variable df1(dataframe 1) as the series listed in nofly, or lists/NOFLYTESTFILE.csv
print(df1)

#dob_return = df1[df1['DOB'].str.contains(dob_input)]
#print(ln_return)


def negResult():
    negResultfeed = Label(root,text="No Matches Found!")
    negResultfeed.grid(row=6,column=0)

def userClick():
    fn_return = df1[df1['FIRSTNAME'].str.contains(fn_entry.get())]
    ln_return = fn_return[fn_return['LASTNAME'].str.contains(ln_entry.get())]
    userFeedback = Label(root, text=f'Searching No Fly list for {ln_entry.get()}, {fn_entry.get()}...',bg="#D3D3D3",fg='black',pady=50)
    userFeedback.grid(row=6,column=1)
    if ln_return.empty == True:
        negResult()
    else: userResults()
    
def userResults():
    fn_return = df1[df1['FIRSTNAME'].str.contains(fn_entry.get())]
    ln_return = fn_return[fn_return['LASTNAME'].str.contains(ln_entry.get())]
    userResultfeed = Label(root, text=(ln_return[['FIRSTNAME','LASTNAME','MIDDLENAME','DOB']]),bg="white",fg='black',pady=10,width=50)
    userResultfeed.grid(row=10,column=1)

submitButton = Button(root, text="Search", command=userClick)
submitButton.grid(row=5, column=1)


root.mainloop()
