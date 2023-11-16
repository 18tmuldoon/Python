#Caesar Cipher
#abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C"]
abc = ("ABCDEFGHIJKLMNOPQRSTUVWXYZABC")
userI = input("Input Message")
keyNum = int(input("Input Key Number"))
EncDec = input("Encode or Decode")


t1 = len(userI)
userIn = list(userI)
t = -1

if EncDec == "Decode":
    while t <= t1:
        n = 0
        t = t + 1
        while n < 26:
            if userIn[t] == abc[n]:
                print(abc[n+keyNum])
            n = n+1

            