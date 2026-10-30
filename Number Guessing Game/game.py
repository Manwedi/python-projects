import random

number_to_guess = random.randint(1,1000)

#loop
try:
    guess = int(input("Guess a number between 1 and 1000: "))
except ValueError:
    print("Please enter a number only!")
    if guess < number_to_guess:
        print("Number is way too high")
    elif guess > number_to_guess:
        print("Number is way too low")

#break