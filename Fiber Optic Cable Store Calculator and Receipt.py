# DSC510
# Programming Assignment Week 3
# Sarah Theriot
# 6/18/2024

# Change Log
# Change 1:
# Change Made: Modified IF statements to add functions
# Date of Change: 6/26/2024
# Author: Sarah Theriot

def get_name():
    name = input("What is the name of your company? ")
    return name


def calculate_installation_cost(feet, price_per_foot):
    try:
        feet = float(feet)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()
    else:
        installation_cost = feet * price_per_foot
        return installation_cost


def main():
    # Print welcome message to user
    print("Welcome to The Fiber Optic Cable Store!\n")
    # Get company name from user
    company_name = get_name()
    # Get number of feet of cable needed
    feet_needed = input("How many feet of fiber optic cable do you need installed?")

    # Calculate cost of installation
    if float(feet_needed) <= 100:
        price_per_foot = 0.87
    elif float(feet_needed) <= 250:
        price_per_foot = 0.80
    elif float(feet_needed) <= 500:
        price_per_foot = 0.70
    else:
        price_per_foot = 0.50

    installation_cost = calculate_installation_cost(feet_needed, price_per_foot)

    # Print a receipt for the user
    print("\nReceipt:")
    print("**************************")
    print("Company Name:", format(company_name))
    print("Feet of Fiber Optic Cable Ordered:", format(feet_needed))
    print("Installation Cost: $", format(installation_cost, '.2f'))
    print("Total Cost: $", format(installation_cost, '.2f'))
    print("Thank you for using The Fiber Optic Cable Store", format(company_name))


if __name__ == "__main__":
    main()
