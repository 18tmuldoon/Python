#Ex 8
#1
MyFloatValue = 9.82
copyInt = int(MyFloatValue)
copyStr = str(MyFloatValue)

cType = type(MyFloatValue)
IntType = type(copyInt)
StrType = type(copyStr)

print(cType , "-" , MyFloatValue)
print(IntType , "-" , copyInt)
print(StrType , "-" , copyStr)

#2
#mystr = "hi"
#myint = int(mystr)
#print(mystr)
#Traceback (most recent call last):
#  File "<string>", line 16, in <module>
#ValueError: invalid literal for int() with base 10: 'hi'

#Ex 9
#1
#year = input("Enter the current year")
#age = int(input("What age will you be at the end of this year?"))
#print("You were born in", year-age)

#Traceback (most recent call last):
#  File "<string>", line 27, in <module>
#TypeError: unsupported operand type(s) for -: 'str' and 'int'

#2
Traceback (most recent call last):
  File "<string>", line 27, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'int'