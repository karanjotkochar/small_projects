import random

# random.randrange

# random.randint

top_number = input("Enter top limit value: ")

if top_number.isdigit():
    top_number = int(top_number)

    if top_number <= 0:
        print("Enter number greater than 0")
        quit()
else:
    print("Type number next time")
    quit()

random_value = random.randint(0, top_number)
guess = 0

while True:
    guess += 1
    user_guess = input("Enter Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Eenter number next time")
        continue

    if user_guess == random_value:
        print("You got it")
        break
    elif user_guess < random_value:
        print("Make guess high")
    else:
        print("Make guess less")

print(f"You got it in {guess} guesses.")
