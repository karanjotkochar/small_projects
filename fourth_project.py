name = input("Enter your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("Left or Right? ").lower()

if answer == "left":
    print("You are on left")

    answer = input("Walk or Swim? ").lower()
    if answer == "walk":
        print("You are walking")
    elif answer == "swim":
        print("You are swimming")
    else:
        print("Not valid option")


elif answer == "right":
    print("You are on right")

    answer = input("Cross or Back? ").lower()
    if answer == "cross":
        print("You are crossing")

        answer = input("Talk or not to stranger, yes or no? ")
        if answer == "yes":
            print("You are talking")
        elif answer == "no":
            print("You are not talking")
        else:
            print("Not valid option")

    elif answer == "back":
        print("You are going back")
    else:
        print("Not valid option")

else:
    print("Not valid option")

print(f"Thank you {name}.")
