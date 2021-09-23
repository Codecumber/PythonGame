# Rock, Paper, Scissors game
import random

game_list = ("r", "p", "s")

Total_Chances = 10
No_Of_Chances = 0
Computer_Points = 0
Human_Points = 0
print("\nHello, this game is developed by Codecumber.\n")
print(" \t \t \t \t Rock, Paper, Scissors Game \n \n")
print("r for rock \np for paper\ns for scissors \n")

while No_Of_Chances < Total_Chances:
      game= input("Rock, Paper, Scissors: ")
      _random = random.choice(game_list)

      if game == _random:
         print("That's a tie! 0 points to each \n")

    #If user enters r
      elif game == "r" and _random == "p":
           Computer_Points = Computer_Points + 1
           print(f"Your guess is {game} and Computer's guess is {_random} \n")
           print("Computer wins 1 point \n")
           print(f"Computer's Points are {Computer_Points} and your points are {Human_Points} \n")

      elif game == "r" and _random == "s":
           Human_Points = Human_Points + 1
           print(f"Your guess is {game} and Computer's guess is {_random} \n")
           print("Human wins 1 point \n")
           print(f"Computer's Points are {Computer_Points} and your points are {Human_Points} \n ")

    # If user enters p
      elif game == "p" and _random == "s":
           Computer_Points = Computer_Points + 1
           print(f"Your guess is {game} and Computer's guess is {_random} \n")
           print("Human wins 1 point \n")
           print(f"Computer's Points are {Computer_Points} and your points are {Human_Points} \n")

      elif game == "p" and random == "r":
           Human_Points = Human_Points + 1
           print(f"Your guess is {game} and Computer's guess is {_random} \n")
           print("Human wins 1 point \n")
           print(f"Computer's Points are {Computer_Points} and your points are {Human_Points} \n")

    # If user enters s
      elif game == "s" and _random == "r":
           Computer_Points = Computer_Points + 1
           print(f"Your guess is {game} and computer's guess is {_random} \n")
           print("Computer wins 1 point \n")
           print(f"Computer's Points are {Computer_Points} and your points are {Human_Points} \n ")

      elif game == "s" and _random == "p":
           Human_Points = Human_Points + 1
           print(f"Your guess is {game} and computer's guess is {_random} \n")
           print("Computer wins 1 point \n")
           print(f"Computer's Points are {Computer_Points} and your points are {Human_Points} \n ")

      else:
           print("You have given wrong input.\n")

      No_Of_Chances = No_Of_Chances + 1
      print(f"{Total_Chances - No_Of_Chances} is left out of {Total_Chances} \n")

print("Game over")

if Computer_Points == Human_Points:
   print("Tie!")

elif Computer_Points > Human_Points:
     print("Computer wins and you lost!")

else:
    print("You won and computer lost!")

print(f"Your points are {Human_Points} and computer's points are {Computer_Points}")
# Rock Paper Scissors Game in Python
# The rock hits scissors, paper wraps the rock, and scissors cuts paper.

