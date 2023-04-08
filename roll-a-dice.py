import random;
roll = input("To roll the dice enter y")

while(roll == "y"):
  n = random.randint(1,6)
  break

if(n == 1):
    print("     ")
    print("  0  ")
    print("     ")
    print()
    roll = input("You rolled a 1, press y to continue or press n to exit")

    if(roll == "y"):
        roll = input("To roll the dice enter y")
    elif(roll == "n"):
        print("Thanks for rolling")

elif(n == 2):
    print("0    ")
    print("     ")
    print("    0")
    print()
    roll = input("You rolled a 2, press y to continue or press n to exit")

    if(roll == "y"):
        roll = input("To roll the dice enter y")
    elif(roll == "n"):
        print("Thanks for rolling")

elif(n == 3):
    print("0    ")
    print("  0  ")
    print("    0")
    print()
    roll = input("You rolled a 3, press y to continue or press n to exit")

    if(roll == "y"):
        roll = input("To roll the dice enter y")
    elif(roll == "n"):
        print("Thanks for rolling")

elif(n == 4):
    print("0   0")
    print("     ")
    print("0   0")
    print()
    roll = input("You rolled a 4, press y to continue or press n to exit")

    if(roll == "y"):
        roll = input("To roll the dice enter y")
    elif(roll == "n"):
        print("Thanks for rolling")

elif(n == 5):
    print("0   0")
    print("  0  ")
    print("0   0")
    print()
    roll = input("You rolled a 5, press y to continue or press n to exit")   

    if(roll == "y"):
        roll = input("To roll the dice enter y")
    elif(roll == "n"):
        print("Thanks for rolling")

else:
    print("0   0")
    print("0   0")
    print("0   0")
    print()
    roll = input("You rolled a 6, press y to continue or press n to exit") 

    if(roll == "y"):
        roll = input("To roll the dice enter y")
    elif(roll == "n"):
        print("Thanks for rolling")

    


