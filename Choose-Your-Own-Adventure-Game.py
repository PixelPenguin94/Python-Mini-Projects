# 4) Project Level (Easy)

name = input("Type your name: ")
print("Welcome", name, "To this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?: "
).lower()

if answer == "left":
    answer = input(
        "You are near a river. You want to walk around it or swim across? Type walk or swim: "
    ).lower()

    if answer == "swim":
        print("You swam across the river and were eaten by crocodiles. You lose!")
    elif answer == "walk":
        print("You walked for a long time and encountered bandits. You lose!")
    else:
        print("Invalid option.")

elif answer == "right":
    answer = input(
        "You come to a bridge, it is wobbly, do you want to cross it or head back? Type cross or back: "
    ).lower()

    if answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you want to talk to them (yes/no)?"
        ).lower()

        if answer == "yes":
            print("They give you gold and treasure map! You WIN!")

        elif answer == "no":
            print("They stranger gets offended. You lose!")

        else:
            print("Invalid option.")
    elif answer == "back":
        print("You go back. You lose!")
    else:
        print("Invalid option.")

else:
    print("Not a valid option. You lose.")
