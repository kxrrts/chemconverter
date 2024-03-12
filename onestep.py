import periodictable 
import re 
from periodictable import *
#from equationsWIP import get_compound_info 
def conversioncalc():
    avgnumber = 6.022e23

    element = input("Which element would you like to access? ") 


    #setting up for exponents 
    def parse_exponent(input_str): 
        import re

    def parse_exponential_input(input_str):
        match = re.match(r'^([\d.]+)x10\^(\d+)$', input_str)
        if match:
            coefficient, exponent = map(float, match.groups())
            return coefficient * (10 ** exponent)
        else:
            raise ValueError("Invalid input format. Please enter a number in the form '5.023x10^6'.")



    #grabbing the correct element from the library
    try: 
        selected_element = periodictable.elements.symbol(element)
        molar_mass = selected_element.mass

        print(f"The molar mass of {selected_element.name} ({selected_element.symbol}) is {molar_mass:.4f} g/mol.")
    except ValueError:
        print(f"Element with symbol {element} not found.")



    #converting to moles from grams or atoms
    def grams_atoms_moles(selected_element): 
        if options == "1": 
            value1 = input("How many grams of this element do you have ")  
        elif options == "3": 
            value1 = input("How many atoms of this element do you have? (Express exponents as 5.02x10^3) ")
            try:
                valueE = parse_exponential_input(value1)
            except ValueError as e:
                print(e)
                exit()
            ans = (valueE)/avgnumber*selected_element.mass
        #considers options 2 and 4 now 
        elif options == "2" or options == "4": 
            value1 = input("How many moles of this element do you have? ")
            choice1 = input("Press x to convert to atoms or y to convert to grams ")
            if choice1 == "y":
                ans = float(value1)*selected_element.mass
            else: 
                try:
                    valueE = parse_exponential_input(value1) #runs exponent check again 
                except ValueError as e:
                    print(e)
                    exit()
                ans = float(value1)*avgnumber #multiplies moles by conversion factor of 6.022 ** 23 for one mole 
        else:
            ans = float(value1)/selected_element.mass 
        print(str(ans) + "is your answer. (Double check units)")
        return ans 
    #converting from liters to grams, moles, and even atoms 
    def liters(selected_element): 
        value2 = input("How many moles of this element do you have (Liter conversion)? ") 
        volume_ml = 1 
        value2 = selected_element.density / selected_element.mass
        ans = 1 / value2 * volume_ml
        print(str(ans))
        return ans 

    #compound conversion 
    #def compounds(compound_formula): 
        compound_info = get_compound_info(compound_formula)
        print(compound_info)

    #lets the user chose which converting calculations to perform 
    options = input("What would you like to convert from? 1. Grams -> Moles 2. Moles -> Grams 3. Atoms -> Moles 4. Moles -> Atoms 5. Liters to Grams, Moles, Atoms ")
    if options in ["1", "2", "3", "4"]:
        grams_atoms_moles(selected_element)
    elif options == "5": 
        liters(selected_element)
