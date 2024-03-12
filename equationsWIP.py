from chempy import Substance
from chempy import balance_stoichiometry


def get_compound_info(compound_formula):
    compound = Substance.from_formula(compound_formula)
    return {
        'formula': compound_formula,
        'mass': compound.mass,
        'elements': compound.composition,
    }

# Example usage
compound_formula = input("Enter a chemical compound formula: ")
compound_info = get_compound_info(compound_formula)

print(f"Compound Formula: {compound_info['formula']}")
print(f"Molar Mass: {compound_info['mass']} g/mol")
print("Elemental Composition:")
for element, count in compound_info['elements'].items():
    print(f"  {element}: {count}")

#ALL BROKEN HERE
def get_compound_info(compound_formula):
    compound = Substance.from_formula(compound_formula)
    return f"Name: {compound.name}, Molar Mass: {compound.mass:.2f} g/mol"

# Get the user input
user_input = input("Enter a chemical compound equation (balancing): ")

# Separate the compounds
compounds = [compound.strip() for compound in user_input.split('+')]

# Separate the compounds into reactants and products
reactants = compounds[:len(compounds)//2]
products = compounds[len(compounds)//2:]

# Create dictionaries for reactants and products
reactants_dict = {reactant: 1 for reactant in reactants}
products_dict = {product: 1 for product in products}

# Balance the equation
balanced_equation = balance_stoichiometry(reactants_dict, products_dict)

# Print the balanced equation
print("Balanced Equation:")
print(f"{balanced_equation.reactant} = {balanced_equation.product}")

# Display information for each compound
print("\nCompound Information:")
for compound_formula in compounds:
    compound_info = get_compound_info(compound_formula)
    print(compound_info)
