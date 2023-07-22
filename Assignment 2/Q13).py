#Q13). Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
'''  Unit                                                     Price
First 100 units                                             no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)'''

no_of_units = int(input("Enter num of units consumed by user: "))
Charge=0
if no_of_units <=100:
    print("No charge till 100 units")

elif no_of_units > 100 and no_of_units < 200:
    Charge = (no_of_units -100)*5
    print("Total bill: ",Charge)

else:
    Charge = 500 + (no_of_units - 200)*10
    print("Total bill: ", Charge)







