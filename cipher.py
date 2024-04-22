while True:
    def menu():
        print("1) Make a Code")
        print("2) Decode a message")
        print("3) Quit")
        
        usr = input(int("Enter your selection"))
        return usr
        
    choice = menu()
    if choice  == 1:
        