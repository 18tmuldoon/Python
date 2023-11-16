#Ex 0
runningTotal = 0
p1 = 12
p2 = 24
p3 = 36
p4 = 48

runningTotal = p1 + runningTotal
runningTotal = p2 + runningTotal
runningTotal = p3 + runningTotal
runningTotal = p4 + runningTotal

print(runningTotal)

#Ex 1
fin = open("daffodils.txt")
for line in fin:
    print(line.strip())
fin.close()

#Ex 2
rt = 0
fin = open("daffodils.txt")
for line in fin:
    rt = rt + 1
fin.close()
print("number of lines is ", rt)

#Ex 3
af = 0
afn = 0
ad = 0
adn = 0
fin = open("num_calc_1.txt")
for line in fin:
    line = line.strip()
    if(line.isdigit()):
     x = int(line)
     af = af+x
     afn = afn+1
fin.close()

fin = open("num_calc_2.txt")
for line in fin:
    line = line.strip()
    if(line.isdigit()):
     x = int(line)
     ad = ad+x
     adn = adn+1
fin.close()

tot = af+ad
ton = afn+adn
mean = tot//ton
print("mean is ", mean)

#Ex 4
total = 0
y = 20
while y>0:
    user = int(input("Input Number"))
    total = total + user
    y = y-1
print(total)

#Ex 5
y1 = 10
fin = open("file1.txt","w")
while y1>0:
    user1 = input("Input Number")
    fin.writelines(user1)
    fin.writelines("\n")
    y1 = y1-1
fin.close()
af = 0
afn = 0
ad = 0
adn = 0
fin = open("num_calc_1.txt")
for line in fin:
    line = line.strip()
    if(line.isdigit()):
     x = int(line)
     af = af+x
     afn = afn+1
fin.close()
af1 = 0
afn1 = 0
ad1 = 0
adn1 = 0
fin = open("file1.txt")
for line in fin:
    line = line.strip()
    if(line.isdigit()):
     x1 = int(line)
     ad1 = ad1+x1
     adn1 = adn1+1
fin.close()

tot1 = af1+ad1
ton1 = afn1+adn1
mean1 = tot1//ton1
print("mean is ", mean1)


