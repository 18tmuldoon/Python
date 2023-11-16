runningTotal = 0
price1 = 10
price2 = 14

runningTotal = price1 + runningTotal

runningTotal = price2 + runningTotal

print(runningTotal)

fin = open("myfile.txt")
print(fin)
for line in fin:
    print(line.strip())
    
for line in fin:
    print(line.strip())
fin.close()