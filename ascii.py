character = input("Input a character")

asValue = ord(character)
print("The ASCII value of ", character, "is: ", asValue)

Uni = int(input("Input a Unicode value"))
UniValue = chr(Uni)
print("The Unicode related character is ", UniValue)

message = ("abcdefghijklmonopqrstuvwxyz")

leng = len(message)
x = 0
output = []

while leng > 0 :
    y = ord(message[x])
    t = y+2
    if t > 122:
        t -= 26
    q = chr(t)
    output.append(q)
    x = x+1
    leng = leng-1
    
print(output)
