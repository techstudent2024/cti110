# Isadeen Adams
# 10/08/2024
# P2LAB1
# create a budget plan

print ('Welcome to my store')

print ("T-shirt $5.00")
print ("Shorts  $9.00")
print ("Hat     $7.00")

# Ask user to enter item
item = input("What would you like to purchase?  ")
# Ask user how many do they want
amount = int(input("How many do you want? "))
# ask user price of item
print("A", item, "is how much? ")
price = float(input())


print ("-" *10, "Total amount of purchase", "-" *10)

        
print (item,"x",amount)
print (item,"$",format(price,".2f"))


answer= price * amount
print ("Your Total: $", format(answer,".2f"))
