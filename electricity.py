#ELECTRICITY BILL CALCULATOR

#WRITE A PROGRAM THAT CALCULATES THE ELECTRICITY BILL BASED ON THE NUMBER OF UNITS CONSUMED. THE BILLING RATES ARE AS FOLLOWS:

#- For the first 100 units: 25 per unit

#- For the next 100 units (101-200): 35 per unit

#- For the next 100 units (201-300): 45 per unit

units = float(input("Enter the unit consumed: "))
if units <= 100:
    total_bill = units * 25
    print(f"The amount for {units} units consumed is Ksh {total_bill}")

elif units <= 200:
    total_bill = (100 * 25) + ((units - 100) * 35)
    print(f"The amount for {units} units consumed is Ksh {total_bill}")

elif units <= 300:
    total_bill = (100 * 25) + (100 * 35) + ((units - 200) * 45)
    print(f"The amount for {units} units consumed is Ksh {total_bill}")

else:
    total_bill = (100 * 25) + (100 * 35) + ((units - 200) * 45)
    print(f"The amount for the {units} units consumed is Ksh {total_bill}")
    

