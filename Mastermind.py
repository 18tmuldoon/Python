import random

colours = ["red", "blue", "green", "pink", "purple", "yellow", "orange"]


comChoice = []
usrChoice = []
corr = 0
n = 0

x = 4
while x > 0:
    comChoice.append(random.choice(colours))
    x = x-1

#print(comChoice)

x = 4
while x > 0:
    usrInp = input("Input colour: ")
    usrChoice.append(usrInp)
    x = x-1

#print(usrChoice)

x = 4
while x > 0:
    if comChoice[n] == usrChoice[n]:
        corr = corr + 1
    n = n + 1
    x = x-1
 
n = 0
m = 0
cW = 0
x = 16
while x > 0:
    if comChoice[m] == usrChoice[n]:
        cW = cW + 1
    n = n+1
    if n == 4:
        m = m+1
        n = 0

    x = x-1   

cW = cW - corr

print("Correct colour in the Correct position: ", corr)
print("Correct colour in the Wrong position: ", cW)