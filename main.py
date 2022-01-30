rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.")

game_images = [rock, paper, scissors]

user_input = int(input())

random_choice = random.randint(0,2)

# if user_input == 0:
#   print(rock)
# elif user_input == 1:
#   print(paper)
# else:
#   print(scissors)

if user_input > 2:
  print("You typed invalid number you lose...!!!") 
else:
  print(game_images[user_input])
   

  print(f"\nComputer chose:\n")

  # if random_choice == 0:
  #   print(rock)
  # elif random_choice == 1:
  #   print(paper)
  # else:
  #   print(scissors)

  print(game_images[random_choice])

  if user_input == 0:

    if random_choice == 0:
      print("It's Draw 📍")
    elif random_choice == 1:
      print("You lose ☹️")
    else:
      print("You win 🥳👏👏")

  elif user_input == 1:

    if random_choice == 1:
      print("It's Draw 📍")
    elif random_choice == 0:
      print("You Win 🥳👏👏")
    else:
      print("You lose ☹️")
  elif user_input == 2:
    if random_choice == 2:
      print("It's Draw 📍")
    elif random_choice == 0:
      print("You Lose ☹️")
    else:
      print("You Win 🥳👏👏")
  else:
    print("You typed invalid number you lose...!!!")  
