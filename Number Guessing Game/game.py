import random

number_to_guess = random.randint(1,1000)

#loop
while True:
    try:
        guess = int(input("Guess a number between 1 and 1000: "))
        if guess > number_to_guess:
            print("Number is way too high")
        elif guess < number_to_guess:
            print("Number is way too low")
        else:
            print("Awesome!! you've gussed the number")
        break
except ValueError:
