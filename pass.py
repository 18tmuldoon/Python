
While True:
    def Menu():
        print("1) Create a new User ID")
        print("2) Change a password")
        print("3) Display all User IDs")
        print("4) Quit")
        inp = input(int("Enter Selection:"))
        return inp

    inp = Menu()
    if inp == 1:
        
    elif inp == 2:
        
    elif inp == 3:
        
    elif inp == 4:
        break
    else:
        print("Invalid input")
        inp = Menu()