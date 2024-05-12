def menu():
    print("1) Make a Code")
    print("2) Decode a message")
    print("3) Quit")
    
    usr = int(input("Enter your selection"))
    return usr

def encode(uncode):
    code = ""
    for x in uncode:
            if x != " ":
                n = ord(x) + 1
                if n == 123:
                    n -= 26
                elif n == 91:
                    n -= 26
                elif n == 58:
                    n -= 10
                m = chr(n)
                code = code + m
            elif x == " ":
                code = code + x
    return code

def decode(deco):
    code = ""
    for x in deco:
        if x != " ":
            n = ord(x) - 1
            if n == 96:
                n += 26
            elif n == 64:
                n += 26
            elif n == 47:
                n += 10
            m = chr(n)
            code = code + m
        elif x == " ":
            code = code + x
    return code
    
while True:
    choice = int(menu())
    if choice  == 1:
        uncode = input("Input what you wish to code")
        coded = encode(uncode)
        print(coded)
        
    if choice == 2:
        deco = input("Input what you wish to decode")
        uncoded = decode(deco)
        print(uncoded)
        
    if choice == 3:
        break
