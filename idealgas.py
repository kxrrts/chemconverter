import math 


def idealgaslawcalc():
    #this is the ideal gas constant 
    r = float(0.00821)

    # receives at least three of the PV=nRT components
    pressure = input("What is the pressure (if none put n) ")
    volume = input("What is the volume (if none put n) ")
    moles = input("How many moles do you have? (If none put n) ")
    temp = input("What is the temperature in kelvins? ")

    #solves for the missing variable 
    def calculations():
        ans = None
        #sets a handle for the instance where n > 1 
        unknowns = [pressure, volume, moles, temp].count("n") 
        if  unknowns == 2: 
            print("You must need at least 3 parts to solve for the fourth variable.")
        elif unknowns == 1: 
            if pressure == 'n':
                ans = float(float(moles) * float(temp) * r / float(volume))
            elif volume == 'n':
                ans = float(float(moles) * float(temp) * r / float(pressure))
            elif moles == 'n':
                ans = float(float(pressure) * float(volume) / (float(temp) * r))
            elif temp == 'n':
                ans = float(float(pressure) * float(volume) / (float(moles) * r))
        else: 
            print("You already have everything found.")
        print(str(ans))
        return ans

#ideal gas law conversions 
convert = input("Would you like to perform pressure conversions? (y/n) ")
kPa = float(101.3) 
barometic = float(760.0)