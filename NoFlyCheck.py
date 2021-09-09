#Imported Libraries
import pandas as pd
import time
import numpy as np
#Global Variables
programname = 'No Fly Check'
version = '1.0.0'
nofly = 'lists/NOFLYTESTFILE.csv'
selectee = 'lists/SELECTEES.csv'

fn_input = input("First Name")
ln_input = input("Last Name")
#dob_input = input("DOB")
#requestingbase = input("Requesting Base")
#User = input("User Name")
#run
print(f'Initializing {programname} {version}...')
#No Fly List Series Creation
df1 = pd.read_csv(nofly)
#Line 12 defines the variable df1(dataframe 1) as the series listed in nofly, or lists/NOFLYTESTFILE.csv
print(df1)
fn_return = df1[df1['FIRSTNAME'].str.contains(fn_input)]
ln_return = fn_return[fn_return['LASTNAME'].str.contains(ln_input)]
#dob_return = df1[df1['DOB'].str.contains(dob_input)]
#print(ln_return)
if ln_return.empty == True:
    print('No Matchest Found!')
else: print(ln_return)
