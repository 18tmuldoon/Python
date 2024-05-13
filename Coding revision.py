#1
lst = []
for x in range(0 , 5):
    lst.append(int(input("Input a number")))
    
for x in range(0 , len(lst)):
    lst[x] += 1
    print(lst)

#2
hours = []
for x in range(0 , 7):
    hours.append(int(input("Input hours in day")))

week = 0

for x in range(0 , len(hours)):
    week = week + (hours[x] * .5)
    
print(week)

cost = week * 1.35

print("Steven drinks ", week, " litres of milk a week")
print("Steven owes ", cost, " a week")

#3
msr = []
for x in range(0 , 7):
    msr.append(int(input("Input measurments")))

total1 = sum(msr)
print("The total rainfall for the week is ", total1 , "cm")

for x in range(0 , len(msr)):
    if msr[x] > 3.5:
        print("Day ", x , " excedes 3.5cm of rainfall")


#4
nsales = int(input("Input the amount of sales people"))
names = []
sales = []

for x in range (0 , nsales):
    names.append(input("Input the name of employee"))
    sales.append(int(input("Input the value of this employees sales")))

max1 = max(sales)
min1 = min(sales)
total2 = sum(sales)
avgS = total2 / len(sales)

print("Total sales = ", total2)
print("Max sales by any one salesperson = ", max1)
print("Min sales by any one salesperson = ", min1)
print("Average sales = ", avgS)

