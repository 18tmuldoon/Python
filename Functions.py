import random
'''
#1
num = int(input("Input a Number"))

def count(num):
    x = num
    z = 1
    while x > 0:
        print (z)
        x = x-1
        z = z+ 1
        
count(num)



#2
print(" 1) Addition", "\n", "2) Subtraction")
imp = int(input("Enter 1 or 2:"))


        

if imp == 1:
    def add1():
        def cor():
            if ans == usrAns:
                print("Correct")
            else:
                print("Incorrect")
        num1 = random.randint(5,20)
        num2 = random.randint(5,20)
        print( num1, " + ", num2)
        usrAns = int(input("Whats the answer"))
        ans = num1 + num2
        print ("Answer is = ", ans)
        cor()
    add1()
   

if imp == 2:
    def sub1():
        def cor():
            if ans == usrAns:
                print("Correct")
            else:
                print("Incorrect")
        num1 = random.randint(25,50)
        num2 = random.randint(1,25)
        print( num1, " - ", num2)
        usrAns = int(input("Whats the answer"))
        ans = num1 - num2
        print ("Answer is = ", ans)
        cor()
    sub1()
else:
    print("Invalid Input Try Again")
    
    
    
#3
    
def bet():
    def inpt():
        print("I am thinking of a number")
        guess = int(input("Input your guess"))
        
        def sme():
            if guess == comp_num:
                print("Correct, you win")
            else:
                print("Try Again")
                inpt()
        sme()
    user1 = int(input("Input a low number"))
    user2 = int(input("Input a high number"))
    
    comp_num = random.randint(user1, user2)
    print(comp_num)
        
    inpt()
        
bet()


#4
a = 0
names = ["Mark","Tom","Jacob"]
while a < 10:
    def lst():
        print(" 1) Add a Name", "\n", "2) Change a Name", "\n", "3) Delete a Name", "\n", "4) View all Names", "\n", "5) End Program")
    
        inpt = int(input("Select Option"))
    
        if inpt == 1:
            usr = input("Input Name")
            names.insert(0,usr)
            
        elif inpt == 2:
            nme = input("Select name to remove")
            pos = names.index(nme)
            nme1 = input("Input new name")
            names.insert(pos,nme1)
            names.pop(pos+1)
  
        elif inpt == 3:
            print(names)
            nme = input("Select name to remove")
            pos = names.index(nme)
            names.pop(pos)
    
        elif inpt == 4:
            print(names)
    
        elif inpt ==5:
            global a
            a = 10
    lst()
'''
#5
while p < 10:   
    print(" 1) Add to file", "\n", "2) View all records", "\n", "3) Quit program")
    inpt = int(input("Select Option"))