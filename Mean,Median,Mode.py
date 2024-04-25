F_data = open("1000 random numbers for frequency.txt", "r")
C_data = open("1000 random numbers - corrupted 1", "r")


#While True:
def Menu():
    print("1) Calculate Mean")
    print("2) Calculate Median")
    print("3) Calculate Mode")
    print("4) Calculate Frequency")
    print("5) Quit")
    inp = int(input("Enter Selection:"))
    return inp

inp = Menu()
if inp == 1:
    print(C_data.read())
elif inp == 2:
    
elif inp == 3:

elif inp == 4:
    
elif inp == 5:
    break
else:
    print("Invalid input")
inp = Menu()
