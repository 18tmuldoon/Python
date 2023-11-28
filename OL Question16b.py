# Question 16_b
# Student Name: Thomas Muldoon 

Standard_Postal_List=["Netherlands", "Finland", "Greece", "Ireland", "Hungary", "Denmark", "Romania", "Spain", "France", "Poland", "Sweden", "Germany", "Portugal"]

country1 = str(input("Please entre the country that you wish to send the order to: "))

if country1 in Standard_Postal_List:
    print("This country is on the approved delivery list.")
    
else:
    print("This country is not on the approved delivery list.")
    
    add = input("Do you want to add this to the Standard Postal List? y/n: ")
    if add == "y":
        Standard_Postal_List.append(country1)
        print(country1, " has been added to Standard Postal List")
    else:
        print(country1, " has NOT been added to Standard Postal List")
    

print(Standard_Postal_List)
