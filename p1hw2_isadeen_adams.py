# Isadeen Adams
# 10/08/2024
# P2LAB1
# create a budget plan

print ('This program calculates and displays travel expenses')

# Ask user to enter their budget
budget = float(input("What is your travel budget? $ "))
# Where are they going
destination = input("Where are you going? ")
# Gas amount?
gas = int(input("How much on gas? $ "))
# How much for accommodation/hotel? 
accomodation = int(input('How much for acommodation/hotel? $ '))
# Ask amount for food
food = int (input('How much for food? $ '))
# Add all expenses

print ("-" *10, "Travel Expenses", "-" *10)
print ("Location:",input(destination))
print ("Initial Budget: $",format(budget,".2f"))

print ("Fuel: $", format(gas,".2f"))
print ("Accomodation: $", format(accomodation,".2f"))
print ("Food: $", format(food,".2f"))

expenes= gas + accomodation + food
answer= budget - expenes
print ("Remaining Balance: $", format(answer,".2f"))





