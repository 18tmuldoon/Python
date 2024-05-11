F_data = open("1000 random numbers for frequency.txt", "r")
C_data = open("1000 random numbers - corrupted 1", "r")
data = C_data.read()
Fdata = F_data.read()

xnumbers = []
ynumbers = []

numbers = data.split()

Fr = Fdata.split(",")

for x in numbers:
    if "/" not in x and "#" not in x:
        xnumbers.append(x)
    else:
        ynumbers.append(x)

for x in ynumbers:
    if "#" in x:
        z = data.index(x)
        w = (int(numbers[z-1]) + int(numbers[z+1])) //2
        xnumbers.append(w)


for x in range(0, len(xnumbers)):
    xnumbers[x] = round(float(xnumbers[x]))
    
xnumbers.sort()


#While True:
def Menu():
    print("1) Calculate Mean")
    print("2) Calculate Median")
    print("3) Calculate Mode")
    print("4) Calculate Frequency")
    print("5) Quit")
    inp = int(input("Enter Selection:"))
    return inp

def mean(xnumbers):
    mean1 = sum(xnumbers)/len(xnumbers)
    return mean1

def median(xnumbers):
    if len(xnumbers) % 2 == 0:
        median1 = (xnumbers[len(xnumbers)//2 - 1] + xnumbers[len(xnumbers)//2]) / 2
    else:
        median1 = xnumbers[len(xnumbers)//2]
    return median1

def mode(xnumbers):
    counts = {}
    y = 0
    w = None
    for x in xnumbers:
        if x in counts:
            counts[x] += 1
        else :
            counts[x] = 1
            
        if counts[x] > y:
            y = counts[x]
            w = x

    return w


def freq(Fdata):
    Ftbl = {}
    
    for x in Fdata:
        if x == ",":
            continue
        elif x in Ftbl:
            Ftbl[x] += 1
        elif x not in Ftbl:
            Ftbl[x] = 1
        
    return Ftbl

while True:
    inp = Menu()
    
    if inp == 1:
        mean1 = mean(xnumbers)
        print("Mean is ", mean1)
        
    elif inp == 2:
        median1 = median(xnumbers)
        print("Median is ", median1)
        
    elif inp == 3:
        mode1 = mode(xnumbers)
        print("Mode is ", mode1)
        inp = Menu()
        
    elif inp == 4:
        freq1 = (freq(Fdata))
        #print("Frequancy is ", freq1)
        print(" Number ", " Frequency")
        for num, frequancy in freq1.items():
            print(f'    {num}        {frequancy}')
        
    elif inp == 5:
        print("End")
        break
    else:
        print("Invalid input")
