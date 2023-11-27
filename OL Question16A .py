# Question 16(a)
# Student Name:
#This program is a simple ordering system
print("Welcome to the new online ordering system.\n")
name = input("Please enter your user name: ")
total_cost=0
item_count=0

numORD = int(input("How many items are in the customers order: "))
if numORD < 0:
    print("Invalid option")
    
i = 0

while i < numORD:
    item_count = item_count + 1
    print("Enter the price of item ", item_count, " :")
    inp = int(input("$ "))
    total_cost = total_cost + inp
    i = i + 1

print("You entered",item_count,"items and the total is €",total_cost)
print("The member of staff who processed your order was: " , name)


balance = int(input("What is the customers current account balance $ "))

if balance >= total_cost:
    balance = balance - total_cost
    print("Your remaining balance: ", balance)
else:
    balance = balance - total_cost
    owe = balance - balance - balance
    print("The customer does not have enough credits in their account, they still owe: $", owe)



