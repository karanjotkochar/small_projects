print("Welcome to the game")

game = input("Do you want to play? ")

if game != "yes":
    quit()

print("Great Let's play")
score = 0

question1 = input("What is CPU ")

if question1.lower() == "central processing unit":
    print("great")
    score += 1
else:
    print("oops")

print(f"Score = {score} ")
