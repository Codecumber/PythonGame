# Rock, Paper, Scissors
import random

list1 = ("r", "p", "s")

Total_Chances = 10
No_Of_Chances = 0
Computer_Points = 0
Human_Points = 0
print(" \t \t \t \t Rock, Paper, Scissors Game \n \n")
print("r for rock \np for paper\ns for scissors \n")

while No_Of_Chances < Total_Chances:
    _input = input("Rock, Paper, Scissors: ")
    _random = random.choice(list1)
    if _input == _random:
        print("Tie Both 0 point to each \n")

    # If user enters r
    elif _input == "r" and _random == "p":
        Computer_Points = Computer_Points + 1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print("Computer wins 1 point \n")
        print(f"Computer_Points are {Computer_Points} and your points are {Human_Points} \n")

    elif _input == "r" and _random == "s":
        Human_Points = Human_Points + 1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"Computer_Points are {Computer_Points} and your points are {Human_Points} \n ")

    # If user enters p
    elif _input == "p" and _random == "s":
        Computer_Points = Computer_Points + 1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"Computer_Points are {Computer_Points} and your points are {Human_Points} \n")

    elif _input == "p" and _random == "r":
        Human_Points = Human_Points + 1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"Computer_Points are {Computer_Points} and your points are {Human_Points} \n")

    # If user enters s
    elif _input == "s" and random == "r":
        Computer_Points = Computer_Points + 1
        print(f"Your guess is {_input} and computer guess is {_random} \n")
        print("Computer wins 1 point \n")
        print(f"Computer_Points are {Computer_Points} and your points are {Human_Points} \n ")

    elif _input == "s" and random == "p":
        Human_Points = Human_Points + 1
        print(f"Your guess is {_input} and computer guess is {_random} \n")
        print("Computer wins 1 point \n")
        print(f"Computer_Points are {Computer_Points} and your points are {Human_Points} \n ")

    else:
        print("you have given wrong input \n")

    No_Of_Chances = No_Of_Chances + 1
    print(f"{Total_Chances - No_Of_Chances} is left out of {Total_Chances} \n")

print("Game over")

if Computer_Points == Human_Points:
    print("Tie")

elif Computer_Points > Human_Points:
    print("Computer wins and you lost")

else:
    print("You win and computer lost")

print(f"Your points are {Human_Points} and computer's points are {Computer_Points}")

