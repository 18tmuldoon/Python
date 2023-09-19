#1
name = input("Enter Your Name")
ln = len(name)
print("length of 1st name is ", ln)

#2
Lname = input("Enter Your Last Name")
Fname = name + " " + Lname
print(Fname)

#3
Nrhyme = input("Enter Line of Nursery Rhyme")
LenNr = len(Nrhyme)
print("length of line is ", LenNr)
num1 = int(input("Input 1st number"))
num2 = int(input("Input 2nd number"))
k = Nrhyme[num1:num2]
print(k)

#4
word = input("Enter a lowercase word")
wordU = word.upper()
print(wordU)

#5
if ln < 5:
    Fname = name + Lname
    Fname = Fname.upper()
    print(Fname)
elif ln > 5:
    name = name.lower()
    print(name)

#6
word2 = input("Enter a word")
Fword = word2[0]
lenword = len(word2)
vowel = ["a","e","i","o","u","A","E","I","O","U"]
vowelL = len(vowel) - 1
end = ""

if Fword in vowel:
    end = "way"
