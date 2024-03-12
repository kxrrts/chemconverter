import periodictable 
import re 
from periodictable import * 
from onestep import conversioncalc #imports the conversion function 
from idealgas import idealgaslawcalc #imports the ideal gas law function 
from entcalc import entcalculator #imports the enthalpy calculator function 

run = False 

while True:
        starting = input("Do you want to start the calculator? (y/n): ")
        if starting.lower() == 'y':
            run = True
            break
        elif starting.lower() == 'n':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
while run: 
    choices = input("Press 1 for conversions, 2 for enthalpy calculator, and 3 for ideal gas laws ") 
    if choices == '1': 
         conversioncalc() 
    elif choices == '2': 
         entcalculator()
    elif choices == '3': 
         idealgaslawcalc() 
    else: 
         break 


