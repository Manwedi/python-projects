#MANWEDI CLAUDE
import random

#Ask: Roll the dice?
while True:
    choice = input("Begin dice roll? (Y/N): ")
#Loop
    if choice == "Y" or choice == "y":
        dice1 = random.randint(1, 6)  #Random integer Generator
        dice2 = random.randint(1, 6)
        print(f"({dice1}, {dice2})")
    elif choice == "N":
        print("Thanks for playing")
        break
    else:
        print("Invalid Choice")