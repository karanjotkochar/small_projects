import random

user_score = 0
computer_score = 0

options = ["rock", "paper", 'scissors']

while True:
    user_input = input(
        "Kindly give the input as Rock/Paper/Scissors/Q: ").lower()

    if user_input == "q":
        break

    elif user_input not in options:
        print("Invalid option")
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissor = 2

    computer_pick = options[random_number]
    print(f"Compputer picked: {computer_pick} ")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_score += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_score += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_score += 1
    else:
        print("You Lost!")
        computer_score += 1


print(f"User Score: {user_score} ")
print(f"Computer Score: {computer_score} ")

print("GoodBye!")

# When both same - To Implement
