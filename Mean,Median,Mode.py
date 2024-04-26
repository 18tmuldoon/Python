F_data = open("1000 random numbers for frequency.txt", "r")
C_data = open("1000 random numbers - corrupted 1", "r")
data = data = C_data.read()
dataC = []

for word in data:
    Hash = False
    Slash = False
    if data.find("#"):
    
    if data.find("/")
        
#dataC.append(data)

#While True:
def Menu():
    print("1) Calculate Mean")
    print("2) Calculate Median")
    print("3) Calculate Mode")
    print("4) Calculate Frequency")
    print("5) Quit")
    inp = int(input("Enter Selection:"))
    return inp

def mean():
    print(data)



inp = Menu()
if inp == 1:
    mean1 = mean()
    print("mean is ", mean1)
    
elif inp == 2:
    median1 = median()
    
elif inp == 3:
    mode1 = mode()
    print("Mode is ", mode1)

elif inp == 4:
    freq1 = freq()
    print("Frequancy is ", freq1) 
elif inp == 5:
    print("End")
    #break
else:
    print("Invalid input")
inp = Menu()
