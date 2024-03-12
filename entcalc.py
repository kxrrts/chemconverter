ans_enthalpy = None
ans_entropy = None
run = False
def entcalculator():
    def enthalpy():
        reactants = []
        products = []

        while True:
            reactant_nums = input("Enter the heat of formation for your reactants (type d when done): ")
            if reactant_nums.lower() == 'd':
                break
            hf_reactants = float(reactant_nums)
            reactants.append(hf_reactants)

        while True:
            product_nums = input("Enter the heat of formation for your products (type d when done): ")
            if product_nums.lower() == 'd':
                break
            hf_products = float(product_nums)
            products.append(hf_products)

        sum_hf_reactants = sum(reactants)
        sum_hf_products = sum(products)
        ans_enthalpy = sum_hf_products - sum_hf_reactants
        return ans_enthalpy

    def entropy():
        reactants1 = []
        products1 = []

        while True:
            reactants1num = input("Enter the standard entropies of your reactants (type d when done): ")
            if reactants1num.lower() == 'd':
                break
            se_reactants = float(reactants1num)
            reactants1.append(se_reactants)

        while True:
            products1num = input("Enter the standard entropies of your products (type d when done): ")
            if products1num.lower() == 'd':
                break
            se_products = float(products1num)
            products1.append(se_products)

        sum_se_reactants = sum(reactants1)
        sum_se_products = sum(products1)
        ans_entropy = sum_se_products - sum_se_reactants
        return ans_entropy

    def spontaneity():
        print("Keep in mind this uses enthalpy and entropy from the previous sections")
        temp_spon = float(input("Input the temperature in kelvins: "))

        if ans_enthalpy is None or ans_entropy is None:
            check = input("You need both entropy and enthalpy unless you have spontaneity (press g if you have spontaneity): ")

            if check.lower() == 'g':
                deltag = float(input("Input the delta g value: "))
                ent_entr = input("Press 1 if you have entropy, press 2 if you have enthalpy: ")

                if ent_entr == '1' and ans_entropy is not None:
                    calc_spon = deltag / (-ans_entropy * temp_spon)
                elif ent_entr == '2' and ans_enthalpy is not None:
                    calc_spon = (deltag - ans_enthalpy) / (-temp_spon)
                else:
                    print("Cannot calculate spontaneity. Make sure you have valid entropy or enthalpy values.")
                    return
        else:
            calc_spon = ans_enthalpy - (ans_entropy / 1000) * temp_spon

        print("The delta g of this equation is " + str(calc_spon))
        return calc_spon

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
        enthalpy_change = input("Do you want to calculate the enthalpy change? (y/n): ")
        if enthalpy_change.lower() == 'y':
            ans_enthalpy = enthalpy()
            print("Your change in enthalpy is: " + str(ans_enthalpy))
        elif enthalpy_change.lower() == 'n':
            ans_enthalpy = None

        entropy_change = input("Do you want to calculate entropy change? (y/n): ")
        if entropy_change.lower() == 'y':
            ans_entropy = entropy()
            print("Your change in entropy is: " + str(ans_entropy))
        elif entropy_change.lower() == 'n':
            ans_entropy = None

        spon_change = input("Would you like to calculate spontaneity? (y/n): ")
        if spon_change.lower() == 'y':
            spontaneity()
        elif spon_change.lower() == 'n':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
        
        break 
entcalculator()
